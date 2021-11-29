// var - распростроняется в области функции, let и const, в любом блоке {}

function showAlert() {   // функция вызываемая по таймеру
    alert('moo!');
}
let timeoutID = setTimeout(showAlert, 5000);  // присваивается переменной для управления. (функция, 5 сек)

clearTimeout(timeoutID); // остановка таймера. передаём (переменная таймера)

//_______________________________________________________________________________

let intervalID = setInterval(showAlert, 2000);   //  работает циклом. (запускаемая функция, 2 сек)

clearInterval (intervalID);   // остановка интервала

//_______________________________________________________________________________

function stopWatch() {          //Показывает время выполнения кода
    let startTime = Date.now();     //фиксация времени запуска

    function getDelay() {
        let elapsedTime = Date.now() - startTime;   // расчёт разницы от первого запуска, для дальнейшего вычисления
        alert(elapsedTime + ' миллисек.');
    }

    return getDelay;  // возвращает прошедшее время
}
let timer = stopWatch();       // Запуск
timer();                    // Получение результата

//_______________________________________________________________________________

//Варианты для консоли

console.log("This is text");
console.warn("This is a warning!");
console.error("This is an error!");


//_______________________________________________________________________________

// Сложение значений из массива, не используя цикл

const euros = [23, 23.5, 63.32, 45];
const sum = euros.reduce((total, amount) => total + amount);    
// аналогично - const sum = euros.reduce(function(total, amount) {return total + amount;}, 0);    0 - это начальное значение
//total содержит итоговое значение, полученное в результате всех произведенных на этот момент действий; 
//amount — это текущий элемент массива. 


//_______________________________________________________________________________

// Выбор эелемента в DOM

let element = document.querySelector(".class || #id || html || a[href='#']"); // не примет :visited, :link, ::before, ::after
let element = document.querySelectorAll("те же варианты"); // можно обращаться как с масовом element[i], element.length

// Возврат значения 

element.getAttribute(""); // возврат значения атрибута в скобках
element.id || element.class     // короткая запись только для этих двух атрибутов

// Запись значения

element.setAttribute("src", "https:\\"); // запись атрибута
element.className = "" // короткий вариант. Производит ПЕРЕЗАПИСЬ

element.textContent = "" // метод установки текста контента. 
// Установка CSS прямо в тег, типа element.style.backgroundColor = "".
// Что бы указать CSS свойство содержащее тире, нужно его удалить типа: border-radius,  будет: borderRadius

// Работа с классами

element.classList. // одно из...
                  add(""); // добавить класс
                  remove(""); // удалить
                  toggle(""); // переключить (методом удаления и добавления) с вкл на выкл и обратно
                  contains(""); // булево, содержит ли указанный класс


// Прогулка по "DOM-у"

firstChild
lastChild
parentNode
children
previousSibling
nextSinling

// Вариант прогулки по потомкам

let bodyElement = document.body;

for (let i = 0; i < bodyElement.children.length; i++) {  // число детей у элемента
    let childElement = bodyElement.children[i];  // обращатся можно как к элементу массива
    document.writeln(childElement.tagName); // writeln выводит имена тэгов со знаком перевода каретки, в документ (этот html)
}

// Вариант прогулки рекурсией

function theDOMElementWalker(node) {
    if (node.nodeType == Node.ELEMENT_NODE) {
        console.log(node.tagName);
        node = node.firstChild;

        while (node) {
            theDOMElementWalker(node);
            node = node.nextSibling;
        };
    };
};
let variable = document.querySelector(".class");
theDOMElementWalker(variable);

// Созданае элементов

let element = document.createElement("p"); // пока не отображается и сам по себе
element.textContent = "какой то текст"; //можно и потом

let parentElement = document.querySelector("body"); // выбор родителя для элемента
parentElement.appendChild(element); // добавление родителю потомка. Встаёт последним ребёнком

let child_old = document.querySelector("");  // выбор ребёнка на место которого вставить, сдвинув этого
parentElement.insertBefore(element, child_old); // вставка потомка в определённое место
                                    elemChild.nextSibling // вставит потомка после элемента elemChild. Удобно, не выяснять кого мы сдвигаем
            
// Удаление потомка

parentElement.removeChild(element);
element.parentNode.removeChild(element); // что бы не искать родителя удаляемого потомка
// или просто 
element.remove();

// Клонирование элементов

let parentElement = document.querySelector("body"); // кому припаяем клонированого потомка
let element = document.querySelector("h1"); // кого клонируем
let clon = element.cloneNode(true); // true - нужноли клонировать его потомков
parentElement.appendChild(clon); // добавили потомка


//проверка