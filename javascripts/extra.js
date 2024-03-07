document$.subscribe(function () {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function (table) {
        new Tablesort(table)
    })
})

let correct = [
    "Absolut korrekt! 👍",
    "Richtig geraten! 🎉",
    "Das ist die richtige Antwort! ✔️",
    "Gut gemacht, das ist korrekt! 🏆",
    "Exzellent, das ist richtig! 🌟",
    "Genau, das ist die richtige Antwort! 👏",
    "Du hast recht! 🎯",
    "Stimmt genau! 🥇",
    "Das ist die korrekte Antwort! 🎈",
    "Richtig, gut gemacht! 🏅",
    "Vollkommen richtig! 🎊",
    "Ja, das ist es! 🥳",
    "Perfekt, das ist richtig! 💯",
    "Bravo, das ist korrekt! 🙌",
    "Das hast du richtig erkannt! 🕵️‍♀️",
    "Das ist ein Volltreffer! 🎯",
    "Du hast es geschafft, das ist richtig! 🚀",
    "Das ist einwandfrei richtig! ✅",
    "Richtig, du bist ein Genie! 🧠",
    "Das ist die Antwort, gut gemacht! 📚",
    "Richtig, du hast es erfasst! 🧐",
    "Das ist korrekt, gut erkannt! 👀",
    "Ja, das ist die Antwort! 📝",
    "Das ist richtig, gut gemacht! 👌",
    "Richtig, du hast es getroffen! 🎯",
    "Das ist richtig, gut geraten! 🎲",
    "Richtig, du hast es herausgefunden! 🔍",
    "Das ist korrekt, gut gemacht! 👏",
    "Richtig, du hast es verstanden! 💡",
    "Das ist die richtige Antwort, gut gemacht! 🏁"
]
let lastid = 0;


function checkAnswer(inputElement, right) {

    inputElement.parentElement.parentElement.parentElement.querySelectorAll('.incorrect').forEach(function (input) {
        input.classList.remove('incorrect');
    });
    inputElement.parentElement.parentElement.parentElement.querySelectorAll('.correct').forEach(function (input) {
        if (!input.querySelector("input").checked) {
            console.log(input)
            input.classList.remove('correct');
        }

    });
    if (inputElement.checked) {
        if (right) {
            inputElement.parentElement.classList.add('correct');
        } else {
            inputElement.parentElement.classList.add('incorrect');
        }
    } else {
        inputElement.parentElement.classList.remove('incorrect');
        inputElement.parentElement.classList.remove('correct');
    }


    inputElement.parentElement.querySelectorAll('.explanation').forEach(function (input) {
        input.style.display = 'block';
    });

    let correctItems = inputElement.parentElement.parentElement.parentElement.querySelectorAll('.true')
    let incorrectItems = inputElement.parentElement.parentElement.parentElement.querySelectorAll('.false')
    let allRight = true;
    correctItems.forEach(function (input) {
        if (!input.checked) {
            allRight = false;
        }
    });
    incorrectItems.forEach(function (input) {
        if (input.checked) {
            allRight = false;
        }
    });
    let allRightElement = inputElement.parentElement.parentElement.parentElement.parentElement.querySelector('.all-right');
    if (allRight) {
        if (allRightElement.style.display === 'block') {
            return;
        }

        let id = Math.floor(Math.random() * correct.length);
        while (id === lastid) {
            id = Math.floor(Math.random() * correct.length);
        }

        allRightElement.innerHTML = correct[id];
        allRightElement.style.display = 'block';
        allRightElement.classList.add('animate__bounceIn');


    }
    else {
        allRightElement.style.display = 'none';
        allRightElement.classList.remove('animate__bounceIn');
    }
}

