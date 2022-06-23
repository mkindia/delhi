export function whatsapp(mobile,message){
    if (typeof mobile != undefined){
    window.open("https://wa.me/91"+mobile+"/?text="+message); 
    } 
    else{alert('Mobile no. not Found');}
  }
  