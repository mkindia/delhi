

// for alert message
function alertmsg(msg, duration) {
  var msgdiv=document.createElement("div");
  msgdiv.innerHTML +='<br><input id="prompt_value1"/>';  
  var el = msgdiv.appendChild(document.createElement("div"));
 // msgdiv.className="basemodal";
 // el.className="base-modal-content";
   msgdiv.setAttribute("style", "   z-index: 999998; top:0;  left:0; right:0; bottom:0; position:absolute; padding:10px; background-color: rgba(0,0,0,0.1); text-align: center;");
  

   el.setAttribute("style", "  margin: 0 auto; z-index: 999999; top:47px; width:350px; padding:17px;  font-style: italic;  left:0; right:0; position:absolute; border-radius:8px;color:#f0f0f0;border-color:#f0f0f0; border-width:1px; border-style: solid; background-color:#36486b; opacity: 0.9; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19); -webkit-animation-name: animatetop;  -webkit-animation-duration: 0.4s;  animation-name: animatetop;  animation-duration: 0.4s");

  el.innerHTML = msg.toUpperCase();
  setTimeout(function () {
      el.parentNode.removeChild(el);
      msgdiv.parentNode.removeChild(msgdiv);
     
  }, duration);
  
  document.body.appendChild(msgdiv);
 
  document.body.appendChild(el);
}

//Custom Propmt dialogbox
function CustomPrompt() {

  this.render = function(header,dialog,fctn){
  // alert("hello");
 
  var msgdiv=document.createElement("div");
  msgdiv.id='maindiv';
  msgdiv.className = 'basemodal';
  msgdiv.style='position:absolute;';
 // msgdiv.setAttribute("style", "   z-index: 999998; top:0;  left:0; right:0; bottom:0; position:absolute; padding:10px; background-color: rgba(0,0,0,0.1); text-align: center;");
  document.body.appendChild(msgdiv);
  var maindiv= document.getElementById("maindiv");
  var content = document.createElement("div");
      content.id='content';
      content.className='base-modal-content col-l-4 col-m-5 col-s-10 col-';
      content.style='margin-top: 50px; display:block;';
      maindiv.appendChild(content);

  var cont_id =document.getElementById('content');
  var d_header = document.createElement("div");
      d_header.id='header';
     // el.setAttribute("style", "  margin: 0 auto; z-index: 999999; top:47px; width:350px; padding:17px; height:100px; font-style: italic;  left:0; right:0; position:absolute; border-radius:8px;color:#f0f0f0;border-color:#f0f0f0; border-width:1px; border-style: solid; background-color:#36486b; opacity: 0.9; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19); -webkit-animation-name: animatetop;  -webkit-animation-duration: 0.4s;  animation-name: animatetop;  animation-duration: 0.4s");
      d_header.className='base-modal-header';      
      cont_id.appendChild(d_header);
  var d_header_id= document.getElementById('header');
  var d_header_h = document.createElement('h');
      d_header_h.style='position: relative; font-weight: bold; margin:0; top: 25%; -ms-transform: translateY(-50%);transform: translateY(-50%);';
      d_header_h.innerHTML = header ;
      d_header_id.appendChild(d_header_h);

  var d_body=document.createElement("div");
      d_body.id='d_body';
      d_body.className='base-modal-body col-l-12 col-m-12 col-s-12'
      d_body.setAttribute("style", "margin-top:10px; margin-bottom:20px;"); 
      d_body.innerHTML=dialog;
      cont_id.appendChild(d_body);

  var d_body_id=document.getElementById('d_body');
  var inputdialog = document.createElement("input");
      inputdialog.id='inputdialog';
      inputdialog.setAttribute("style", "border:1px solid black; font-size:18px; height:30px; border-radius:7px; width:100%;"); 
      d_body_id.appendChild(inputdialog);     
 

  var d_footer = document.createElement("div")
      d_footer.id='d_footer'
      d_footer.className = 'base-modal-footer col-l-12 col-m-12 col-s-12';
      d_footer.innerHTML = '<button class="buttonstyle" style="float:right; margin-top:5px; margin-right:10px;" onclick="c_prompt.ok(\''+fctn+'\')">OK</button> <button style="float:right; margin-top:5px; margin-right:10px;" class="buttonstyle" onclick="c_prompt.cancel()">Cancel</button>';	
      cont_id.appendChild(d_footer);

  
  }
  this.cancel = function(){
   
		document.getElementById('maindiv').parentNode.removeChild(maindiv);
	//document.getElementById('content').style.display = "none";
   
    
	}
	this.ok = function(fctn){
		var prompt_value1 = document.getElementById('inputdialog').value;
		window[fctn](prompt_value1);
		document.getElementById('maindiv').parentNode.removeChild(maindiv);
	
	}
}
var c_prompt = new CustomPrompt();

function CustomAlert() {

  this.render = function(header,dialog,duration){
 // alert(duration);
 
  var msgdiv=document.createElement("div");
  msgdiv.id='maindiv';
  msgdiv.className = 'basemodal';
  msgdiv.style='position:absolute;';
 // msgdiv.setAttribute("style", "   z-index: 999998; top:0;  left:0; right:0; bottom:0; position:absolute; padding:10px; background-color: rgba(0,0,0,0.1); text-align: center;");
  document.body.appendChild(msgdiv);
  var maindiv= document.getElementById("maindiv");
  var content = document.createElement("div");
      content.id='content';
      content.className='base-modal-content col-l-4 col-m-5 col-s-10 col-';
      content.style='margin-top: 50px; display:block;';
      maindiv.appendChild(content);

  var cont_id =document.getElementById('content');
  
  var d_header = document.createElement("div");
      d_header.id='header';
      d_header.style='background-color: #e4e4e4;';    
      d_header.className='base-modal-header';      
      cont_id.appendChild(d_header);

  var d_header_id= document.getElementById('header');
  var d_header_h = document.createElement('h');
      d_header_h.style='position: relative; font-weight: bold; margin:0; top: 25%; -ms-transform: translateY(-50%);transform: translateY(-50%);';
      d_header_h.innerHTML = header ;
      d_header_id.appendChild(d_header_h);

  var d_body=document.createElement("div");
      d_body.id='d_body';
      d_body.className='base-modal-body col-l-12 col-m-12 col-s-12'
      d_body.setAttribute("style", "margin-top:10px; margin-bottom:20px;  text-align: center;"); 
      d_body.innerHTML=dialog;
      cont_id.appendChild(d_body);

 

  var d_footer = document.createElement("div")
      d_footer.id='d_footer'
      d_footer.className = 'base-modal-footer col-l-12 col-m-12 col-s-12';
      d_footer.innerHTML = '<button style="float:right; margin-top:5px; margin-right:10px;" class="buttonstyle" onclick="c_alert.ok()">Ok</button>';	
      cont_id.appendChild(d_footer);

  if(duration != "undefined" && duration != '' && duration !=null )
  {
  
  setTimeout(function () {
    var element =  document.getElementById('maindiv');
    if (typeof(element) != 'undefined' && element != null)
    {
      document.getElementById('maindiv').parentNode.removeChild(maindiv);
    }
      
    }, duration);
  }
    
  }
 
	this.ok = function(){
   
		document.getElementById('maindiv').parentNode.removeChild(maindiv);
   
	}
  
}
var c_alert = new CustomAlert();

function CustomConfirm(){
 this.render = function (header,dialog,fctn){
  // alert("hello");
 
  var msgdiv=document.createElement("div");
  msgdiv.id='maindiv';
  msgdiv.className = 'basemodal';
  msgdiv.style='position:absolute;';
 // msgdiv.setAttribute("style", "   z-index: 999998; top:0;  left:0; right:0; bottom:0; position:absolute; padding:10px; background-color: rgba(0,0,0,0.1); text-align: center;");
  document.body.appendChild(msgdiv);
  var maindiv= document.getElementById("maindiv");
  var content = document.createElement("div");
      content.id='content';
      content.className='base-modal-content col-l-4 col-m-5 col-s-10 col-';
      content.style='margin-top: 50px; display:block;';
      maindiv.appendChild(content);

  var cont_id =document.getElementById('content');
  var d_header = document.createElement("div");
      d_header.id='header';
     // el.setAttribute("style", "  margin: 0 auto; z-index: 999999; top:47px; width:350px; padding:17px; height:100px; font-style: italic;  left:0; right:0; position:absolute; border-radius:8px;color:#f0f0f0;border-color:#f0f0f0; border-width:1px; border-style: solid; background-color:#36486b; opacity: 0.9; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19); -webkit-animation-name: animatetop;  -webkit-animation-duration: 0.4s;  animation-name: animatetop;  animation-duration: 0.4s");
      d_header.className='base-modal-header';      
      cont_id.appendChild(d_header);
  var d_header_id= document.getElementById('header');
  var d_header_h = document.createElement('h');
      d_header_h.style='position: relative; font-weight: bold; margin:0; top: 25%; -ms-transform: translateY(-50%);transform: translateY(-50%);';
      d_header_h.innerHTML = header ;
      d_header_id.appendChild(d_header_h);

  var d_body=document.createElement("div");
      d_body.id='d_body';
      d_body.className='base-modal-body col-l-12 col-m-12 col-s-12'
      d_body.setAttribute("style", "margin-top:10px; margin-bottom:20px; text-align: center;"); 
      d_body.innerHTML=dialog;
      cont_id.appendChild(d_body);

 

  var d_footer = document.createElement("div")
      d_footer.id='d_footer'
      d_footer.className = 'base-modal-footer col-l-12 col-m-12 col-s-12';
      d_footer.innerHTML = '<button class="buttonstyle" style="float:right; margin-top:5px; margin-right:10px;" onclick="c_confirm.ok(\''+fctn+'\')">OK</button> <button style="float:right; margin-top:5px; margin-right:10px;" class="buttonstyle" onclick="c_confirm.cancel(\''+fctn+'\')">Cancel</button>';	
      cont_id.appendChild(d_footer);

  
  }
  this.cancel = function(fctn){
    window[fctn](false);
		document.getElementById('maindiv').parentNode.removeChild(maindiv);
	}
	this.ok = function(fctn){	
		window[fctn](true);
		document.getElementById('maindiv').parentNode.removeChild(maindiv);
	
	}

}

var c_confirm = new CustomConfirm();


// for input list  datalist  validation
var inputs = document.querySelectorAll(".validdatalist"); //input[list] for all input type thar have list
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


function selectedDatalistAttributeValue(inputId,datalistId,attributeName){

  let elem= document.getElementById(inputId.trim());
  //let atrivalue = 'please select a valid option';
  let dt = document.getElementById(datalistId.trim());
for (let i = 0; i < dt.childElementCount; i++) {
// check the selected value with option values.
if (dt.children[i].attributes.value.value === elem.value) {
// if Hit use the attributes object to find your attribute and get its value.
let atrivalue = dt.children[i].getAttribute(attributeName);
return atrivalue;
}
}

}