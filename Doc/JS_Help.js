// var - распростроняется в области функции, let и const, в любом блоке {}

function showAlert() {   // функция вызываемая по таймеру
    alert('moo!');
}
let timeoutID = setTimeout(showAlert, 5000);  // присваивается переменной для управления. (функция, 5 сек)

clearTimeout(timeoutID); // остановка таймера. передаём (переменная таймера)


// Модальные окна

let result = prompt("title", "default"); //как alert с текстовым полем. default - необязательный
// введённый текст будет в result. При отмене вернёт null

let result = confirm("Тут например вопрос?");
// Вернёт true или false, что нажато - ok или отмена


debugger;   // создаст точку останова при отладке

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
console.dir(document.body);     // отобразит список свойств и методов переданного объекта


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

// Проверка значения

element.hasAttribute('disabled')  // вернёт true если есть заданный атрибут

element.removeAttribute('disabled')   // удаление атрибута


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


//_______________________________ Добавление элементов______________________

let ul = document.querySelector('ul');
let li = document.querySelector('li');

node.append('li-1', 'li-2', 'li-3')        // добавляет узлы или строки в конец node
node.prepend(...nodes or strings)           // в начало node;
node.before(...nodes or strings)            // до node;
node.after(...nodes or strings)             // после node;
node.replaceWith(...nodes or strings)       // заменяет node заданными узлами или строками.

// Удаление элементов

const listItem = document.querySelector('li');
listItem.remove(); 

element.closest('.class-parant');      // возвращает ближайший родительский элемент

// Пример удаления всего злемента через кнопку

<li class='todo__item'>
    <span>Что то</span>
    <button class='todo__item-button'>Удалить</button>
</li>

const delButton = document.querySelector('.todo__item-button');

delButton.addEventListener('click', () => {
    const parant = delButton.closest('todo__item');
    parant.remove();
});

// Перемещение

const list = document.querySelector('.todo-list');

const listIt = list.children;       // в children хранится псевдомассив детей
list.append(listIt[0]);     // это вставит в конец выбранный элемент

// Копирование узлов

const deppCopy = elem.cloneNode(true);      // скопирует элемент с потомками. false - без потомков
parant.append(deepCopy);        // после, добавить куда либо

//_______________________________________________________________________________

// События

document.addEventListener('click', changeColor, false); // событие, функция, (true/false - погружение/высплытие)

document.removeEvetnListener('click', changeColor, false); // удаление слушателя

event.stopPropagation();    // остановка распространения события

// События мыши

click
dblclick
mouseover
mouseout
mouseenter
mouseleave
mousedown
mouseup
mousemove
contextmenu
mousewheel
DOMMouseScroll


// Колёсико

document.addEventListener('mousewheel', mouseWheel, false);     // события колеса для IE и Chrome
document.addEventListener('DOMMouseScroll', mouseWheel, false); // события колеса для Firefox

//mousewheel.wheelDelta значение. Вверх +1, вниз -1
//DOMMouseScroll.detail значение. Вверх -1, вниз +1

// Простой подход унифицировать события колёсика

function example(e) {
    let scrollDirection; //хранит значение wheelDelta или detail
    let wheelData = e.wheelDelta;

    if (wheelData) {                    //если свойство есть
        scrollDirection = wheelData;    //записали положение
    }else {
        scrollDirection = -1 * e.deteil;    // или переделали свойство firefox на противоположный знак
    };
    if (scrollDirection > 0) {
        console.log("Scrolling up! " + scrollDirection);
    }else {
        console.log("Scrolling down! " + scrollDirection);
    };
};


// События клавиш

keydown
keypress  // сработает только если клавиша отображает знак
keyup

window.addEventListener('keydown', fun, false);

// Свойства события Keyboard

KeyCode
CharCode // только у keypress содержит ASCII код
ctrKey, altKey, shiftKey // возвращает булево
MetaKey // булево для клавиши win/Command

// Example
function checkKeyPressed(e) {
    if (e.keyCode == 65) {
        console.log();
    };
};

// Example
function moveSomething(e) {
    switch (e.keyCode) {
        case 37:    // влево
            break;
        case 38:    // вверх
            break;
        case 39:    // вправо
            break;
        case 40:    // вниз
            break;
    };
};

// Example
let keys = []; // проверка комбинаций

function keysPressed(e) {
    keys[e.keyCode] = true; // сохраняет по индексу каждую клавишу в архив

    // Ctrl + Shift + 5
    if (keys[17] && keys[16] && keys[53]) {
        console.log();
    };

    // Ctrl + f
    if (keys[17] && keys[70]) {
        console.log();
        e.preventDefault(); // во вызовит поиск в браузере
    };
};
function keysReleased(e) {
    // отметит отпущеные клавиши
    keys[e.keyCode] = false;
};

//_______________________________________________________________________________

async   // атрибут <script async.. асинхронная загрузка скрипта. Хз в какой последовательности выполнятся.

defer   // запустится после всей загрузки, перед событием DOMContentLoaded. В отсичии от async

// События загрузки страницы

document.addEventListener('DOMContentLoaded', fun, false); // слушать в document
// Сработает когда будет загружена сырая разметка, без картинок и стелей.
// Достаточно для работы с DOM

window.addEventListener('load', fun, false);   // слушать в window
// Сработает когда случится полная загрузка документа


// Один обработчик на группу

// При прослушки события на элементе, оно прокатывается по всему дереву его потомков, срабатывая для каждого.
let theParent = document.quwrySelector('#thisParent'); // находим родителя группы элементов
theParent.addEventListener('click', doSomething, false);

function doSomething(e) {
    if (e.target != e.currentTarget) {  // target - целевой элемент, currentTarget - к кому прикреплён слушатель
        let clickedItem = e.target.id;  // конкретный элемент-ребёнок
        console.log("Click elem.");
    };
    e.stopPropagation(); // останавливаем распростронение события дальше по дереву
};

//_______________________________________________________________________________

// Побитовые оперпторы

/*

AND(и) ( & )
OR(или) ( | )
XOR(побитовое исключающее или) ( ^ )
NOT(не) ( ~ )
LEFT SHIFT(левый сдвиг) ( << )
RIGHT SHIFT(правый сдвиг) ( >> )
ZERO-FILL RIGHT SHIFT(правый сдвиг с заполнением нулями) ( >>> )

*/

//_______________________________________________________________________________

alert(`Привет, ${userName}`);       //Вставка переменной в строку

//_______________________________________________________________________________

(x > 0) && alert("Что то неважное");  //alert сработает если первое выражение вернёт ture

//_______________________________________________________________________________

a ?? b  // Оператор обьедиенения с null
a || b  // почти тоже самое

//  Отличие:
//  ||  возвращает первое истинное
//  ??  возвращает первое определённое, != null/undefined

result = (a !== null && a !== undefined) ? a : b;      // Понятное изложение

// Пример
let height = 0;

alert(height || 100); // 100
alert(height ?? 100); // 0

//_______________________________________________________________________________

// Выход из вложенных цыклов по break\continue

outer:      // имя метки любое
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++){
        let input = prompt("", "");
        if (!input) break outer;    // вернётся на уровень этой метки
    };
};

//_______________________________________________________________________________


switch (a) {        //Сравнение всегда строгое
    case 2:
        alert('Мало');
        break;
    case 4:
        alert('Достаточно');
        break;
    case 5:
    case 10:                 // Возможность групировать из за отсутствия break
        alert('Много');
        break;
    default:                // Необязательный
        alert('Не сегодня');
};

//_______________________________________________________________________________

// Применение Function Expression

let age = prompt("Сколькло вам лет?", 18);

let welcome = (age < 18) ?
    function() { alert("Привет!"); } :      // соддаётся на текуший момент
    () => alert("Здравствуйте!");           // вариант стрелочной функции

welcome();

//_______________________________________________________________________________

// Копирование Object


//Example_1

let user = {
    name: "Ivan",
    age: 30,
};

let clone = {};

for (let key in user) {
    clone[key] = user[key];
};


// Example_2

let user = { name: "Ivan"};

let perm_1 = { canView: true};
let perm_2 = { canEdit: true};

Object.assign(user, perm_1, perm_2);
// user теперь равно {name: "Ivan", canView: true, canEdit: true}

let user = {
    name: "Ivan",
    age: 30,
};

let clone = Object.assign({}, user);


// Example_3    Глубокое копирование
// Библиотека lodash
//  Метод _.cloneDeep(obj)


// ______________________ Добавление в DOM, теги и тексты ________________________

element.innerHTML = '<div class=""></div>';     // добавляет разметку в родитель. Перезаписывает. Можно +=
element.innerText = 'этот метод не увидит скрытый текст в разметке';        // лучьше не использовать
element.textContent = 'текст';      //  добавление текста

element.insertAdjacentHTML('beforeend', '<div></div>');    // в отличии от inner не перерендорит DOM и не 
                                                           // затрёт добавленное элементам через js

                                                          // beforeend - вставка перед закрывающим тегом содержащего элемента; 
                                                          // beforebegin - до открывающего тега; afterbegin - после 
                                                          // открывающего тега; afterend - после закрывающего тега
element.insertAdjacentText = '';

//_____________________________ Методы массива ____________________________

const array_one = ['1', '2', '3'];   
const array_two = array_one.concat('4', '5');   // создаёт новый массив с добавляет к массиву one свои аргументы. Так же в аргументах могут быть ссылки на массивы
// log => ['1', '2', '3','4', '5']

const array_three = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух'];
array_three.join();         // log => "Кот,Пёс,Трубадур,Осёл,Петух"  Метод создаёт строку из массива
     // .join(', ') log => "Кот, Пёс, Трубадур, Осёл, Петух"


// меняют исходный массив
arr.push('', '');       // в конец
arr.pop();          // удалит последний и возвращает его. если посто - undefined

arr.shift();        // удалит первый элемент и вернёт его значение
arr.unshift('', '');        // дабавит в начало массива ещё вернёт число элементов после добавления


Array.forEach(element => console.log(element));     // пройдёт по каждому элементу массива и примени функйию

Array.isArray(arr);                 // нужен для определения что это массив а не объект



const out = где_ищем.some(function(item) {        // some - проверяет наличие в массиве искомое. Возовращает булево
    return item === 'что ищем';
});

const out_1 = где_ищем.find(function (item) {        // find разница от some - вернёт значение элемента, на котором он завершил проверку
    return item.includes('что ищем');
});

const out_2 = где_ищем.every(function (item) {     // every вернёт true если все элементы прошли проверку
    return item.indexOf('доля правды') > -1;
  });


// ____Сложение значений из массива, не используя цикл
    
const euros = [23, 23.5, 63.32, 45];
const sum = euros.reduce((total, amount) => total + amount);   // главное отличие, первый аргумент сожердит результат колбека на каждой итерации
    // аналогично - const sum = euros.reduce(function(total, amount) {return total + amount;}, 0);    0 - это начальное значение
    //total содержит итоговое значение, полученное в результате всех произведенных на этот момент действий; 
    //amount — это текущий элемент массива. 

// ____ещё пример reduce

const order = ['яблоко', 'банан', 'апельсин', 'банан', 'яблоко', 'банан'];
const result = order.reduce(function (prevVal, item) {
      if (!prevVal[item]) {
        prevVal[item] = 1;      // если ключа ещё нет в объекте, значит это первое повторение
      } else {
        prevVal[item] += 1;      // иначе увеличим количество повторений на 1
      }
      return prevVal;           // и вернём изменённый объект
    }, {});             // Начальное значение — пустой объект.
    
console.log(result); // { яблоко: 2, банан: 3, апельсин: 1 }

// ___ Поверхностное копироване массива

const newArr = Object.assign([], arr);
// или
const nerArr = arr.slice();


array_one.sort()        // сортировка массива. Без параметров сортирует как строки по символам в Unicode

Object.keys({ name: 'Алан', surname: 'Кей' });          // Вернёт массив клюей объекта


//ECMAScript 2017 появилось два новых метода для работы с объектами. Возвращаются массивы
Object.entries  // все пары «ключ-значение
Object.values   // возвращает значения всех свойств и методов объекта


//_______________________________________________________________

fun = () => {
    throw new Error('кастомная ошибка');
    // Пример о том что если эта функция реализована в классе,
    // а вызвать её в наследнике, то в консоле будет это сообщение
}


class GG {
    consructor(s, g) {
        doc.addEventListener('submit', this.fun);
    }

    fun(e) {
        e.preventDefault();
        const data = Object.fromEntries(new FormData(e.target));        //  
        this.g(data);   //  функция колбэк, которой отправляются данные из формф в виде объекта
    }
}
