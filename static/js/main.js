var login = document.querySelector('.login')
var register = document.querySelector('.register')
var registerform = document.querySelector('.auth-form')

document.querySelectorAll('[data-login]').forEach( loginfunction =>
    {

    loginfunction.addEventListener('click', ()=> {

        register.style.backgroundColor = 'white';

        login.style.backgroundColor = 'rgba(248, 245, 245, 0.808)';

        document.querySelector('.auth-form').style.display = 'none';

        document.querySelector('.login-form').style.display = 'block';


  })

})

document.querySelectorAll('[data-register]').forEach(registerfunction => {

    registerfunction.addEventListener('click', ()=> {

        register.style.backgroundColor = 'rgba(248, 245, 245, 0.808)';

        login.style.backgroundColor = 'white';

        registerform.style.display = 'block';

        document.querySelector('#id_username').placeholder = 'username';

        document.querySelector('#id_password1').placeholder = 'password';

        document.querySelector('#id_password2').placeholder = 'password confirmation';

        document.querySelector('.login-form').style.display = 'none';
    })

})