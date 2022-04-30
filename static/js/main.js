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


document.addEventListener('click', e => {
    var dropdown = e.target.matches("[data-dropdown]")

    const currentdropdown =  e.target.closest('[data-dropdown]')

    if (dropdown) {
    currentdropdown.classList.toggle('active')
    }

    if (!dropdown) {
        currentdrop = document.querySelectorAll('[data-dropdown]').forEach(dropdown => dropdown.classList.remove('active'))

    }

	document.querySelectorAll('[data-dropdown].active').forEach(drop => {
        if(drop === currentdropdown) return
        drop.classList.remove('active')
    })

})



var addToRead = document.querySelectorAll('.readlist');

addToRead.forEach(button => {

    button.addEventListener('click', function(){

    var bookId = this.dataset.bookid
    var action = this.dataset.action
    console.log('bookId:', bookId, 'action:', action);

    updatecart(bookId, action);

})

})


function updatecart(bookId, action){

    var body = {'bookId':bookId, 'action':action};
    $.ajax({
        headers:{'X-CSRFToken':csrftoken},
        type:'POST',
        url:'/addRead/',
        data:JSON.stringify(body),
        success: function(){

        }
    })
}





var addToRead = document.querySelectorAll('.archive');

addToRead.forEach(button => {

    button.addEventListener('click', function(){

    var bookId = this.dataset.product
    var action = this.dataset.action
    console.log('bookId:', bookId, 'action:', action, 'User:', user);

    updatecart(productId, action);

})

})


function updatecart(bookId, action){

    var body = {'bookId':bookId, 'action':action};
    $.ajax({
        headers:{'X-CSRFToken':csrftoken},
        type:'POST',
        url:'/archived/',
        data:JSON.stringify(body),
        success: function(){

        }
    })
}
