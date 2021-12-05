
var loginmodal = document.getElementById("loginModal");
var loginbtn = document.getElementById("loginBtn");
var menumodal = document.getElementById("menuModal");
var menubtn = document.getElementById("menuBtn");
   // menubtn.style.display="none";

loginbtn.onclick = function() {  
 loginmodal.style.display = "block";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == loginmodal || event.target == menumodal) {
    loginmodal.style.display = "none";
    menumodal.style.display ="none";
  }
}


//var span1 = document.getElementsByClassName("close")[1];


menubtn.onclick = function(){
  menumodal.style.display = "block";
}


