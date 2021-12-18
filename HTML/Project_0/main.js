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


function pow(x, n) {
    return n % 1 == 0 ? x**n : alert("Ошибка");
};

let x = prompt("Введите число", 0);
let n;
do {
    n = prompt("Введите второе целое число", 1);
}while(!(n >= 1 && n % 1 == 0));

alert(`Результат: ${pow(x, n)}`);
