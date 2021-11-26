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



