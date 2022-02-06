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

let menu = {
    width: 200,
    height: 300,
    title: "My menu",
};

multiplyNumeric(menu);

function multiplyNumeric(obj) {
    for (let key in obj) {
        if (typeof obj[key] == "number") {
            menu[key] *= 2;
        };
    };
}

for (let item in menu) {
    alert(menu[item]);
};
