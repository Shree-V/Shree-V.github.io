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

const height = document.documentElement.clientHeight;
const width = document.documentElement.clientWidth;
const button3 = document.querySelector('#enter').addEventListener('click', enter);
const box = document.getElementById("container");

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
  const num = Math.floor(Math.random() * (1000 - 1));
  console.log(num);
  if (Number(current) - num < Number(lowerLim)) {
    upper = lowerLim;
  } 
  else {
    upper = Number(current) - num;
  }
  
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
  const num = Math.floor(Math.random() * (1000 - 1));
  console.log(num);
  if (Number(current) + num > Number(upperLim)) {
    lower = upperLim;
  } 
  else {
    lower = Number(current) + num; 
  }
  
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

function randomPosition() {
  let randY = Math.floor((Math.random() * height) + 1);
  let randX = Math.floor((Math.random() * width) + 1);
  box.style.transform = `translate(${randX}px, ${randY}px)`;
  randomPosition();
}

// document.ready(function(){
//   animateDiv('.container');
// });

// function makeNewPosition(){
    
//   // Get viewport dimensions (remove the dimension of the div)
//   // var h = window.height() - 50;
//   // var w = window.width() - 50;
  
//   var nh = Math.floor(Math.random() * height);
//   var nw = Math.floor(Math.random() * width);
  
//   return [nh,nw];    
  
// }

// function animateDiv(myclass){
//   var newq = makeNewPosition();
//   myclass.animate({ top: newq[0], left: newq[1] }, 1000,   function(){
//     animateDiv(myclass);        
//   });
  
// };