# -*- coding: utf-8 -*-
# Zmienne do komunikatów pokazujących się po udzieleniu odpowiedzi na pytanie
ok = "Odpowiedź prawidłowa."
a = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: a."
b = "Odpowiedź nieprawidłowa. Odpowiedź prawdiłowa to: b."
c = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: c."
d = "Odpowiedź nierpawdiłowa. Odpowiedź prawidłowa to: d."

# Zmienna score do liczenia punktacji
score = 0


print ("Witam w quizie dotyczącym testów niefunkcjonalnych oprogramowania. Quiz składa się z  pytań, w każdym z pytań są 4 możliwe odpowiedzi tylko jedna z nich jest poprawna.\n")
print ("Pytanie nr 1\n Które z poniższych kryteriów najlepiej odzwierciedla skuteczność testów wydajnościowych w warunkach rzeczywistych?")
print ("a) Minimalizacja średniego czasu odpowiedzi przy niskim obciążeniu")
print ("b) Zdolność systemu do utrzymania wysokiej wydajności podczas szczytowego obciążenia przez dłuższy okres")
print ("c) Maksymalne wykorzystanie zasobów sprzętowych bez względu na koszty")
print ("d) Liczba błędów wykrytych za pomocą testów")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if  answer == "b":
    print (ok)
    score += 1

else:
    print (b, "Odpowiedź b) jest poprawna, ponieważ rzeczywiste warunki użytkowania systemu często charakteryzują się długotrwałymi okresami wysokiego obciążenia, szczególnie podczas godzin szczytu lub ważnych wydarzeń. System, który utrzymuje stabilną wydajność w takich warunkach, sprawdzi się najlepiej w rzeczywistym środowisku. Pozostałe opcje koncentrują się na pojedynczych aspektach wydajności lub nie uwzględniają kluczowego czynnika czasu trwania testów.")

print ("Pytanie nr 2\n Który aspekt testowania bezpieczeństwa jest najtrudniejszy do zautomatyzowania i wymaga największego zaangażowania człowieka?")
print ("a) Skanowanie portów i wykrywanie otwartych usług")
print ("b) Weryfikacja konfiguracji zabezpieczeń systemowych")
print ("c) Testy socjotechniczne, czyli próby manipulacji ludzkimi zachowaniami")
print ("d) Analiza logiki biznesowej pod kątem potencjalnych luk w zabezpieczeniach")

answer = input("Podaj odpowiedź: (a/b/c/d)").strip().lower()

if answer == "d":
        print (ok)
        score += 1

else:
    print (d, " Analiza logiki biznesowej wymaga głębokiego zrozumienia procesów biznesowych, kontekstu działania aplikacji oraz przewidywania nietypowych ścieżek wykorzystania systemu. Te aspekty są trudne do zautomatyzowania, ponieważ wymagają kreatywnego myślenia, umiejętności wnioskowania i analizy różnych scenariuszy, które są domeną ludzkich ekspertów. Pozostałe aspekty (skanowanie portów, weryfikacja konfiguracji) można znacznie łatwiej zautomatyzować przy użyciu specjalistycznych narzędzi.")

    print ("Pytanie nr 3 \n Który scenariusz najlepiej oddaje ideę testowania degradowalności systemu?")
print ("a) Ocena, czy system potrafi odzyskać pełną funkcjonalność po awarii")
print ("b) Testowanie zachowania systemu przy nagłym wzroście liczby użytkowników")
print ("c) Analiza utrzymania minimalnej funkcjonalności przy stopniowym ograniczaniu zasobów (np. pamięci, przepustowości)")
print ("d) Pomiar szybkości odpowiedzi systemu przy maksymalnym obciążeniu")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer ==  "c":
    print (ok)
    score += 1

else:
    print (c, "Testowanie degradowalności koncentruje się na sprawdzeniu, czy system potrafi nadal działać (choć z ograniczoną funkcjonalnością) w warunkach ograniczonych zasobów. Jest to kluczowe dla zapewnienia ciągłości działania w sytuacjach awaryjnych. System, który potrafi się zdegradować w kontrolowany sposób, zamiast całkowicie przestać działać, zapewnia lepsze doświadczenia użytkownika w trudnych warunkach.")

print ("Pytanie nr 4\n W kontekście testów użyteczności, które narzędzie/metoda dostarcza najbardziej wiarygodnych danych o rzeczywistym zachowaniu użytkowników?")
print ("a) Ankiety online po zakończeniu korzystania z aplikacji")
print ("b) Testy A/B z rejestrowaniem interakcji użytkowników")
print ("c) Testy moderowane z rzeczywistymi użytkownikami, obserwowane na żywo")
print ("d) Wywiady indywidualne z grupą docelową")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print (ok)
    score += 1

else:
    print (b, "Testy A/B dostarczają obiektywnych danych ilościowych o rzeczywistym zachowaniu użytkowników w naturalnym środowisku, bez wpływu obecności obserwatorów. Rejestrowanie interakcji (kliknięcia, czas spędzony na stronie, ścieżki nawigacji) pozwala na dokładną analizę zachowań bez subiektywnych opinii użytkowników. Pozostałe metody opierają się bardziej na deklarowanych opiniach lub zachowaniu w sztucznych warunkach, co może prowadzić do mniej wiarygodnych wyników.")

print ("Pytanie nr 5 \n Który z poniższych parametrów jest kluczowy przy testach dostępności (accessibility testing)?")
print ("a) Szybkość ładowania strony lub aplikacji")
print ("b) Zgodność z wytycznymi WCAG oraz normami dla osób niepełnosprawnych")
print ("c) Responsywność interfejsu przy różnych rozdzielczościach ekranu")
print ("d) Liczba dostępnych funkcji poprawiających komfort użytkowania")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print(ok)
    score += 1

else:
    print (b, "Wytyczne WCAG (Web Content Accessibility Guidelines) stanowią międzynarodowy standard dostępności cyfrowej, opracowany specjalnie, aby zapewnić dostęp do treści internetowych osobom z różnymi niepełnosprawnościami. Zgodność z tymi wytycznymi jest nie tylko dobrą praktyką, ale często również wymogiem prawnym w wielu krajach. Pozostałe parametry, choć ważne dla ogólnego doświadczenia użytkownika, nie adresują bezpośrednio potrzeb osób z niepełnosprawnościami.")

print ("Pytanie nr 6\n Które podejście najlepiej opisuje strategię testowania ryzyka w obszarze testów niefunkcjonalnych")
print ("a) Testowanie wszystkich komponentów systemu w równym stopniu")
print ("b) Skupienie się na krytycznych komponentach, które w razie awarii mają największy wpływ na użytkownika i biznes")
print ("c) Przeprowadzanie testów tylko po wystąpieniu problemu w środowisku produkcyjnym")
print ("d)  Zastosowanie wyłącznie automatycznych narzędzi do kompleksowego testowania")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print(ok)
    score += 1

else:
    print (b, "Strategia testowania oparta na ryzyku polega na priorytetyzacji testów według potencjalnego wpływu awarii na biznes i użytkowników. Pozwala to na efektywne wykorzystanie ograniczonych zasobów testowych i skupienie się na obszarach o największym znaczeniu. Jest to podejście pragmatyczne, uznające, że testowanie wszystkiego w równym stopniu jest często niemożliwe i nieefektywne z punktu widzenia biznesowego.")


print ("Pytanie nr 7\n Która z poniższych metod testowania bezpieczeństwa opiera się na wysyłaniu losowych, nieprzewidywalnych danych w celu wykrycia nieoczekiwanych błędów")
print ("a) Testy penetracyjne")
print ("b) Testy regresyjne sprawdzające stabilność systemu po zmianach")
print ("c) Analiza statyczna kodu źródłowego")
print ("d) Testy fuzzingowe")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "d":
    print (ok)
    score += 1

else:
    print (d, "Fuzzing to technika polegająca na dostarczaniu do aplikacji przypadkowych, niespodziewanych lub nieprawidłowych danych wejściowych, by wykryć błędy, które mogą prowadzić do luk w zabezpieczeniach. Jest szczególnie skuteczna w znajdowaniu problemów, których nie da się łatwo przewidzieć przy standardowym testowaniu. Pozostałe metody mają inne zastosowania i nie opierają się na wprowadzaniu losowych danych.")

print ("Pytanie nr 8\n Jak najlepiej zdefiniować pojęcie latent defects (ukryte defekty) w kontekście testów niefunkcjonalnych?")
print ("a) Błędy ujawniane wyłącznie podczas testów wydajnościowych")
print ("b) Usterki obecne w interfejsie użytkownika, które są łatwe do przeoczenia")
print ("c) Wady systemu ujawniające się dopiero przy specyficznych, rzadkich warunkach operacyjnych")
print ("d) Błędy wykrywane natychmiast po wdrożeniu systemu")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "c":
    print (ok)
    score += 1

else:
    print (c, "Ukryte defekty to problemy, które nie ujawniają się podczas standardowego testowania, a wychodzą na jaw dopiero w specyficznych, często trudnych do odtworzenia warunkach. Mogą to być problemy z pamięcią ujawniające się po długim czasie działania systemu, błędy występujące tylko przy określonych kombinacjach danych czy specyficznym obciążeniu. Ich wykrycie jest trudne i często wymaga specjalistycznych testów niefunkcjonalnych, które symulują długotrwałe lub nietypowe warunki pracy.")

print ("Pytanie nr 9\n Jaką rolę odgrywają testy niefunkcjonalne w kontekście Continuous Integration/Continuous Deployment (CI/CD)?")
print ("a) Są zbędne, ponieważ CI/CD skupia się wyłącznie na testach funkcjonalnych")
print ("b) Umożliwiają szybkie wykrycie regresji wydajnościowych, problemów z kompatybilnością i innych aspektów, zanim zmiany trafią na produkcję")
print ("c) Zastępują konieczność przeprowadzania testów jednostkowych i integracyjnych")
print ("d) Są przydatne tylko w końcowej fazie testowania, tuż przed wdrożeniem")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print (ok)
    score += 1

else:
    print (b, "W środowisku CI/CD, gdzie zmiany są często i szybko wdrażane, testy niefunkcjonalne stanowią istotną linię obrony przed wprowadzeniem regresji w obszarach takich jak wydajność, bezpieczeństwo czy kompatybilność. Automatyzacja tych testów i włączenie ich do procesu CI/CD pozwala na wczesne wykrycie problemów, które mogłyby negatywnie wpłynąć na doświadczenia użytkowników, jeszcze zanim zmiany trafią na środowisko produkcyjne.")

print ("Pytanie nr 10\n Testy użyteczności (Usability Testing) skupiają się głównie na:")
print ("a) Sprawdzeniu, czy aplikacja działa na urządzeniach mobilnych")
print ("b)  Ocenie, jak szybko użytkownik wykonuje kluczowe zadania")
print ("c) Wykrywaniu błędów w logice biznesowej")
print ("d)  Analizie zgodności z normą ISO 9241")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print (ok)
    score += 1

else:
    print (b, "Testy użyteczności koncentrują się przede wszystkim na mierzeniu efektywności, z jaką użytkownicy realizują kluczowe zadania w systemie. Szybkość wykonywania zadań jest bezpośrednio związana z intuicyjnością interfejsu i łatwością korzystania z systemu. Pozostałe odpowiedzi dotyczą albo innych typów testów (jak testy responsywności czy funkcjonalne), albo tylko częściowo pokrywają się z obszarem testów użyteczności.")

print ("Pytanie nr 11\n Który test sprawdza, czy system odzyskuje sprawność w czasie krótszym niż 5 minut po awarii zasilania")
print ("a) Testy wytrzymałościowe (Endurance Testing)")
print ("b) Testy odpornościowe (Resilience Testing)")
print ("c) Testy odzyskiwania (Recovery Testing)")
print ("d) Testy ciągłości działania (Disaster Recovery Testing")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "c":
    print(ok)
    score += 1

else:
    print (c, "Testy odzyskiwania (Recovery Testing) są specjalnie zaprojektowane do weryfikacji, jak szybko i skutecznie system powraca do normalnego funkcjonowania po wystąpieniu awarii, w tym przypadku awarii zasilania. Mierzą one czas potrzebny do przywrócenia usług oraz sprawdzają, czy dane nie zostały utracone lub uszkodzone podczas procesu odzyskiwania. Pozostałe typy testów koncentrują się na innych aspektach niezawodności systemu.")

print ("Pytanie nr 12\n Co jest głównym celem testów Chaosu Inżynieryjnego (Chaos Monkey)?")
print ("a) Symulacja awarii zasilania w centrum danych")
print ("b) Wprowadzanie losowych awarii, aby wymusić projektowanie systemu pod kątem odporności")
print ("c) Testowanie maksymalnego obciążenia bazy danych")
print ("d) Wykrywanie luk w zabezpieczeniach API")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print (ok)
    score += 1

else:
    print (b, "Testy Chaosu Inżynieryjnego, spopularyzowane przez narzędzie Netflix Chaos Monkey, celowo wprowadzają losowe awarie do systemu produkcyjnego, aby wymusić budowanie systemów bardziej odpornych na awarie. Podstawowym założeniem jest, że awarie są nieuniknione, więc lepiej jest testować odporność systemu regularnie i w kontrolowany sposób, niż czekać na rzeczywistą awarię. Takie podejście promuje projektowanie systemów z myślą o tolerowaniu awarii poszczególnych komponentów")

print ("Pytanie nr 13\n Co to jest baseline w kontekście testów wydajnościowych")
print ("a) Minimalny akceptowalny poziom wydajności systemu")
print ("b) Punkt odniesienia do porównania wyników przyszłych testów")
print ("c) Linia bazowa kodu źródłowego poddawana testom")
print ("d) Podstawowy scenariusz testowy")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "b":
    print (ok)
    score += 1

else:
    print (b, "Baseline to punkt odniesienia (wzorzec) służący do porównania wyników przyszłych testów, pozwalający na śledzenie zmian w wydajności systemu. Ustalenie takiego punktu odniesienia jest kluczowe do wykrywania regresji wydajnościowych i oceny wpływu wprowadzanych zmian. Pozwala odpowiedzieć na pytanie, czy wydajność systemu poprawia się czy pogarsza w kolejnych wersjach.")

print ("Pytanie nr 14\n Co oznacza termin Time to First Byte (TTFB) w kontekście testów wydajnościowych?")
print ("a) Czas od wysłania żądania do otrzymania pierwszego bajtu odpowiedzi")
print ("b) Czas do pierwszego uruchomienia aplikacji")
print ("c) Czas do pierwszego błędu w systemie")
print ("d) Czas pierwszej interakcji użytkownika z systemem")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "a":
    print (ok)
    score += 1

else:
    print (a, "TTFB to czas od wysłania żądania do otrzymania pierwszego bajtu odpowiedzi, co stanowi ważny wskaźnik responsywności serwera. Jest to kluczowa metryka w testach wydajnościowych stron internetowych i aplikacji webowych, ponieważ bezpośrednio wpływa na postrzeganie szybkości ładowania przez użytkownika. Wysoki TTFB może wskazywać na problemy z serwerem, bazą danych lub siecią, które wymagają optymalizacji.")

print ("Pytanie nr 15\n Co jest głównym celem testów obciążeniowych (load testing)?")
print ("a) Sprawdzenie, jak system zachowuje się przy maksymalnym przewidywanym obciążeniu")
print ("b) Określenie punktu załamania systemu")
print ("c) Testowanie odporności systemu na atak")
print ("d) Sprawdzenie czasu odpowiedzi dla pojedynczego użytkownika")

answer = input("Podaj odpowiedź: (a/b/c/d/) ").strip().lower()

if answer == "a":
    print (ok)
    score += 1

else:
    print (a, "esty obciążeniowe mają na celu sprawdzenie zachowania systemu przy maksymalnym przewidywanym obciążeniu, w odróżnieniu od testów przeciążeniowych (stress testing), które mają na celu znalezienie punktu załamania. Ich celem jest upewnienie się, że system będzie działał prawidłowo i spełniał wymagania wydajnościowe nawet w okresach szczytowego użytkowania. Testy te pozwalają zidentyfikować wąskie gardła i problemy, które mogą wystąpić w rzeczywistych warunkach eksploatacyjnych.")

# Wyświetlenie uzyskanej punktacji z quizu
print(f"Twój wynik to: {score}/15 punktów. Dziękuję za udział w quizie!")