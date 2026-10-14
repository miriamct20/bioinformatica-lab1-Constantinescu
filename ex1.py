def melting_temp(seq):
    seq = seq.upper().replace(" ", "")
    if set(seq) - set("ACGT"):
        raise ValueError("Sequence may contain only A, C, G, T")
    gc = seq.count("G") + seq.count("C")
    at = seq.count("A") + seq.count("T")
    return 4 * gc + 2 * at

S = "TAACGCTA"
print(f"Tm of {S} = {melting_temp(S)} °C")  

import matplotlib.pyplot as plt

S = "TAACGCTA"

baze = ["A", "T", "G", "C"]
frecvente = [S.count("A"), S.count("T"), S.count("G"), S.count("C")]

plt.bar(baze, frecvente, color=["green", "red", "orange", "blue"])
plt.title("Frecventa bazelor in " + S)
plt.xlabel("Baza")
plt.ylabel("Frecventa")
plt.show()