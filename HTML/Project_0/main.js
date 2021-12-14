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


const number = +prompt('Введите число между 0 и 3', '');

switch (number) {
    case 0:
        alert('Вы ввели 0');
        break;
    case 1:
        alert('Вы ввели 1');
        break;
    case 2:
    case 3:
        alert('Вы ввели 2, а может 3');
        break;
};