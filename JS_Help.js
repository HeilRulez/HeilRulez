// var - распростроняется в области функции, let и const, в любом блоке {}

function showAlert() {   // функция вызываемая по таймеру
    alert('moo!');
}
let timeoutID = setTimeout(showAlert, 5000);  // присваивается переменной для управления. (функция, 5 сек)

clearTimeout(timeoutID); // остановка таймера. передаём (переменная таймера)

//////////////////////////

let intervalID = setInterval(showAlert, 2000);   //  работает циклом. (запускаемая функция, 2 сек)

clearInterval (intervalID);   // остановка интервала

//////////////////////////

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

//////////////////////////

//Варианты для консоли

console.log("This is text");
console.warn("This is a warning!");
console.error("This is an error!");