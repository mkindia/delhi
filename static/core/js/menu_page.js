openeddiv = ['Menu'];
function showhide(d, sd) {
  x = document.getElementById(d).innerText;
  document.getElementById(sd).classList.toggle('show');
  openeddiv.push(x);
  document.getElementById('menuhead').innerText = x;
  document.getElementById('backbtn').classList.add('backbtn');
  h = document.getElementById("menuitembody").classList.add('overflowy-h');
}

function closemenu(){
  document.getElementById('menuModal').style.display="none";
}



function showhide1() {
  var divcount = 1;
  var divclasses = 0;
  var spans = document.getElementsByTagName("div");

  for (var i = 0; i < spans.length; i++) {
    if (spans[i].className == 'showdiv show') {
      // spans[i].style.backgroundColor = '#030';
      // spans[i].classList.remove('show');       
      divcount = divcount + 1;
      divclasses = i;


    }

  }

  if (divcount > 1) {
    document.getElementById('menuhead').innerText = openeddiv[divcount - 2];
    openeddiv.pop();
    spans[divclasses].classList.remove('show');
    divcount = divcount - 1;
  }
  if (divcount == 1) {
    document.getElementById('backbtn').classList.remove('backbtn');
    document.getElementById("menuitembody").classList.remove('overflowy-h');
  }

} 
