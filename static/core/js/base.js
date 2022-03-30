
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
if (event.target == menumodal) {

menumodal.style.display = "none";
}
}

// for alert message
function alertmsg(msg, duration) {
  var el = document.createElement("div");

  el.setAttribute("style", " font-style: italic; margin:50 auto;  left:1; right:1; margin-bottom:15px; position: absolute;border-radius:8px;color:#f0f0f0;border-color:#f0f0f0; border-width:1px; border-style: solid;z-index:10000; padding:6px; background-color:#36486b;text-align: center;");

  el.innerHTML = msg.toUpperCase();
  setTimeout(function () {
      el.parentNode.removeChild(el);
  }, duration);
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
