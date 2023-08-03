document$.subscribe(function () {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function (table) {
        new Tablesort(table)
    })
})


function checkAnswer(inputElement, right) {
    inputElement.parentElement.parentElement.parentElement.querySelectorAll('.incorrect').forEach(function (input) {
        input.classList.remove('incorrect');
    });
    if (right) {
        inputElement.parentElement.classList.add('correct');
    } else {
        inputElement.parentElement.classList.add('incorrect');
    }

    inputElement.parentElement.querySelectorAll('.explanation').forEach(function (input) {
        input.style.display = 'block';
    });
}
