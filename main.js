
var btbutton = document.getElementsByClassName('btlogin');

function login(){
  var token = document.getElementById('password').value;
  var name = document.getElementById('username').value;
  if (name == '' || token == ''){
    alert('field not null !')
  };
  if (name == 'Phatker' && token == 'cyberbug2069'){
    window.location.href = 'page.html'
  }
  else{
    var error = document.getElementById('error').value;
    error = 'error'
  }
}