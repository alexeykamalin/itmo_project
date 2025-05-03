from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from fastapi import HTTPException
from qwen_vl_utils import process_vision_info
import torch
import pika
import logging
from services.crud.prediction import updateprediction
from database.database import get_session
from models.prediction import PredictionUpdate

logging.basicConfig(
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
# Настройка логирования 

connection_params = pika.ConnectionParameters(
    host='rabbitmq',  # Замените на адрес вашего RabbitMQ сервера
    port=5672,          # Порт по умолчанию для RabbitMQ
    virtual_host='/',   # Виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(
        username='rmuser',  # Имя пользователя по умолчанию
        password='rmpassword'   # Пароль по умолчанию
    ),
    heartbeat=30,
    blocked_connection_timeout=2
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
queue_name = 'ml_task_queue'
channel.queue_declare(queue=queue_name)  # Создание очереди (если не существует)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
# Функция, которая будет вызвана при получении сообщения
def callback(ch, method, properties, body):
    logger.info("1 %s", 'lol')
    try:
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": body.decode("utf-8"),
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ]
        logger.info("2")
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        logger.info("3")
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        logger.info("4")
        inputs = inputs.to("cuda")
        generated_ids = model.generate(**inputs, max_new_tokens=128)
        generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        logger.info('-------------------------------------------------------------------------------конец задачи')
        # logger.info('Тут пока заглушка, хочу получить ответ от МЛ: %s', output_text)
    except:
        pass

# Подписка на очередь и установка обработчика сообщений
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True  # Автоматическое подтверждение обработки сообщений
)

channel.start_consuming()