import tkinter as tk
import random
from tkinter import simpledialog

# Globalne zmienne
score = 0
question_index = 0
current_questions = []  # Aktualnie wybrana lista pytań
current_quiz_type = ""  # Typ quizu ("exploratory", "nonfunctional", "regression", "accessibility", "random")

# Mapowanie indeksu na literę opcji
option_letters = ["A", "B", "C", "D"]

# Pytania do quizu testowania eksploracyjnego
questions_exploratory = [
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

# Pytania do quizu testów niefunkcjonalnych
questions_nonfunctional = [
    (
        "Które z poniższych kryteriów najlepiej odzwierciedla skuteczność testów wydajnościowych w warunkach rzeczywistych?",
        [
            "Minimalizacja średniego czasu odpowiedzi przy niskim obciążeniu",
            "Zdolność systemu do utrzymania wysokiej wydajności podczas szczytowego obciążenia przez dłuższy okres",
            "Maksymalne wykorzystanie zasobów sprzętowych bez względu na koszty",
            "Liczba błędów wykrytych przy pomocy testów"
        ],
        1,
        "Rzeczywiste warunki użytkowania systemu często charakteryzują się długotrwałymi okresami wysokiego obciążenia, szczególnie podczas godzin szczytu lub ważnych wydarzeń. System, który utrzymuje stabilną wydajność, sprawdzi się najlepiej, a pozostałe opcje dotyczą tylko pojedynczych aspektów wydajności."
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
        "Analiza logiki biznesowej wymaga głębokiego zrozumienia procesów oraz przewidywania nietypowych ścieżek wykorzystania systemu, co jest zadaniem dla ludzkiego eksperta."
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
        "Testowanie degradowalności sprawdza, czy system potrafi zachować podstawową funkcjonalność nawet przy ograniczonych zasobach, co jest kluczowe w sytuacjach awaryjnych."
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
        "Testy A/B rejestrują rzeczywiste interakcje użytkowników w naturalnych warunkach, co daje obiektywne dane, w przeciwieństwie do metod opartych tylko na subiektywnych opiniach."
    ),
    (
        "Który z poniższych parametrów jest kluczowy przy testach dostępności (accessibility testing)?",
        [
            "Szybkość ładowania strony lub aplikacji",
            "Zgodność z wytycznymi WCAG oraz normami dla osób z niepełnosprawnościami",
            "Szybkość przewijania strony",
            "Liczba dostępnych funkcji poprawiających komfort użytkowania"
        ],
        1,
        "Wytyczne WCAG stanowią międzynarodowy standard dostępności, co gwarantuje, że treści będą dostępne dla osób z różnymi niepełnosprawnościami."
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
        "Testowanie oparte na ryzyku polega na priorytetyzacji testów na kluczowych komponentach, co pozwala skupić zasoby na najważniejszych obszarach."
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
        "Fuzzing polega na wprowadzaniu losowych lub nieprawidłowych danych wejściowych do systemu, aby wykryć błędy lub luki, co jest trudne do osiągnięcia innymi metodami."
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
        "Ukryte defekty to błędy, które nie są widoczne w standardowych testach, lecz ujawniają się w specyficznych, często ekstremalnych warunkach pracy systemu."
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
        "Testy niefunkcjonalne w CI/CD działają jako linia obrony – wykrywają problemy zanim zmiany trafią do środowiska produkcyjnego, co chroni doświadczenie użytkowników."
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
        "Testy użyteczności mierzą efektywność i szybkość, z jaką użytkownicy wykonują zadania, co pomaga ocenić intuicyjność i ergonomię interfejsu."
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
        "Testy odzyskiwania (Recovery Testing) weryfikują, czy system potrafi szybko przywrócić działanie po awarii, np. utracie zasilania."
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
        "Testy Chaos Inżynieryjnego, takie jak Chaos Monkey, celowo wprowadzają losowe awarie, aby wymusić projektowanie systemu odpornego na błędy i awarie."
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
        "Baseline to ustalony punkt odniesienia, na podstawie którego porównywane są kolejne wyniki testów, umożliwiając wykrycie regresji wydajnościowych."
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
        "TTFB to metryka określająca czas, jaki upływa od wysłania żądania do momentu otrzymania pierwszego bajtu odpowiedzi, co jest kluczowe dla oceny responsywności serwera."
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
        "Testy obciążeniowe mają na celu sprawdzenie, czy system wytrzymuje maksymalne przewidywane obciążenie i spełnia wymagania wydajnościowe przed wdrożeniem na produkcję."
    )
]

# Pytania do quizu testów regresyjnych
questions_regression = [
    (
        "Co jest najgłębszym celem testów regresyjnych w kontekście DevOps?",
        [
            "Zapewnienie zgodności z nowymi standardami bezpieczeństwa",
            "Minimalizacja ryzyka niezamierzonych skutków ubocznych zmian w kodzie",
            "Przyspieszenie procesu wdrażania nowych funkcji",
            "Eliminacja konieczności testów manualnych"
        ],
        1,
        "Testy regresyjne mają za zadanie upewnić się, że nowe zmiany nie wprowadzają niezamierzonych skutków ubocznych, co jest kluczowe w środowisku CI/CD."
    ),
    (
        "Mimo 90% pokrycia kodu, nadal występują błędy regresyjne. Dlaczego?",
        [
            "10% niepokrytego kodu zawiera krytyczne ścieżki",
            "Wysoki poziom pokrycia kodu nie gwarantuje wykrycia wszystkich możliwych interakcji i stanów systemu",
            "Testy są źle zaprojektowane, mimo że pokrywają kod",
            "System zawiera elementy, których nie da się przetestować automatycznie"
        ],
        1,
        "Pokrycie kodu mierzy tylko procent wykonania, nie obejmując wszystkich kombinacji danych i stanów systemu."
    ),
    (
        "Prawdziwe stwierdzenie o testach regresyjnych opartych na modelach:",
        [
            "Modele są używane wyłącznie do wizualizacji przypadków testowych",
            "Podejście oparte na modelach eliminuje potrzebę pisania konkretnych przypadków testowych",
            "Modele pozwalają na generowanie przypadków testowych na podstawie formalnej specyfikacji systemu, co zwiększa skuteczność wykrywania regresji",
            "Testy oparte na modelach działają wyłącznie dla systemów zaprojektowanych zgodnie z architekturą sterowaną modelami"
        ],
        2,
        "Model-based testing wykorzystuje formalne modele do automatycznego generowania przypadków testowych, co pozwala objąć różne ścieżki wykonania systemu."
    ),
    (
        "Która praktyka zwiększa ryzyko pominięcia regresji?",
        [
            "Testowanie oparte na mapie ryzyka",
            "Ciągła integracja z automatycznymi testami",
            "Brak aktualizacji przypadków testowych po zmianie wymagań",
            "Selektywna regresja z analizą wpływu"
        ],
        2,
        "Nieaktualne przypadki testowe nie odzwierciedlają bieżącej sytuacji w systemie, przez co mogą nie wykryć regresji."
    ),
    (
        "Który typ regresji nie istnieje w klasyfikacji testów?",
        [
            "Regresja progresywna",
            "Regresja częściowa (partial)",
            "Regresja pełna (full)",
            "Regresja niema (silent)"
        ],
        0,
        "Termin 'regresja progresywna' nie występuje w standardowej klasyfikacji regresji testowych."
    ),
    (
        "Które kryterium jest najmniej istotne przy priorytetyzacji przypadków testowych w regresji?",
        [
            "Częstotliwość użycia funkcji przez użytkowników",
            "Złożoność techniczna modułu",
            "Liczba wykrytych w przeszłości defektów w obszarze",
            "Estetyka interfejsu użytkownika"
        ],
        3,
        "Estetyka interfejsu nie wpływa na krytyczną funkcjonalność systemu, dlatego nie jest istotnym kryterium przy testach regresyjnych."
    ),
    (
        "Co to jest 'regresja' w kontekście testowania?",
        [
            "Nowy błąd w kodzie",
            "Powrót starego błędu po zmianach",
            "Zmniejszenie wydajności systemu",
            "Błąd w interfejsie użytkownika"
        ],
        1,
        "Regresja oznacza, że wcześniej naprawiony błąd pojawia się ponownie w wyniku wprowadzonych zmian w kodzie."
    ),
    (
        "Która technika pozwala ograniczyć zakres testów regresyjnych?",
        [
            "Testowanie eksploracyjne",
            "Analiza wpływu zmian (impact analysis)",
            "Pełne przetestowanie wszystkich modułów",
            "Testowanie czarnoskrzynkowe"
        ],
        1,
        "Analiza wpływu zmian pozwala zidentyfikować te obszary systemu, które mogły ulec zmianie, co umożliwia selektywne przeprowadzenie regresji."
    ),
    (
        "Dlaczego automatyzacja jest ważna w testach regresyjnych?",
        [
            "Eliminuje potrzebę testowania manualnego",
            "Zmniejsza czas wykonania i zapewnia powtarzalność",
            "Gwarantuje brak błędów",
            "Jest tańsza w implementacji"
        ],
        1,
        "Automatyzacja umożliwia szybkie uruchamianie testów, co jest kluczowe w środowiskach CI/CD, choć nie zastępuje całkowicie testów manualnych."
    ),
    (
        "Różnica między 'sanity check' a 'smoke test':",
        [
            "Sanity check weryfikuje kluczowe funkcje po zmianach, smoke test – minimalną stabilność całego systemu przed akceptacją buildu do dalszych testów",
            "Sanity check koncentruje się na poprawności logiki biznesowej, a smoke test na podstawowej funkcjonalności technicznej",
            "Smoke test to szerszy zestaw przypadków testowych, a sanity check to ich podzbiór",
            "Sanity check weryfikuje spójność wewnętrzną, smoke test bada interakcje między komponentami"
        ],
        0,
        "Smoke test sprawdza podstawową stabilność systemu, natomiast sanity check weryfikuje konkretne zmiany w kodzie."
    ),
    (
        "Najczęstsze wyzwanie w testach regresyjnych:",
        [
            "Brak środowiska testowego",
            "Duży nakład czasowy na wykonanie testów",
            "Brak współpracy z developerami",
            "Niska jakość danych testowych"
        ],
        1,
        "Rosnąca liczba przypadków testowych może znacząco wydłużyć czas wykonywania regresji, co stanowi duże wyzwanie."
    ),
    (
        "Co oznacza 'selektywna regresja'?",
        [
            "Testowanie tylko nowych funkcji",
            "Testowanie wybranych obszarów dotkniętych zmianami",
            "Testowanie raz w miesiącu",
            "Ignorowanie testów jednostkowych"
        ],
        1,
        "Selektywna regresja skupia się na testowaniu jedynie tych obszarów systemu, które zostały zmienione lub są zależne od wprowadzonych zmian."
    ),
    (
        "Jakie testy są często pomijane w regresji, a mogą powodować problemy?",
        [
            "Testy integracyjne",
            "Testy związane z danymi (np. migracje)",
            "Testy jednostkowe",
            "Testy akceptacyjne"
        ],
        1,
        "Testy związane z danymi, takie jak migracje, często są pomijane, co może prowadzić do błędów w produkcji mimo wysokiego pokrycia kodu."
    ),
    (
        "Co zaleca się, gdy nie ma czasu na pełną regresję?",
        [
            "Przeprowadzić regresję tylko raz przed release’em",
            "Wykonać testy smoke i sanity, uzupełnione o testy regresyjne w obszarach o wysokim ryzyku",
            "Wdrożyć strategię testowania w warstwie, koncentrując się na testach jednostkowych i integracyjnych",
            "Przeprowadzić regresję po release’e"
        ],
        1,
        "Testy smoke i sanity pozwalają szybko zweryfikować krytyczne funkcje systemu, minimalizując ryzyko, gdy pełna regresja nie jest możliwa."
    ),
    (
        "Które zdanie jest FAŁSZYWE dotyczące testów regresyjnych?",
        [
            "Mogą być wykonywane ręcznie lub automatycznie",
            "Są potrzebne tylko w dużych projektach",
            "Wymagają aktualizacji przy zmianach w wymaganiach",
            "Często wykorzystują istniejące przypadki testowe"
        ],
        1,
        "Testy regresyjne są niezbędne w każdym projekcie, ponieważ każda zmiana kodu niesie ryzyko wprowadzenia błędów, niezależnie od skali projektu."
    )
]

# Pytania do quizu testów dostępności
questions_accessibility = [
    (
        "Co oznacza skrót WCAG w kontekście dostępności oprogramowania?",
        [
            "Web Content Accessibility Guidelines",
            "World Computer Access Group",
            "Web Control and Accessibility Gateway",
            "Web Content Analysis Guidelines"
        ],
        0,
        "WCAG to zbiór wytycznych opracowanych przez W3C, określających, jak tworzyć dostępne treści internetowe dla osób z niepełnosprawnościami."
    ),
    (
        "Który z poniższych elementów NIE jest częścią testów dostępności mobilnej?",
        [
            "Testowanie kompatybilności z czytnikami ekranu (VoiceOver, TalkBack)",
            "Sprawdzanie minimalnego rozmiaru elementów dotykalnych",
            "Testowanie responsywności na różnych rozmiarach ekranu",
            "Sprawdzanie zgodności z protokołem SMTP"
        ],
        3,
        "SMTP to protokół do przesyłania e-maili, niezwiązany z testowaniem dostępności mobilnej. Pozostałe opcje są kluczowe dla oceny dostępności."
    ),
    (
        "Co oznacza termin 'keyboard trap' w kontekście dostępności?",
        [
            "Funkcja zwiększająca bezpieczeństwo klawiatury",
            "Sytuacja, w której użytkownik nie może opuścić elementu interfejsu za pomocą klawiatury",
            "Skrót klawiaturowy blokujący dostęp do strony",
            "Mechanizm ochrony przed niepowołanym dostępem do aplikacji"
        ],
        1,
        "Keyboard trap to sytuacja, gdy użytkownik korzystający z klawiatury nie może wyjść z danego elementu interfejsu, co utrudnia nawigację osobom nieużywającym myszy."
    ),
    (
        "Co to jest 'skip navigation' (pomijanie nawigacji) w kontekście dostępności stron internetowych?",
        [
            "Technika eliminująca menu nawigacyjne z aplikacji mobilnych",
            "Link pozwalający użytkownikom klawiatury przejść bezpośrednio do głównej treści strony",
            "Funkcja, która powoduje, że czytniki ekranu pomijają menu nawigacyjne",
            "Metoda ukrywania nawigacji na urządzeniach o małych ekranach"
        ],
        1,
        "Skip navigation to technika polegająca na umieszczeniu ukrytego linku, który umożliwia pominięcie powtarzających się elementów nawigacyjnych, co ułatwia nawigację użytkownikom klawiatury."
    ),
    (
        "Co to jest 'alt text' i dlaczego jest ważny dla dostępności?",
        [
            "Tekst wyświetlany na przyciskach",
            "Opis obrazka odczytywany przez czytniki ekranu",
            "Nagłówek strony",
            "Stopka strony"
        ],
        1,
        "Alt text to opis obrazu dodawany do tagu <img>, który jest odczytywany przez czytniki ekranu, umożliwiając zrozumienie treści wizualnej przez użytkowników czytników ekranu."
    ),
    (
        "Co to jest semantyczny HTML i dlaczego jest ważny dla dostępności?",
        [
            "HTML używany do definiowania wyglądu strony",
            "HTML wykorzystujący znaczniki zgodnie z ich przeznaczeniem",
            "HTML zoptymalizowany dla wyszukiwarek internetowych",
            "HTML zawierający tylko tekst, bez elementów graficznych"
        ],
        1,
        "Semantyczny HTML polega na stosowaniu znaczników zgodnie z ich znaczeniem (np. <header>, <nav>, <main>), co ułatwia czytnikom ekranu interpretację struktury strony."
    ),
    (
        "Które z poniższych zdań najlepiej opisuje cel 'testów obciążeniowych dostępności'?",
        [
            "Sprawdzenie wydajności strony dla użytkowników z wolnym połączeniem",
            "Weryfikacja, jak technologie wspomagające radzą sobie z dużą ilością treści",
            "Testowanie wytrzymałości fizycznej urządzeń wspomagających",
            "Ten termin nie istnieje w kontekście testowania dostępności"
        ],
        3,
        "Termin 'testy obciążeniowe dostępności' nie występuje – testy obciążeniowe dotyczą wydajności systemu, a nie dostępności."
    ),
    (
        "Testujesz formularz. Co JEST zgodne z WCAG?",
        [
            "Błąd jest pokazany czerwoną ramką i tekstem 'Niepoprawne dane'",
            "Błąd jest opisany w tooltipie po najechaniu myszą",
            "Błąd jest wyświetlony w konsoli przeglądarki",
            "Błąd jest komunikowany zmianą ikony w prawym rogu ekranu"
        ],
        0,
        "Błąd powinien być komunikowany przynajmniej na dwa sposoby - np. wizualnie (np. czerwona ramka) oraz tekstowo, aby był dostępny dla wszystkich użytkowników, w tym osób korzystających z czytników ekranu."
    ),
    (
        "Co jest wymagane dla napisów (captions) na żywo zgodnie z WCAG?",
        [
            "Muszą być zatwierdzone przez prawnika",
            "Powinny być w 100% dokładne",
            "Muszą identyfikować mówców i opisywać istotne dźwięki",
            "Powinny być dostępne tylko w języku angielskim"
        ],
        2,
        "Napisy na żywo muszą identyfikować mówców oraz opisywać istotne dźwięki, aby osoby niesłyszące mogły w pełni zrozumieć przekaz audio."
    ),
    (
        "Co to jest 'screen reader'?",
        [
            "Oprogramowanie do edycji zdjęć",
            "Narzędzie odczytujące tekst na ekranie dla, np. osób niewidomych",
            "Aplikacja do nauki języków",
            "Automatyczny tester interfejsu graficznego"
        ],
        1,
        "Screen reader to oprogramowanie, które odczytuje na głos zawartość ekranu, umożliwiając, np. osobom niewidomym korzystanie z urządzeń."
    ),
    (
        "Czym są technologie asystujące?",
        [
            "Narzędzia do automatycznego testowania oprogramowania",
            "Oprogramowanie i sprzęt ułatwiające korzystanie z technologii osobom z niepełnosprawnościami",
            "Standardy projektowania interfejsów użytkownika",
            "Języki programowania do tworzenia dostępnych stron internetowych"
        ],
        1,
        "Technologie asystujące, takie jak czytniki ekranu czy lupy ekranowe, są niezbędne dla osób z niepełnosprawnościami, umożliwiając im korzystanie z komputerów i smartfonów."
    ),
    (
        "Dlaczego testowanie dostępności jest ważne?",
        [
            "Poprawia SEO",
            "Zwiększa liczbę potencjalnych użytkowników",
            "Spełnia wymagania prawne",
            "Wszystkie powyższe odpowiedzi"
        ],
        3,
        "Testowanie dostępności poprawia SEO, zwiększa potencjalną liczbę użytkowników oraz spełnia wymagania prawne, co czyni je kluczowym elementem projektowania stron."
    ),
    (
        "Co to jest 'alt text' (tekst alternatywny) w kontekście stron internetowych?",
        [
            "Tekst wyświetlany na przyciskach",
            "Opis obrazka odczytywany przez czytniki ekranu",
            "Nagłówek strony",
            "Stopka strony"
        ],
        1,
        "Alt text to opis obrazu, który umożliwia osobom korzystającym z czytników ekranu zrozumienie, co przedstawia dany obraz, a także jest wyświetlany, gdy obraz nie może zostać załadowany."
    )
]

# Tekst powitalny dla quizu testów regresyjnych
intro_text_regression = (
    "Witam w quizie o testach regresyjnych!\n"
    "Odpowiedz na pytania, wybierając jedną z opcji.\n"
    "Powodzenia!"
)

# Tekst powitalny dla quizu testów dostępności
intro_text_accessibility = (
    "Witam w quizie o testach dostępności!\n"
    "Odpowiedz na pytania, wybierając jedną z opcji.\n"
    "Powodzenia!"
)

# Funkcja wyświetlająca komunikat z dynamicznym rozmiarem okna (pole Text z paskiem przewijania)
def custom_showinfo(title, message):
    top = tk.Toplevel(root)
    top.title(title)
    
    frame = tk.Frame(top)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    formatted_message = message.replace("\n", "\n\n")
    text_widget = tk.Text(frame, wrap="word", font=("Arial", 14), width=60, height=10)
    text_widget.insert("1.0", formatted_message)
    text_widget.config(state="disabled")
    scrollbar_y = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)
    text_widget.pack(side="left", fill="both", expand=True)
    
    ok_button = tk.Button(top, text="OK", font=("Arial", 14), command=top.destroy)
    ok_button.pack(pady=(0, 20))
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.5)
    height = int(screen_height * 0.4)
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    top.geometry(f"{width}x{height}+{x}+{y}")
    top.resizable(True, True)
    
    top.grab_set()
    root.wait_window(top)

# Menu wynikowe po ukończeniu quizu
def show_result_menu():
    result_frame = tk.Frame(root, bg="white")
    result_frame.pack(expand=True)
    
    result_label = tk.Label(result_frame, text=f"Twój wynik: {score}/{len(current_questions)}", font=("Arial", 20), bg="white")
    result_label.pack(pady=20)
    
    def go_to_menu():
        result_frame.destroy()
        show_main_menu()
    
    def repeat_quiz():
        result_frame.destroy()
        start_quiz(current_quiz_type)
    
    def exit_app():
        root.quit()
    
    menu_button = tk.Button(result_frame, text="Przejdź do menu", font=("Arial", 18), command=go_to_menu)
    repeat_button = tk.Button(result_frame, text="Powtórz quiz", font=("Arial", 18), command=repeat_quiz)
    exit_button = tk.Button(result_frame, text="Wyjdź", font=("Arial", 18), command=exit_app)
    
    menu_button.pack(pady=5)
    repeat_button.pack(pady=5)
    exit_button.pack(pady=5)

# Funkcje quizu – wspólny interfejs dla wszystkich quizów
def start_quiz(quiz_type):
    global score, question_index, current_questions, current_quiz_type
    score = 0
    question_index = 0
    current_quiz_type = quiz_type

    if quiz_type == "exploratory":
        current_questions = questions_exploratory
        quiz_intro = "Witam w quizie o testowaniu eksploracyjnym!\nOdpowiedz na pytania, wybierając jedną z opcji.\nPowodzenia!"
    elif quiz_type == "nonfunctional":
        current_questions = questions_nonfunctional
        quiz_intro = "Witam w quizie o testach niefunkcjonalnych!\nOdpowiedz na pytania, wybierając jedną z opcji.\nPowodzenia!"
    elif quiz_type == "regression":
        current_questions = questions_regression
        quiz_intro = intro_text_regression
    elif quiz_type == "accessibility":
        current_questions = questions_accessibility
        quiz_intro = intro_text_accessibility
    elif quiz_type == "random":
        # Połącz wszystkie pytania
        all_questions = questions_exploratory + questions_nonfunctional + questions_regression + questions_accessibility
        # Zapytaj użytkownika o liczbę pytań
        num = simpledialog.askinteger("Losowy quiz", "Podaj liczbę pytań (od 15 do 40):", minvalue=15, maxvalue=40)
        if num is None:
            return  # Użytkownik anulował
        current_questions = random.sample(all_questions, num)
        quiz_intro = f"Losowy quiz - {num} pytań!\nPowodzenia!"

    main_menu_frame.pack_forget()
    quiz_frame.pack(expand=True)
    question_number_label.pack(pady=10)
    question_label.pack(pady=20)
    for btn in option_buttons:
        btn.pack(pady=10)
    next_question()

def next_question():
    global question_index
    if question_index < len(current_questions):
        question, options, correct, explanation = current_questions[question_index]
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
        quiz_frame.pack_forget()
        show_result_menu()

def check_answer(selected):
    global score, question_index
    question, options, correct, explanation = current_questions[question_index]
    if selected == correct:
        custom_showinfo("Odpowiedź", "Poprawna odpowiedź!")
        score += 1
    else:
        correct_letter = option_letters[correct]
        custom_showinfo("Odpowiedź", f"Niepoprawna odpowiedź. Odpowiedź prawidłowa to: {correct_letter}.\n\n{explanation}")
    question_index += 1
    next_question()

# Główne menu – nagłówek i przyciski wyboru quizu
def show_main_menu():
    main_menu_frame.pack(expand=True)

# Tworzenie GUI
root = tk.Tk()
root.title("Quizy o Testowaniu Oprogramowania")
root.geometry("640x600")
root.configure(bg="white")

# Główne menu
main_menu_frame = tk.Frame(root, bg="white")
main_menu_frame.pack(expand=True)

header_text = (
    "Witam w aplikacji zawierającej quizy o różnych rodzajach testowania oprogramowania.\n\n"
    "Każdy test zawiera po 4 możliwe odpowiedzi, z których jedna jest poprawna.\n\n"
    "Quiz losowy zawiera losowo wybrane pytania ze wszystkich dostępnych quizów.\n\n"
    "Proszę wybrać jedną z poniższych opcji, aby rozpocząć quiz:"
)
header_label = tk.Label(main_menu_frame, text=header_text, font=("Arial", 16), wraplength=600, justify="center", bg="white")
header_label.pack(pady=20)

exploratory_button = tk.Button(main_menu_frame, text="Testowanie Eksploracyjne", font=("Arial", 16),
                               command=lambda: start_quiz("exploratory"), bg="#4CAF50", fg="white")
nonfunctional_button = tk.Button(main_menu_frame, text="Testy Niefunkcjonalne", font=("Arial", 16),
                                 command=lambda: start_quiz("nonfunctional"), bg="#2196F3", fg="white")
regression_button = tk.Button(main_menu_frame, text="Testy Regresyjne", font=("Arial", 16),
                              command=lambda: start_quiz("regression"), bg="#FFC107", fg="black")
accessibility_button = tk.Button(main_menu_frame, text="Testowanie Dostępności", font=("Arial", 16),
                                 command=lambda: start_quiz("accessibility"), bg="#9C27B0", fg="white")
random_button = tk.Button(main_menu_frame, text="Quiz losowy", font=("Arial", 16),
                          command=lambda: start_quiz("random"), bg="#607D8B", fg="white")

exploratory_button.pack(pady=10)
nonfunctional_button.pack(pady=10)
regression_button.pack(pady=10)
accessibility_button.pack(pady=10)
random_button.pack(pady=10)

# Ramka quizu – wspólna dla wszystkich quizów
quiz_frame = tk.Frame(root, bg="white")
question_number_label = tk.Label(quiz_frame, text="", font=("Arial", 16, "bold"), bg="white")
question_label = tk.Label(quiz_frame, text="", wraplength=600, justify="center", font=("Arial", 18), bg="white")
option_buttons = [tk.Button(quiz_frame, text="", width=60, height=3, font=("Arial", 14)) for _ in range(4)]

root.mainloop()

