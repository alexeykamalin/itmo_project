
(function ($) {
    "use strict";
    /*==================================================================
    [ Validate ]*/

    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    function Validation() {
        var check = true;
        
        return check
    }
    /*==================================================================
    [ Validate ]*/
    $('#add_balance').on('click', function(){
        if(Validation()){
            $.ajax({
                contentType: 'application/json',
                url: '/api/balance/update_balance',
                type: 'POST',
                data: JSON.stringify({
                    value: $('#tugrik').val(),
                    user_id: $('#options').attr('user_id'),
                })
            }).done(function(data){
                console.log(data);
                if(data.result){
                    window.location.href = '/';
                }
            });
        }
    })
    
})(jQuery);
