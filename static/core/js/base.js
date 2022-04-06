
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
if (event.target == menumodal) {

menumodal.style.display = "none";
}
}

// for alert message
function alertmsg(msg, duration) {
  var msgdiv=document.createElement("div");
  var el = msgdiv.appendChild(document.createElement("div"));
 // msgdiv.className="basemodal";
 // el.className="base-modal-content";
   msgdiv.setAttribute("style", "   z-index: 999998; top:0;  left:0; right:0; bottom:0; position:absolute; background-color: rgba(0,0,0,0.2); text-align: center;");
  el.setAttribute("style", "  margin: 0 auto; z-index: 999999; top:47px; width:99%;  font-style: italic;  left:0; right:0; position:absolute; border-radius:8px;color:#f0f0f0;border-color:#f0f0f0; border-width:1px; border-style: solid; padding:25px; background-color:#36486b;text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19); -webkit-animation-name: animatetop;  -webkit-animation-duration: 0.4s;  animation-name: animatetop;  animation-duration: 0.4s");

  el.innerHTML = msg.toUpperCase();
  setTimeout(function () {
      el.parentNode.removeChild(el);
      msgdiv.parentNode.removeChild(msgdiv);
  }, duration);
  
  document.body.appendChild(msgdiv);
  document.body.appendChild(el);
}

// for input list  datalist  validation
var inputs = document.querySelectorAll("input[list]");
for (var i = 0; i < inputs.length; i++) {
  // When the value of the input changes…
  inputs[i].addEventListener("change", function () {
    
    var optionFound = false,
      datalist = this.list;
    // Determine whether an option exists with the current value of the input.
    for (var j = 0; j < datalist.options.length; j++) {
      if (this.value == datalist.options[j].value) {
        optionFound = true;
        break;
      }
    }
    // use the setCustomValidity function of the Validation API
    // to provide an user feedback if the value does not exist in the datalist
    if (optionFound) {
      this.setCustomValidity("");      
    } else {
      this.setCustomValidity("Please select a valid value.");
    }
  });
}

// get datalist id 
function selecteddatalistid(inputid,datalistid)
{
    var    input = document.getElementById(inputid)
    var    list = document.getElementById(datalistid)
    var    i,idc=null;
    for (i = 0; i < list.options.length; ++i)
    {
        if (list.options[i].value === input.value) 
        {
            idc = list.options[i].getAttribute('data-id');            
            return idc;           
            
        }       
    }
}
