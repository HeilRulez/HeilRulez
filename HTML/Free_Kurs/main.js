function changeColor(event) {
  if (document.body.style.getPropertyValue ("background-color") == "rgb(255, 201, 38)") {
    document.body.style.backgroundColor = "#fff";
  }else if (document.body.style.getPropertyValue ("background-color") == "rgb(255, 255, 255)") {
    document.body.style.backgroundColor = "#ffc926";
  };
};

document.addEventListener('click', changeColor, false);

function colorHeading(event) {
  heading.style.color = "#000";
};
function hovered(event) {
  heading_2.style.color = "#000";
};
function hoveredOut(event) {
  heading_2.style.color = "#0099FF";
};

let heading = document.querySelector("#bigMessage");
let heading_2 = document.querySelector("#bigMessage_2");

heading.addEventListener('click', colorHeading, false);
heading_2.addEventListener('mouseover', hovered, false);
heading_2.addEventListener('mouseout', hoveredOut, false);
