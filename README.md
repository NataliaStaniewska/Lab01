# Nowoczesne Technologie Przetwarzania Danych  
# Lab01


**Zadanie 4 - wersjonowanie**  
W projekcie wprowadziłam proste wersjonowanie modeli przez nazwy plików. Zapisany model ma nazwę model_v1.joblib a każda następna jego wersja będzie zapisywana w nowym pliku z wyższym numerem wersji (np. model_v2.joblib, model_v3.joblib), zamiast nadpisywać poprzedni plik.

Numer wersji modelu należy zwiększyć, gdy zmieni się coś istotnego w działaniu modelu, np. zmiany w hiperparametrach, użyty algorytm, dane treningowe, zestaw cech wejściowych albo gdy nowa wersja osiąga wyraźnie lepsze wyniki.


    

**Zadanie 5 - Różnice między środowiskiem deweloperskim a produkcyjnym**
1.	Dane  
W środowisku developerskim dane są czyste, kompletne, często statystyczne.  W produkcji mamy do czynienia z danymi z „realnego świata”, które często bywają niepełne, z błędami. Można sobie z tym poradzić stosując walidację wejścia i obsługę wyjątków czy monitorowanie rozkładów cech i jakości predykcji

2.	Ocena jakości modelu  
W środowisku developerskim jakość modelu sprawdza się na zbiorze testowym i wylicza metryki takie jak: accuracy, precision czy recall. W produkcji dane mogą wyglądać inaczej, więc model może działać gorzej niż w testach, a poprawne odpowiedzi nie zawsze są dostępne od razu. Można sobie z tym poradzić zbierając informacje zwrotne czyli prawdziwe etykiety, regularnie licząc metryki na danych z produkcji oraz wdrażając model stopniowo.

3.	Środowisko uruchomieniowe  
W środowisku developerskim przeważnie pojawia się mniej problemów bo wszystko jest ustawione lokalnie. W produkcji środowisko musi być powtarzalne i stabilne. Można sobie z tym poradzić pilnując zależności (requirements.txt), używając wirtualnych środowisk i kontenerów oraz testując uruchomienie w CI.

4.	Monitorowanie modelu  
W produkcji trzeba na bieżąco obserwować, czy model działa poprawnie i czy nie spada jakość jego predykcji, a także czy działa wystarczająco szybko. Można sobie z tym poradzić zbierając logi i podstawowe statystyki np. czas odpowiedzi, liczba błędów oraz ustawiając alerty, gdy coś odbiega od normy.

5.	Retraining i automatyzacja  
W środowisku developerskim często model jest trenowany jednorazowo. W produkcji może tracić jakość, więc wymaga retrainingu oraz kontrolowanego wdrażania. Można sobie z tym poradzić planując retraining (cykliczny lub po wykryciu driftu) i automatyzując proces przez CI/CD.

