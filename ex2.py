import math

S = input("DNA sequence: ").upper().replace(" ", "")
Na = float(input("Na+ concentration: "))

A = S.count("A")
T = S.count("T")
G = S.count("G")
C = S.count("C")
N = len(S)

if A + T + G + C != N or N == 0:
    print("Error: use only A, T, G, C")
else:
    GC_percent = (G + C) / N * 100

   
    Tm1 = 4 * (G + C) + 2 * (A + T)

    Tm2 = 81.5 + 16.6 * math.log10(Na) + 0.41 * GC_percent - 600 / N

    print("Length:", N, " GC%:", round(GC_percent, 1))
    print("Tm (Wallace)      =", Tm1, "°C")
    print("Tm (salt-adjusted) =", round(Tm2, 1), "°C")
    import matplotlib.pyplot as plt

numar_GC = [3, 4, 5, 6, 7, 8]
valori_Tm = [0.3, 5.4, 10.5, 15.7, 20.8, 25.9]

plt.plot(numar_GC, valori_Tm, marker="o")
plt.title("Tm vs number of C + G")
plt.xlabel("Number of C + G")
plt.ylabel("Tm (°C)")
plt.grid(True)
plt.show()