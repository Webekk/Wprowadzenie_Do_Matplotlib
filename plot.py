#Dodawanie odpowiednich paczek i modulow
import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie danych
x = np.linspace(0, 10, 100)

# Skladanie danych w funkcje
plt.plot(x, x, label='funkcja liniowa')

# Dodanie legendy
plt.legend()

# Pokazanie Funkcji
plt.show()
