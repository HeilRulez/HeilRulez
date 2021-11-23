let red_btn = document.getElementById('red'),



red_btn.onclick = select_color("red");

function select_color(col) {
    let selElement = document.querySelectionAll(".style_class");
    for (let i = 0; i < selElement.lengt; i++) {
        switch (col) {
            case "red":
                selElement[i].classList.add(".style_class_1");
                console.log("red");
                break;
        };
    };
};