
var loginmodal = document.getElementById("loginModal");
var loginbtn = document.getElementById("loginBtn");
var menumodal = document.getElementById("menuModal");
var menubtn = document.getElementById("menuBtn");
var profilebtn = document.getElementById("profilebtn");
   // menubtn.style.display="none";

loginbtn.onclick = function(event) {  
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


menubtn.onclick = function(event){
  menumodal.style.display = "block";
}




profilebtn.onclick = function(event) 
{
  document.getElementById("profile-modal").classList.toggle('show');
 }