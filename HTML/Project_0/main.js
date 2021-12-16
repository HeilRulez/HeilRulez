"use strict";

function createElem(element) {
    let bodyElement = document.querySelector('body');
    let addElement = document.createElement(element);
    bodyElement.appendChild(addElement);
    addElement.textContent = "Hello, JS!";

    return addElement;
};


// let input = prompt("Integer", 2);
// let arr = [];

// nextIterate:
// for (let j = 2; j <= input; j++) {
//     for(let i = 2; i < j; i++){
//         if (j % i == 0) continue nextIterate;
//     };
//     arr.push(j);
// };
// alert(arr);


let ask = (question, yes, no) =>
    confirm(question) ? yes() : no();

ask("Вы согластны?",
    () => alert("Вы согласились."),
    () => alert("Вы отменили выполнение.")
    );