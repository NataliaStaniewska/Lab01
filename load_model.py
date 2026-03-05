import joblib

# wczytanie modelu
model = joblib.load("model_v1.joblib")

# przykładowy rekord
sample = [[5.1, 3.5, 1.4, 0.2]]

# predykcja
prediction = model.predict(sample)
print("Przewidziana klasa:", prediction[0])