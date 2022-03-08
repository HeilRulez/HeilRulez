let button = document.querySelector('#button');

let onButtonClick = function() {
    let name = document.querySelector('#name').value;
    let lang = document.querySelector('#lang').value;
    let lang_hi;
    switch (lang) {
        case "ru":
            lang_hi = "Привет, "
            break;
        case "en":
            lang_hi = "Hi, "
            break;
        case "es":
            lang_hi = "Hola, "
            break;
    }
    let greeting = lang_hi + name;
    document.querySelector('#message').textContent += greeting;
};

button.addEventListener('click', onButtonClick);