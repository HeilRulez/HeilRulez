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