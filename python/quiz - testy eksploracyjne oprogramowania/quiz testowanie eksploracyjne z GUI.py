import tkinter as tk

# Mapowanie indeksu na literę opcji
option_letters = ["A", "B", "C", "D"]

# Lista 15 pytań dotyczących testowania eksploracyjnego
questions = [
    (
        "Czym jest testowanie eksploracyjne?",
        [
            "Rodzaj testowania opartego na skryptach",
            "Nieskryptowane testowanie oparte na wiedzy testera",
            "Testowanie z użyciem automatycznych narzędzi",
            "Proces planowania testów"
        ],
        1,
        "Testowanie eksploracyjne polega na spontanicznej eksploracji aplikacji, wykorzystując doświadczenie i intuicję testera, a nie sztywne skrypty."
    ),
    (
        "Jaki jest główny cel testowania eksploracyjnego?",
        [
            "Znalezienie jak największej liczby błędów w krótkim czasie",
            "Weryfikacja zgodności z dokumentacją",
            "Przetestowanie wszystkich możliwych scenariuszy",
            "Automatyzacja testów regresyjnych"
        ],
        0,
        "Głównym celem testowania eksploracyjnego jest szybkie wykrywanie krytycznych błędów, co jest szczególnie przydatne, gdy dokumentacja jest niepełna lub zmienna."
    ),
    (
        "Co stanowi największe wyzwanie w testach eksploracyjnych?",
        [
            "Brak potrzeby dokumentacji",
            "Konieczność ciągłego dostosowywania się do nowych informacji i zmieniającego się kontekstu",
            "Zbyt duża liczba testerów",
            "Łatwość automatyzacji"
        ],
        1,
        "Testowanie eksploracyjne wymaga ciągłej adaptacji do zmieniających się warunków, co stanowi główne wyzwanie dla testera."
    ),
    (
        "Które narzędzie jest najczęściej używane do testów eksploracyjnych?",
        [
            "JIRA",
            "Selenium",
            "TestRail",
            "Nie wymaga specjalnych narzędzi"
        ],
        3,
        "Testowanie eksploracyjne opiera się przede wszystkim na umiejętnościach testera, dlatego nie korzysta z dedykowanych narzędzi."
    ),
    (
        "Które z poniższych NIE jest zaletą testowania eksploracyjnego?",
        [
            "Szybkie wykrywanie błędów",
            "Elastyczność w podejściu",
            "Dokładna powtarzalność testów",
            "Brak konieczności skryptów testowych"
        ],
        2,
        "Testowanie eksploracyjne, przez swój spontaniczny charakter, nie gwarantuje powtarzalności wyników – to właśnie ta cecha jest jego wadą."
    ),
    (
        "Czy testowanie eksploracyjne wymaga dokumentacji?",
        [
            "Tak, takiej samej jak testy skryptowane",
            "Nie, dokumentacja nie jest konieczna",
            "Może być ograniczona do notatek",
            "Wymaga pełnej specyfikacji testów"
        ],
        2,
        "W testowaniu eksploracyjnym dokumentacja zazwyczaj przybiera formę luźnych notatek, co wystarcza do rejestracji odkrytych błędów."
    ),
    (
        "Jakie umiejętności są najważniejsze dla testera eksploracyjnego?",
        [
            "Znajomość narzędzi automatyzujących",
            "Szybkość klikania",
            "Kreatywność i analityczne myślenie",
            "Umiejętność pisania skryptów testowych"
        ],
        2,
        "Kluczowe są umiejętności kreatywnego myślenia i analizy, które pozwalają testerowi na efektywne wykrywanie błędów."
    ),
    (
        "Kiedy najlepiej stosować testy eksploracyjne?",
        [
            "Na początku projektu",
            "Po zakończeniu wszystkich testów skryptowanych",
            "W dowolnym momencie",
            "Tylko gdy nie ma dokumentacji"
        ],
        2,
        "Testy eksploracyjne można przeprowadzać na różnych etapach projektu, uzupełniając inne metody testowania."
    ),
    (
        "Czy testowanie eksploracyjne można automatyzować?",
        [
            "Tak, w pełni",
            "Nie, nie można automatyzować",
            "Można częściowo wspomagać narzędziami",
            "Automatyzacja jest kluczowym elementem"
        ],
        2,
        "Choć testowanie eksploracyjne jest przede wszystkim manualne, istnieją narzędzia wspierające dokumentację i analizę wyników."
    ),
    (
        "Jakie raportowanie stosuje się w testach eksploracyjnych?",
        [
            "Szczegółowe raporty zgodne z normą IEEE",
            "Brak raportowania",
            "Notatki i checklisty",
            "Tylko logi systemowe"
        ],
        2,
        "Raportowanie w testach eksploracyjnych opiera się głównie na nieformalnych notatkach i checklistach, co odzwierciedla ich spontaniczny charakter."
    ),
    (
        "Jakie są główne techniki testowania eksploracyjnego?",
        [
            "Sesyjne testowanie eksploracyjne",
            "Testowanie z użyciem skryptów",
            "Testowanie regresyjne",
            "Testowanie obciążeniowe"
        ],
        0,
        "Sesyjne testowanie eksploracyjne pozwala na zorganizowaną eksplorację systemu w określonych przedziałach czasowych, ułatwiając dokumentację wyników."
    ),
    (
        "Jakie jest główne zastosowanie testowania eksploracyjnego?",
        [
            "Testowanie nowych funkcji",
            "Testowanie wydajności",
            "Testowanie zgodności z dokumentacją",
            "Testowanie bezpieczeństwa"
        ],
        0,
        "Testowanie eksploracyjne jest szczególnie przydatne przy wprowadzaniu nowych funkcji, gdyż pozwala szybko wykryć krytyczne błędy."
    ),
    (
        "Kto najczęściej przeprowadza testy eksploracyjne?",
        [
            "Tylko testerzy manualni",
            "Tylko programiści",
            "Zarówno testerzy, jak i programiści",
            "Nikt, testy eksploracyjne są zbędne"
        ],
        2,
        "Testy eksploracyjne są przeprowadzane zarówno przez testerów, jak i programistów, co pozwala uzyskać różne perspektywy na działanie systemu."
    ),
    (
        "Czy testowanie eksploracyjne jest częścią testowania manualnego?",
        [
            "Tak",
            "Nie",
            "Zależy od projektu",
            "Nie ma związku z testowaniem manualnym"
        ],
        0,
        "Testowanie eksploracyjne to forma testowania manualnego, oparta na intuicji i doświadczeniu testera."
    ),
    (
        "Jakie narzędzia mogą wspomagać testowanie eksploracyjne?",
        [
            "Mind mapping tools",
            "Narzędzia do automatyzacji testów",
            "Systemy do CI/CD",
            "Żadne, testowanie eksploracyjne nie używa narzędzi"
        ],
        0,
        "Narzędzia do mind mappingu mogą pomóc w organizacji myśli i dokumentacji przebiegu testów eksploracyjnych, mimo że sam proces jest głównie manualny."
    )
]

# Tekst powitalny
intro_text = (
    "Witam w quizie o testowaniu eksploracyjnym!\n"
    "Odpowiedz na pytania, wybierając jedną z opcji.\n"
    "Powodzenia!"
)

def custom_showinfo(title, message):
    """
    Wyświetla komunikat w oknie Toplevel z dynamicznym rozmiarem dostosowanym do treści.
    Zawartość komunikatu umieszczana jest w polu Text z paskiem przewijania (scrollbar),
    dzięki czemu dłuższy tekst nie wywołuje błędów związanych z rozmiarem okna.
    """
    top = tk.Toplevel(root)
    top.title(title)
    
    # Ramka na zawartość
    frame = tk.Frame(top)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Pole tekstowe z możliwością przewijania
    text_widget = tk.Text(frame, wrap="word", font=("Arial", 14), width=60, height=10)
    text_widget.insert("1.0", message)
    text_widget.config(state="disabled")  # Tylko do odczytu
    
    scrollbar_y = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)
    text_widget.pack(side="left", fill="both", expand=True)
    
    # Przycisk OK
    ok_button = tk.Button(top, text="OK", font=("Arial", 14), command=top.destroy)
    ok_button.pack(pady=(0, 20))
    
    # Obliczenie rozmiaru okna
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Ustawienie okna na ~60% szerokości i 50% wysokości ekranu
    width = int(screen_width * 0.6)
    height = int(screen_height * 0.5)
    
    # Wyśrodkowanie
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    top.geometry(f"{width}x{height}+{x}+{y}")
    
    # Pozwolenie na zmianę rozmiaru przez użytkownika
    top.resizable(True, True)
    
    # Zablokowanie interakcji z głównym oknem
    top.grab_set()
    root.wait_window(top)

def start_quiz():
    global score, question_index
    score = 0
    question_index = 0
    intro_label.pack_forget()
    start_button.pack_forget()
    question_number_label.pack(pady=10)
    question_label.pack(pady=20)
    for btn in option_buttons:
        btn.pack(pady=10)
    next_question()

def next_question():
    global question_index
    if question_index < len(questions):
        question, options, correct, explanation = questions[question_index]
        question_number_label.config(text=f"Pytanie nr {question_index + 1}")
        question_label.config(text=question)
        for i, btn in enumerate(option_buttons):
            btn.config(
                text=options[i],
                command=lambda i=i: check_answer(i),
                wraplength=600,
                height=3,
                font=("Arial", 14)
            )
    else:
        custom_showinfo(
            "Koniec quizu",
            f"Twój wynik: {score}/{len(questions)}\nDziękuję za udział w teście!"
        )
        root.quit()

def check_answer(selected):
    global score, question_index
    question, options, correct, explanation = questions[question_index]
    if selected == correct:
        custom_showinfo("Odpowiedź", "Poprawna odpowiedź!")
        score += 1
    else:
        correct_letter = option_letters[correct]
        custom_showinfo(
            "Odpowiedź",
            f"Niepoprawna odpowiedź. Odpowiedź prawidłowa to: {correct_letter}. {explanation}"
        )
    question_index += 1
    next_question()

# Tworzenie GUI
root = tk.Tk()
root.title("Quiz o Testowaniu Eksploracyjnym")
root.geometry("640x600")

intro_label = tk.Label(root, text=intro_text, wraplength=600, justify="center", font=("Arial", 16))
intro_label.pack(pady=(60, 40))

start_button = tk.Button(root, text="Rozpocznij Quiz", command=start_quiz, font=("Arial", 16), height=2, width=20)
start_button.pack()

question_number_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
question_label = tk.Label(root, text="", wraplength=600, justify="center", font=("Arial", 18))

option_buttons = [tk.Button(root, text="", width=60, height=3, font=("Arial", 14)) for _ in range(4)]

root.mainloop()
