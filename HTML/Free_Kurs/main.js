function changeColor(event) {
  if (document.body.style.getPropertyValue("background-color") == "rgb(255, 201, 38)") {
    document.body.style.backgroundColor = "#fff";
  }else if (document.body.style.getPropertyValue("background-color") == "rgb(255, 255, 255)") {
    document.body.style.backgroundColor = "#ffc926";
  };
  OutPut(event, event.type);
};

function colorHeading(event) {
  event.target.style.color = "#000";
  OutPut(event, event.type);
};
function hovered(event) {
  event.target.style.color = "#000";
  OutPut(event, event.type);
};
function hoveredOut(event) {
  event.target.style.color = "#0099FF";
  OutPut(event, event.type);
};
function btnChangeFn(event) {
  if (event.type == 'dblclick') {
    OutPut(event, event.type);
  }else {
    OutPut(event, event.type);
  };
};


function OutPut (current, st="null") {
  outPutTxt.textContent = ("Tag: " + current.target.tagName + ", ID: " + current.target.id + ", " + st);
};

let bodyElm  = document.querySelector("#colorBody");
let heading = document.querySelector("#bigMessage");
let heading_2 = document.querySelector("#bigMessage_2");
let outPutTxt = document.querySelector("#outputText");
let btnChange = document.querySelector("#btnChange");

bodyElm.addEventListener('click', changeColor, false);
heading.addEventListener('click', colorHeading, false);
heading_2.addEventListener('mouseover', hovered, false);
heading_2.addEventListener('mouseout', hoveredOut, false);

btnChange.addEventListener('mousedown', btnChangeFn, false);
btnChange.addEventListener('mouseup', btnChangeFn, false);
btnChange.addEventListener('dblclick', btnChangeFn, false);
