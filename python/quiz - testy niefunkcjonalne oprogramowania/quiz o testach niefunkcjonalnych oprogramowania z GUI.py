import tkinter as tk

# Mapowanie indeksu na literę opcji
option_letters = ["A", "B", "C", "D"]

# Lista 15 pytań – (treść pytania, lista opcji, indeks poprawnej odpowiedzi, wyjaśnienie)
questions = [
    (
        "Które z poniższych kryteriów najlepiej odzwierciedla skuteczność testów wydajnościowych w warunkach rzeczywistych?",
        [
            "Minimalizacja średniego czasu odpowiedzi przy niskim obciążeniu",
            "Zdolność systemu do utrzymania wysokiej wydajności podczas szczytowego obciążenia przez dłuższy okres",
            "Maksymalne wykorzystanie zasobów sprzętowych bez względu na koszty",
            "Liczba błędów wykrytych przy pomocy testów"
        ],
        1,
        "Rzeczywiste warunki użytkowania systemu często charakteryzują się długotrwałymi okresami wysokiego obciążenia, "
        "szczególnie podczas godzin szczytu lub ważnych wydarzeń. System, który utrzymuje stabilną wydajność, sprawdzi "
        "się najlepiej, a pozostałe opcje dotyczą tylko pojedynczych aspektów wydajności."
    ),
    (
        "W testowaniu bezpieczeństwa, który aspekt jest najtrudniejszy do zautomatyzowania i wymaga największego zaangażowania człowieka?",
        [
            "Skanowanie portów i wykrywanie otwartych usług",
            "Weryfikacja konfiguracji zabezpieczeń systemowych",
            "Testy socjotechniczne, czyli próby manipulacji ludzkimi zachowaniami",
            "Analiza logiki biznesowej pod kątem potencjalnych luk w zabezpieczeniach"
        ],
        3,
        "Analiza logiki biznesowej wymaga głębokiego zrozumienia procesów oraz przewidywania nietypowych ścieżek "
        "wykorzystania systemu, co jest zadaniem dla ludzkiego eksperta."
    ),
    (
        "Który scenariusz najlepiej oddaje ideę „testowania degradowalności” systemu?",
        [
            "Ocena, czy system potrafi odzyskać pełną funkcjonalność po awarii",
            "Testowanie zachowania systemu przy nagłym wzroście liczby użytkowników",
            "Analiza utrzymania minimalnej funkcjonalności przy stopniowym ograniczaniu zasobów (np. pamięci, przepustowości)",
            "Pomiar szybkości odpowiedzi systemu przy maksymalnym obciążeniu"
        ],
        2,
        "Testowanie degradowalności sprawdza, czy system potrafi zachować podstawową funkcjonalność nawet przy "
        "ograniczonych zasobach, co jest kluczowe w sytuacjach awaryjnych."
    ),
    (
        "W kontekście testów użyteczności, które narzędzie/metoda dostarcza najbardziej wiarygodnych danych o rzeczywistym zachowaniu użytkowników?",
        [
            "Ankiety online po zakończeniu korzystania z aplikacji",
            "Testy A/B z rejestrowaniem interakcji użytkowników",
            "Testy moderowane z rzeczywistymi użytkownikami, obserwowane na żywo",
            "Wywiady indywidualne z grupą docelową"
        ],
        1,
        "Testy A/B rejestrują rzeczywiste interakcje użytkowników w naturalnych warunkach, co daje obiektywne dane, "
        "w przeciwieństwie do metod opartych tylko na subiektywnych opiniach."
    ),
    (
        "Który z poniższych parametrów jest kluczowy przy testach dostępności (accessibility testing)?",
        [
            "Szybkość ładowania strony lub aplikacji",
            "Zgodność z wytycznymi WCAG oraz normami dla osób niepełnosprawnych",
            "Responsywność interfejsu przy różnych rozdzielczościach ekranu",
            "Liczba dostępnych funkcji poprawiających komfort użytkowania"
        ],
        1,
        "Wytyczne WCAG stanowią międzynarodowy standard dostępności, co gwarantuje, że treści będą dostępne dla osób "
        "z różnymi niepełnosprawnościami."
    ),
    (
        "Które podejście najlepiej opisuje strategię „testowania ryzyka” w obszarze testów niefunkcjonalnych?",
        [
            "Testowanie wszystkich komponentów systemu w równym stopniu",
            "Skupienie się na krytycznych komponentach, które w razie awarii mają największy wpływ na użytkownika i biznes",
            "Przeprowadzanie testów tylko po wystąpieniu problemu w środowisku produkcyjnym",
            "Zastosowanie wyłącznie automatycznych narzędzi do kompleksowego testowania"
        ],
        1,
        "Testowanie oparte na ryzyku polega na priorytetyzacji testów na kluczowych komponentach, co pozwala skupić "
        "zasoby na najważniejszych obszarach."
    ),
    (
        "Która z poniższych metod testowania bezpieczeństwa opiera się na wysyłaniu losowych, nieprzewidywalnych danych w celu wykrycia nieoczekiwanych błędów?",
        [
            "Testy penetracyjne",
            "Testy regresyjne sprawdzające stabilność systemu po zmianach",
            "Analiza statyczna kodu źródłowego",
            "Testy fuzzingowe"
        ],
        3,
        "Fuzzing polega na wprowadzaniu losowych lub nieprawidłowych danych wejściowych do systemu, aby wykryć błędy "
        "lub luki, co jest trudne do osiągnięcia innymi metodami."
    ),
    (
        "Jak najlepiej zdefiniować pojęcie „latent defects” (ukryte defekty) w kontekście testów niefunkcjonalnych?",
        [
            "Błędy ujawniane wyłącznie podczas testów wydajnościowych",
            "Usterki obecne w interfejsie użytkownika, które są łatwe do przeoczenia",
            "Wady systemu ujawniające się dopiero przy specyficznych, rzadkich warunkach operacyjnych",
            "Błędy wykrywane natychmiast po wdrożeniu systemu"
        ],
        2,
        "Ukryte defekty to błędy, które nie są widoczne w standardowych testach, lecz ujawniają się w specyficznych, "
        "często ekstremalnych warunkach pracy systemu."
    ),
    (
        "Jaką rolę odgrywają testy niefunkcjonalne w kontekście Continuous Integration/Continuous Deployment (CI/CD)?",
        [
            "Są zbędne, ponieważ CI/CD skupia się wyłącznie na testach funkcjonalnych",
            "Umożliwiają szybkie wykrycie regresji wydajnościowych, problemów z kompatybilnością i innych aspektów, zanim zmiany trafią na produkcję",
            "Zastępują konieczność przeprowadzania testów jednostkowych i integracyjnych",
            "Są przydatne tylko w końcowej fazie testowania, tuż przed wdrożeniem"
        ],
        1,
        "Testy niefunkcjonalne w CI/CD działają jako linia obrony – wykrywają problemy zanim zmiany trafią do "
        "środowiska produkcyjnego, co chroni doświadczenie użytkowników."
    ),
    (
        "Testy użyteczności (Usability Testing) skupiają się głównie na:",
        [
            "Sprawdzeniu, czy aplikacja działa na urządzeniach mobilnych",
            "Ocenie, jak szybko użytkownik wykonuje kluczowe zadania",
            "Wykrywaniu błędów w logice biznesowej",
            "Analizie zgodności z normą ISO 9241"
        ],
        1,
        "Testy użyteczności mierzą efektywność i szybkość, z jaką użytkownicy wykonują zadania, co pomaga ocenić "
        "intuicyjność i ergonomię interfejsu."
    ),
    (
        "Który test sprawdza, czy system odzyskuje sprawność w czasie krótszym niż 5 minut po awarii zasilania?",
        [
            "Testy wytrzymałościowe (Endurance Testing)",
            "Testy odpornościowe (Resilience Testing)",
            "Testy odzyskiwania (Recovery Testing)",
            "Testy ciągłości działania (Disaster Recovery Testing)"
        ],
        2,
        "Testy odzyskiwania (Recovery Testing) weryfikują, czy system potrafi szybko przywrócić działanie po awarii, "
        "np. utracie zasilania."
    ),
    (
        "Co jest głównym celem testów 'Chaos Inżynieryjnego' (Chaos Monkey)?",
        [
            "Symulacja awarii zasilania w centrum danych",
            "Wprowadzanie losowych awarii, aby wymusić projektowanie systemu pod kątem odporności",
            "Testowanie maksymalnego obciążenia bazy danych",
            "Wykrywanie luk w zabezpieczeniach API"
        ],
        1,
        "Testy Chaos Inżynieryjnego, takie jak Chaos Monkey, celowo wprowadzają losowe awarie, aby wymusić projektowanie "
        "systemu odpornego na błędy i awarie."
    ),
    (
        "Co to jest 'baseline' w kontekście testów wydajnościowych?",
        [
            "Minimalny akceptowalny poziom wydajności systemu",
            "Punkt odniesienia do porównania wyników przyszłych testów",
            "Linia bazowa kodu źródłowego poddawana testom",
            "Podstawowy scenariusz testowy"
        ],
        1,
        "Baseline to ustalony punkt odniesienia, na podstawie którego porównywane są kolejne wyniki testów, "
        "umożliwiając wykrycie regresji wydajnościowych."
    ),
    (
        "Co oznacza termin 'Time to First Byte' (TTFB) w kontekście testów wydajnościowych?",
        [
            "Czas od wysłania żądania do otrzymania pierwszego bajtu odpowiedzi",
            "Czas do pierwszego uruchomienia aplikacji",
            "Czas do pierwszego błędu w systemie",
            "Czas pierwszej interakcji użytkownika z systemem"
        ],
        0,
        "TTFB to metryka określająca czas, jaki upływa od wysłania żądania do momentu otrzymania pierwszego bajtu "
        "odpowiedzi, co jest kluczowe dla oceny responsywności serwera."
    ),
    (
        "Co jest głównym celem testów obciążeniowych (load testing)?",
        [
            "Sprawdzenie, jak system zachowuje się przy maksymalnym przewidywanym obciążeniu",
            "Określenie punktu załamania systemu",
            "Testowanie odporności systemu na ataki",
            "Sprawdzenie czasu odpowiedzi dla pojedynczego użytkownika"
        ],
        0,
        "Testy obciążeniowe mają na celu sprawdzenie, czy system wytrzymuje maksymalne przewidywane obciążenie i spełnia "
        "wymagania wydajnościowe przed wdrożeniem na produkcję."
    )
]

# Tekst powitalny
intro_text = (
    "Witam w quizie o testach niefunkcjonalnych!\n"
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
root.title("Quiz o Testach Niefunkcjonalnych")
root.geometry("640x600")

intro_label = tk.Label(root, text=intro_text, wraplength=600, justify="center", font=("Arial", 16))
intro_label.pack(pady=(60, 40))

start_button = tk.Button(root, text="Rozpocznij Quiz", command=start_quiz, font=("Arial", 16), height=2, width=20)
start_button.pack()

question_number_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
question_label = tk.Label(root, text="", wraplength=600, justify="center", font=("Arial", 18))

option_buttons = [tk.Button(root, text="", width=60, height=3, font=("Arial", 14)) for _ in range(4)]

root.mainloop()
