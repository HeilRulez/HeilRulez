"use strict";

function createElem(element) {
    let bodyElement = document.querySelector('body');
    let addElement = document.createElement(element);
    bodyElement.appendChild(addElement);
    addElement.textContent = "Hello, JS!";

    return addElement;
};

let userName = prompt("Как тебя величать?", "");
alert(`Привет, ${userName}`);

