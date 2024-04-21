document.addEventListener("DOMContentLoaded", function() {
    const myNotesBtn = document.getElementById("myNotesBtn");
    const groupNotesBtn = document.getElementById("groupNotesBtn");
    const personalNotes = document.querySelectorAll(".personal-note");
    const groupNotes = document.querySelectorAll(".group-note");
    const notes = document.querySelectorAll('.notes'); // Получаем все заметки
    let currentIndex = 0; // Текущий индекс заметки

    // Функция для скрытия всех личных заметок и отображения всех групповых заметок
    function showGroupNotes() {
        personalNotes.forEach(function(note) {
            note.style.display = "none";
        });
        groupNotes.forEach(function(note) {
            note.style.display = "block";
        });
        currentIndex = 0; // Сброс индекса при переключении к групповым заметкам
        showNotes(currentIndex);
        togglePrevNextButtons();
    }

    // Функция для скрытия всех групповых заметок и отображения всех личных заметок
    function showPersonalNotes() {
        personalNotes.forEach(function(note) {
            note.style.display = "block";
        });
        groupNotes.forEach(function(note) {
            note.style.display = "none";
        });
        currentIndex = 0; // Сброс индекса при переключении к личным заметкам
        showNotes(currentIndex);
        togglePrevNextButtons();
    }

    // Добавляем обработчики событий для кнопок
    myNotesBtn.addEventListener("click", function() {
        myNotesBtn.classList.add("active");
        groupNotesBtn.classList.remove("active");
        showPersonalNotes();
    });

    groupNotesBtn.addEventListener("click", function() {
        groupNotesBtn.classList.add("active");
        myNotesBtn.classList.remove("active");
        showGroupNotes();
    });

    // Функция для показа определенной заметки
    function showNotes(index, notePairs) {
        notes.forEach(function(note, i) {
            if (i === index) {
                note.style.display = 'block'; // Показываем заметку с указанным индексом
            } else {
                note.style.display = 'none'; // Скрываем остальные заметки
            }
        });
    }

    // Функция для управления доступностью кнопок прокрутки
    function togglePrevNextButtons() {
        const prevButton = document.getElementById('prevNote');
        const nextButton = document.getElementById('nextNote');

        if (notes.length <= 2) { // Если заметок меньше двух, делаем кнопки неактивными
            prevButton.disabled = true;
            nextButton.disabled = true;
        } else {
            // Проверяем, должна ли кнопка "влево" быть активной
            prevButton.disabled = currentIndex === 0;

            // Проверяем, должна ли кнопка "вправо" быть активной
            nextButton.disabled = currentIndex === notes.length - 1;
        }
    }

    // Добавляем обработчики событий для кнопок прокрутки заметок
    document.getElementById('prevNote').addEventListener('click', function() {
        const notePairs = document.querySelectorAll('.note-pair');
        if (currentIndex > 0) {
            currentIndex--;
            showNotes(currentIndex, notePairs);
            togglePrevNextButtons();
        }
    });

    document.getElementById('nextNote').addEventListener('click', function() {
        const notePairs = document.querySelectorAll('.note-pair');
        if (currentIndex < notePairs.length - 1) {
            currentIndex++;
            showNotes(currentIndex, notePairs);
            togglePrevNextButtons();
        }
    });

    // По умолчанию показываем личные заметки
    showPersonalNotes();
});
