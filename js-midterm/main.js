var upper = "9999999999"; 
var lower = "0000000000"; 

var current = "5555555555"; 
var phonestring = current;

var tempstring = "";
var extrazeros = 0;


const upperLim = upper;
const lowerLim = lower;

// $(document).ready(function() {
  
//   $('#decrease').click(decrease);
//   $('#increase').click(increase);
  
//   $('#enter').click(enter);


const button3 = document.querySelector('#enter').addEventListener('click', enter);

function enter() {
  alert("You submitted: " + numberToString(current)); 
}

function numberToString(p) {
  var sp = "" + p; 
  var acc = ""; 
  for(var i=0; i < sp.length; i++) {
    acc += sp.charAt(i);
    if([2, 5].indexOf(i) != -1) {
      acc += "-";
    }
  }
  return acc; 
}

function updateDisplay() {
//   current = Math.floor((upper + lower) / 2); 
    phonestring = numberToString(current);
//   $("#phone-number").html(numberToString(current)); 
}

function decrease() {
  upper = Number(current) - 1;
  if (upper >= lowerLim) {
    current = upper;
  }
  current = "" + current;
  upper = "" + upper;
  if (current.length < 10) {
    extrazeros = 10 - current.length;
    for (let i = 0; i < extrazeros; i++) {
        tempstring += "0";
    }
    current = tempstring + current;
    tempstring = "";
  }
}

function increase() {
  lower = Number(current) + 1; 
  if (lower <= upperLim) {
    current = lower;
  }
  current = "" + current;
  lower = "" + lower;
  if (current.length < 10) {
    extrazeros = 10 - current.length;
    for (let i = 0; i < extrazeros; i++) {
        tempstring += "0";
    }
    current = tempstring + current;
    tempstring = "";
  }
   //updateDisplay(); 
}   

