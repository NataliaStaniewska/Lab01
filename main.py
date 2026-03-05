from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# ZADANIE 1
# wczytanie danych
iris = load_iris()
X = iris.data
y = iris.target

# zamiana na DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["target"] = y

# wyświetlenie 5 pierwszych wierszy
print("Pierwsze 5 wierszy:")
print(df.head())

# sprawdzenie rozmiaru danych
print("\nRozmiar danych:")
print(df.shape)

# sprawdzenie typów kolumn
print("\nTypy kolumn:")
print(df.dtypes)

#ZADANIE 2

# podzielenie zbioru danych na treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# utworzenie modelu
model = LogisticRegression(max_iter=1000)

# trening modelu
model.fit(X_train, y_train)

# przewidywanie
y_pred = model.predict(X_test)

# metryki
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:")
print(accuracy)

print("\nRaport klasyfikacji:")
print(classification_report(y_test, y_pred))

# ZADANIE 3
# zapisanie modelu do pliku
joblib.dump(model, "model_v1.joblib")
