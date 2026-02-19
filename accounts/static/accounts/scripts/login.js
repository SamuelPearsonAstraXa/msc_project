const username = document.getElementById('id_username');
const password = document.getElementById('id_password');

username.setAttribute('autocomplete', 'new-username')
username.setAttribute('placeHolder', 'Email address')
username.setAttribute('title', 'Email address')

password.setAttribute('autocomplete', 'new-password')
password.setAttribute('placeHolder', 'Password')
password.setAttribute('title', 'Password')