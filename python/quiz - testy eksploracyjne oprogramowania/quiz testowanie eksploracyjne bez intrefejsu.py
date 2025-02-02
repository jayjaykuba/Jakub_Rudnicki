# -*- coding: utf-8 -*-
#zmienne do komunikatów pojawiających się po udzieleniu odpowiedzi
ok = "Odpowiedź prawidłowa."
bad_a = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: a"
bad_b = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: b"
bad_c = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: c"
bad_d = "Odpowiedź nieprawidłowa. Odpowiedź prawidłowa to: d"

# Zmienna score służaca do liczenia punktacji
score = 0

print ("Witam w quizie dotyczącym testowania eksploracyjnego oprogramowania. Quiz składa się z 15 pytań, w każdym z pytań są 4 możliwe odpowiedzi tylko jedna z nich jest poprawna.\n")
print("Pytanie nr 1")
print("Kto najczęściej wykonuje testy eksploracyjne?")
print('a: Użytkownicy końcowi ')
print("b: Autmatyczne narzędzia testowe")
print("c: Interesariusze")
print("d: Testerzy")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "d":
    print(ok)
    score += 1
else:
    print(bad_d)

print("Pytanie nr 2")
print("Jaki jest głowny cel testów eksploracyjnych")
print('a: Znalezienie luk w zabezpiczeniach ')
print("b: Przeprowadzenie testów wydajnościowych")
print("c: Znalezienie nieznaych wcześniej błędów poprzez eksplorację systemu")
print("d: Weryfikacja zgodności z wymogami regulacyjnymi")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "c":
    print(ok)
    score += 1
else:
    print(bad_c)

print("Pytanie nr 3")
print("Co stanowi największe wyzwanie w testach eksploracyjnych?")
print('a: Brak możliwości automatyzacji')
print("b: Konieczność ciągłego dostosowywania się do zmieniających się wymagań biznesowych w trakcie testowania")
print("c: Trudność w powtarzalności testów")
print("d: Wymóg posiadania specjalistycznej wiedzy programistycznej")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "c":
    print(ok)
    score += 1
else:
    print(bad_c)

print("Pytanie nr 4")
print("Jedną z głównych metod do zarządzania testami eksploracyjnymi jest:")
print('a: Testy regresyjne')
print("b: Zarządzanie testami oparte na sesjach")
print("c: Projektowanie przypadków testowych")
print("d: Automatyzacja testów eksploracyjnych")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "b":
    print(ok)
    score += 1
else:
    print(bad_b)

print("Pytanie nr 5")
print("Co jest głównym elementem opisu celu pojedynczej sesji testów eksploracyjnych?")
print('a: Raport z poprzednich testów regresyjnych')
print("b: Harmonogram spotkań zespołu testowego")
print("c: Dokumentacja wymagań biznesowych")
print("d:Statut (charter) sesji")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "d":
    print(ok)
    score += 1
else:
    print(bad_d)

print("Pytanie nr 6")
print("Czym jest sesja debriefingowa z liderem?")
print('a: Przegląd dokumentacji wymagań przed rozpoczęciem testów')
print("b: Szkolenie zespołu testowego na temat nowych narzędzi")
print("c: Sesja planowania kolejnych testów regresyjnych")
print("d: Spotkanie podsumowujące wyniki sesji testowej i omawiające wnioski")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "d":
    print(ok)
    score += 1
else:
    print(bad_d)

print("Pytanie nr 7")
print("W czym skrypt Selenium może być najbardziej pomocny w testach eksploracyjnych?")
print('a: Rejestracja działań testera w celu późniejszej analizy lub odtworzenia kroków')
print("b: Automatyzacja powtarzalnych czynności, aby tester mógł skupić się na eksploracji")
print("c: Generowanie raportów z testów regresyjnych")
print("d: Tworzenie statutów (charterów) dla sesji testowych")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "a":
    print(ok)
    score += 1
else:
    print(bad_a)

print("Pytanie nr 8")
print("Jakie są różnice między testowaniem ad hoc a testami eksploracyjnymi?")
print('a: Testy eksploracyjne są wykonywane tylko przez nowicjuszy, a testy ad hoc przez doświadczonych testerów.')
print("b: Testy ad hoc są zawsze dokumentowane, a testy eksploracyjne polegają wyłącznie na intuicji testera.")
print("c: Testy ad hoc są całkowicie nieplanowane, podczas gdy testy eksploracyjne mają określony cel i strukturę, np. statut (charter).")
print("d: Testy eksploracyjne wymagają użycia narzędzi do automatyzacji, a testy ad hoc są wykonywane manualnie.")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "c":
    print(ok)
    score += 1
else:
    print(bad_c)

print("Pytanie nr 9")
print("Co jest główną cechą testowania eksploracyjnego")
print('a: Wykonywanie testów bez wcześniejszego przygotowania testowych przypadków')
print("b: Ścisłe trzymanie się scenariuszy testowych")
print("c: Unikanie dokumentowania testów")
print("d: Automatyczne wykonywanie testów")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "a":
    print(ok)
    score += 1
else:
    print(bad_a)

print("Pytanie nr 10")
print("Jakie umiejętności są kluczowe dla testera podczas testowania eksploracyjnego?")
print('a: Znajomość języków programowania')
print("b: Ścisłe trzymanie się test planu")
print("c: Umiejętność pisania skryptów automatycznych")
print("d: Krytyczne myślenie, intuicja i doświadczenie testerskie")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "d":
    print(ok)
    score += 1
else:
    print(bad_d)

print("Pytanie nr 11")
print("W jakich sytuacjach testowanie eksploracyjne jest szczególnie zalecane?")
print('a: Kiedy testy systemowe muszą być przeprowadzane w pełnej zgodności z wcześniejszymi przypadkami testowymi i dokumentacją')
print("b: Kiedy w projekcie wymagane jest skrupulatne śledzenie każdej zmiany w systemie za pomocą regresji manualnych")
print("c: Kiedy zespół testerski ma niewiele czasu, a wymagania systemowe są niejasne lub często się zmieniają")
print("d: Kiedy dostępność narzędzi automatycznych jest ograniczona, a wymagania dotyczące pełnej dokumentacji są wysokie")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "c":
    print(ok)
    score += 1
else:
    print(bad_c)

print("Pytanie nr 12")
print("Jaka jest największa wartość testowania eksploracyjnego w porównaniu do tradycyjnych testów opartych na przypadkach testowych?")
print('a: Pozwala całkowicie zastąpić testy oparte na przypadkach testowych, eliminując potrzebę wcześniejszego planowania')
print("b: Zapewnia pełną powtarzalność i ułatwia audytowanie procesu testowego w długoterminowych projektach")
print("c: Umożliwia szybkie wykrycie defektów w systemie, szczególnie tych, które nie były przewidziane w formalnych przypadkach testowych")
print("d: Jest jedynym skutecznym sposobem testowania systemów krytycznych, takich jak oprogramowanie medyczne czy lotnicze")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "c":
    print(ok)
    score += 1
else:
    print(bad_c)

print("Pytanie nr 13")
print("Która z poniższych cech najlepiej opisuje sposób dokumentowania wyników testów eksploracyjnych?")
print('a: Wyniki testów eksploracyjnych są dokumentowane w formie strukturalnych przypadków testowych, aby zapewnić powtarzalność testów')
print("b: Wyniki testów eksploracyjnych mogą być dokumentowane w formie notatek testerskich lub raportów błędów, zamiast ścisłych przypadków testowych")
print("c: Testowanie eksploracyjne nie wymaga żadnej dokumentacji, ponieważ opiera się wyłącznie na wiedzy testerów i ich doświadczeniu")
print("d: Testy eksploracyjne wymagają pełnej dokumentacji planu testów, ponieważ są częścią formalnego procesu walidacji")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "b":
    print(ok)
    score += 1
else:
    print(bad_b)

print("Pytanie nr 14")
print("W jaki sposób testowanie eksploracyjne może wspierać testowanie regresyjne w dużych projektach?")
print('a: Może być używane do odkrywania nieoczekiwanych skutków ubocznych zmian w kodzie, które nie zostały uwzględnione w istniejących przypadkach testowych')
print("b: Umożliwia pełną automatyzację testów regresyjnych, eliminując potrzebę pisania skryptów testowych")
print("c: Zapewnia 100% pokrycie testowe, co oznacza, że można uniknąć tradycyjnych testów regresyjnych")
print("d: Jest wykorzystywane wyłącznie do testowania interfejsów użytkownika i nie ma zastosowania w testach regresyjnych")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "a":
    print(ok)
    score += 1
else:
    print(bad_a)

print("Pytanie nr 15")
print("Jakie podejście do zarządzania ryzykiem jest zgodne z testowaniem eksploracyjnym?")
print('a: W testowaniu eksploracyjnym ryzyko jest minimalne, ponieważ testerzy pracują wyłącznie na podstawie swojej intuicji')
print("b: Ryzyko w testowaniu eksploracyjnym jest trudne do kontrolowania, ponieważ nie można go oszacować przed rozpoczęciem testów")
print("c: Testowanie eksploracyjne jest mniej efektywne w zarządzaniu ryzykiem, ponieważ nie pozwala na wcześniejsze zaplanowanie przypadków testowych")
print("d: Testowanie eksploracyjne jest szczególnie przydatne w obszarach wysokiego ryzyka, ponieważ umożliwia szybkie wykrywanie nieprzewidzianych problemów")
odpowiedz = input("Podaj odpowiedź (a/b/c/d/): ")

if odpowiedz == "d":
    print(ok)
    score += 1
else:
    print(bad_d)

# Wyświetlenie uzyskanej punktacji z quizu
print(f"Twój wynik to: {score}/15 punktów. Dziękuję za udział w quizie!")