$(document).ready(function() {

    // 1 - Перемінні флаги результатів валідації
    let res1 = false;
    let res2 = false;
    let res3 = false;
    let res4 = false;

    // 2 - Валідація логіна
    $('#login').blur(function() {
        let loginX = $('#login').val();
        let loginR = /^[a-zA-Z][a-zA-Z0-9_]{5,15}$/;
        if (loginR.test(loginX) == true){
            $('#login-err').text('');
            res1 = true;
            // Провірка занятості логіна...
            $.ajax({
                url:'/account/ajax_reg',
                data:'login=' + loginX,
                success: function(result) {
                    if (result.message === 'занятий'){
                        $('#login-err').text('Логін - занятий! Виберіть інший');
                        res1 = false;
                    } else {
                        $('#login-err').text('');
                        res1 = true
                    }
                }
            });
        } else {
            $('#login-err').text('Логін - НЕ правельний');
            res1 = false;
        }
    });

    // 3. Валідація 1 пароля
    $('#pass1').blur(function() {
        let pass1X = $('#pass1').val();
        let pass1R = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_]{8,}$/;
        if (pass1R.test(pass1X) == true){
            $('#pass1-err').text('');
             let res2 = true;
        } else {
            $('#pass1-err').text('Пароль - НЕ правельний');
             let res2 = false;
        }
    });

    // 4. Валідація 2 паролю
    $('#pass2').blur(function() {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X){
            $('#pass2-err').text('');
            let res3 = true;
        } else {
            $('#pass2-err').text('Пароль - НЕ одинковий');
            let res3 = false;
        }
    });

    // 5.Валідація скриньки
    $('#email').blur(function() {
        let emailX = $('#email').val();
        let emailR = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailR.test(emailX) == true){
            $('#email-err').text('');
            let res4 = true;
        } else {
            $('#email-err').text('Email - НЕ правельний');
            let res4 = false;
        }
    });

    // #. Фінальна перевірка
    $('#submit').click(function(){
        if (res1 == true && res2 == true && res3 == true && res4 == true){
            $('#form-1').attr('onsubmit', 'return true'); // - Розблокування форми
        } else {
            $('#form-1').attr('onsubmit', 'return true'); // - Розблокування форми
            alert('Форма має не коректні данні! \nВідправка данних заблокована!')
        }
    });
});