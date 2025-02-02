import tkinter as tk
from tkinter import messagebox

# Lista pytań i odpowiedzi
questions = [
    ("Czym jest testowanie eksploracyjne?", 
     ["Rodzaj testowania opartego na skryptach", 
      "Nieskryptowane testowanie oparte na wiedzy testera", 
      "Testowanie z użyciem automatycznych narzędzi", 
      "Proces planowania testów"], 
     1),
    ("Jaki jest główny cel testowania eksploracyjnego?", 
     ["Znalezienie jak największej liczby błędów w krótkim czasie", 
      "Weryfikacja zgodności z dokumentacją", 
      "Przetestowanie wszystkich możliwych scenariuszy", 
      "Automatyzacja testów regresyjnych"], 
     0),
    ("Co stanowi największe wyzwanie w testach eksploracyjnych?", 
     ["Brak potrzeby dokumentacji", 
      "Konieczność ciągłego dostosowywania się do nowych informacji i zmieniającego się kontekstu", 
      "Zbyt duża liczba testerów", 
      "Łatwość automatyzacji"], 
     1),
    ("Które narzędzie jest najczęściej używane do testów eksploracyjnych?", 
     ["JIRA", "Selenium", "TestRail", "Nie wymaga specjalnych narzędzi"], 
     3),
    ("Które z poniższych NIE jest zaletą testowania eksploracyjnego?", 
     ["Szybkie wykrywanie błędów", 
      "Elastyczność w podejściu", 
      "Dokładna powtarzalność testów", 
      "Brak konieczności skryptów testowych"], 
     2),
    ("Czy testowanie eksploracyjne wymaga dokumentacji?", 
     ["Tak, takiej samej jak testy skryptowane", "Nie, dokumentacja nie jest konieczna", "Może być ograniczona do notatek", "Wymaga pełnej specyfikacji testów"], 
     2),
    ("Jakie umiejętności są najważniejsze dla testera eksploracyjnego?", 
     ["Znajomość narzędzi automatyzujących", "Szybkość klikania", "Kreatywność i analityczne myślenie", "Umiejętność pisania skryptów testowych"], 
     2),
    ("Kiedy najlepiej stosować testy eksploracyjne?", 
     ["Na początku projektu", "Po zakończeniu wszystkich testów skryptowanych", "W dowolnym momencie", "Tylko gdy nie ma dokumentacji"], 
     2),
    ("Czy testowanie eksploracyjne można automatyzować?", 
     ["Tak, w pełni", "Nie, nie można automatyzować", "Można częściowo wspomagać narzędziami", "Automatyzacja jest kluczowym elementem"], 
     2),
    ("Jakie raportowanie stosuje się w testach eksploracyjnych?", 
     ["Szczegółowe raporty zgodne z normą IEEE", "Brak raportowania", "Notatki i checklisty", "Tylko logi systemowe"], 
     2),
    ("Jakie są główne techniki testowania eksploracyjnego?", 
     ["Sesyjne testowanie eksploracyjne", "Testowanie z użyciem skryptów", "Testowanie regresyjne", "Testowanie obciążeniowe"], 
     0),
    ("Jakie jest główne zastosowanie testowania eksploracyjnego?", 
     ["Testowanie nowych funkcji", "Testowanie wydajności", "Testowanie zgodności z dokumentacją", "Testowanie bezpieczeństwa"], 
     0),
    ("Kto najczęściej przeprowadza testy eksploracyjne?", 
     ["Tylko testerzy manualni", "Tylko programiści", "Zarówno testerzy, jak i programiści", "Nikt, testy eksploracyjne są zbędne"], 
     2),
    ("Czy testowanie eksploracyjne jest częścią testowania manualnego?", 
     ["Tak", "Nie", "Zależy od projektu", "Nie ma związku z testowaniem manualnym"], 
     0),
    ("Jakie narzędzia mogą wspomagać testowanie eksploracyjne?", 
     ["Mind mapping tools", "Narzędzia do automatyzacji testów", "Systemy do CI/CD", "Żadne, testowanie eksploracyjne nie używa narzędzi"], 
     0)
]

# Wstęp
intro_text = "Witam w quizie o testowaniu eksploracyjnym! Odpowiedz na pytania, wybierając jedną z opcji. Powodzenia!"

def start_quiz():
    global score, question_index
    score = 0
    question_index = 0
    intro_label.pack_forget()
    start_button.pack_forget()
    next_question()

def next_question():
    global question_index
    if question_index < len(questions):
        question, options, correct = questions[question_index]
        question_number_label.config(text=f"Pytanie nr {question_index + 1}")
        question_label.config(text=question)
        for i, btn in enumerate(option_buttons):
            btn.config(text=options[i], command=lambda i=i: check_answer(i), wraplength=600, height=3, font=("Arial", 14))
    else:
        messagebox.showinfo("Koniec quizu", f"Twój wynik: {score}/{len(questions)}\nDziękuję za udział w teście!")
        root.quit()

def check_answer(selected):
    global score, question_index
    correct_answer = questions[question_index][2]
    if selected == correct_answer:
        messagebox.showinfo("Odpowiedź", "Poprawna odpowiedź!")
        score += 1
    else:
        messagebox.showinfo("Odpowiedź", f"Niepoprawna odpowiedź! Prawidłowa: {questions[question_index][1][correct_answer]}")
    question_index += 1
    next_question()

# Tworzenie GUI
root = tk.Tk()
root.title("Quiz o Testowaniu Eksploracyjnym")
root.geometry("640x600")  # Zmniejszenie szerokości okna o 20%

intro_label = tk.Label(root, text=intro_text, wraplength=600, justify="center", font=("Arial", 16))
intro_label.pack(pady=20)

start_button = tk.Button(root, text="Rozpocznij Quiz", command=start_quiz, font=("Arial", 16), height=2, width=20)
start_button.pack()

question_number_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
question_number_label.pack(pady=10)

question_label = tk.Label(root, text="", wraplength=600, justify="center", font=("Arial", 18))
question_label.pack(pady=20)

option_buttons = [tk.Button(root, text="", width=60, height=3, font=("Arial", 14)) for _ in range(4)]
for btn in option_buttons:
    btn.pack(pady=10)

root.mainloop()
