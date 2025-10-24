# Liste, tuple si mai mult

# -- Liste --

# 🔹 1. Creează o listă cu 5 orașe și afișează-o. ✅
orase = ["Suceava", "Botosani", "Cluj", "Bacau", "Maramures"]
print(orase)

# 🔹 2. Afișează al doilea și al patrulea element din listă. ✅
print(orase[1], orase[3])

# 🔹 3. Înlocuiește al treilea element cu alt oraș. ✅
orase[2] = "Bucuresti"
print(orase)

# 🔹 4. Adaugă un nou oraș la sfârșitul listei. ✅
orase.append("Constanta")
print(orase)

# 🔹 5. Inserează un oraș pe poziția 2. ✅
orase.insert(1, "Timisoara")
print(orase)

# 🔹 6. Elimină un oraș după valoare. ✅
orase.remove("Bucuresti")
print(orase)

# 🔹 7. Afișează lungimea listei. ✅
print(len(orase))

# 🔹 8. Sortează lista în ordine alfabetică și afișează-o. ✅
orase.sort()
print(orase)

# 🔹 9. Parcurge lista cu un for și afișează fiecare oraș în format: Orasul: <nume>. ✅

for oras in orase:
    print("Orasul: ", oras)

# 🔹 10. Creează o listă cu numere întregi, calculează și afișează suma tuturor elementelor. ✅
elemente = [1, 5, 23, 3.41, 10]
print(sum(elemente))


# # -- Tuple --
# ✨ 1. Creează un tuplu cu 4 numere întregi și afișează-l. ✅
nr_intregi = (4, 2, 9, 10)
print(nr_intregi, type(nr_intregi))

# ✨ 2. Creează un tuplu cu 3 culori și afișează primul și ultimul element. ✅
tp_culori = ("rosu", "galben", "albastru")
print(tp_culori[0])
print(tp_culori[-1])

# ✨ 3. Verifică dacă "verde" se află într-un tuplu de culori. ✅

if "verde" in tp_culori:
    print("Verde se afla in tuplul de culori")
else:
    print("Verde nu se afla in tuplul de culori")

# ✨ 4. Afișează lungimea unui tuplu cu zilele săptămânii. ✅

tp_zileSapt = ("luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica")
print(len(tp_zileSapt))

# ✨ 5. Creează două tupluri de numere și concatenează-le. ✅

tp_nr1 = (1, 2, 3)
tp_nr2 = (4, 5, 6)
tp_nr3 = tp_nr1 + tp_nr2
print(tp_nr1 + tp_nr2)

# ✨ 6. Creează un tuplu cu un singur element (ex.: 100). Afișează tipul variabilei. ✅
tp_singurElement = (100,)
print(tp_singurElement)
print(type(tp_singurElement[0]))

# ✨ 7. Fă slicing dintr-un tuplu cu numere: selectează elementele de pe pozițiile 1 până la 3. ✅
print(tp_nr3[0:3])

# ✨ 8. Parcurge un tuplu cu un for și afișează fiecare element. ✅

for element in tp_nr3:
    print("Elementul : ", element)

# ✨ 9. Creează un tuplu și multiplică-l de 3 ori (ex.: tup * 3). Afișează rezultatul. ✅
tp_exemplu = (1, 2, 3)
print(tp_exemplu * 3)


# ✨ 10. Scrie o funcție care primește un tuplu de numere și returnează suma lor. ✅


def sumaTupluri(tp1: tuple, tp2: tuple):
    """
    sumaTupluri :  Returneaza suma elementelor unor tupluri de numere.

    Args:
        tp1 (tuple): Primul tuplu de numere
        tp2 (tuple): Al doilea tuplu de numere

    Returns:
        f-string: String cu suma respectiva.
    """
    suma = sum(tp1) + sum(tp2)
    return f"Suma tuplurilor este {suma}"


print(sumaTupluri(tp_nr1, tp_nr2))


# # -- Dictionare --
# ✨ 1. Creează un dicționar cu cheile: "nume", "vârstă", "oraș". Afișează-l. ✅

primul_dictionar = {"nume": "Matei", "varsta": 24, "oras": "Suceava"}
print(primul_dictionar)

# ✨ 2. Afișează valoarea cheii "nume". ✅
print(primul_dictionar["nume"])
print(primul_dictionar.get("nume"))

# ✨ 3. Modifică valoarea cheii "oraș" cu alt oraș. ✅
primul_dictionar["oras"] = "Bacau"
print(primul_dictionar.get("oras"))

# ✨ 4. Adaugă o cheie nouă numită "profesie" cu o valoare la alegere.✅
primul_dictionar["profesie"] = "Analist"
print(primul_dictionar)

# ✨ 5. Verifică dacă cheia "vârstă" există în dicționar.✅
if "varsta" in primul_dictionar:
    print("Cheia este in dictionar")

# ✨ 6. Șterge cheia "profesie" din dicționar.✅
primul_dictionar.pop("profesie")
print(primul_dictionar)

# ✨ 7. Afișează toate cheile din dicționar. ✅
print(primul_dictionar.keys())

# ✨ 8. Afișează toate valorile din dicționar. ✅
print(primul_dictionar.values())

# ✨ 9. Parcurge dicționarul și afișează fiecare pereche cheie: valoare. ✅
for k, v in primul_dictionar.items():
    print(k, " = ", v)

# ✨ 10. Creează un dicționar care conține numele unui student și o listă cu 3 note. Afișează media notelor ✅.
studentDict = {"nume": "Matei", "note": [10, 9, 8]}
print(sum(studentDict.get("note")) / len(studentDict.get("note")))


# RECAPITULARE FINALA
# ✨ 1. Creează o listă cu 4 animale și afișează al doilea și ultimul element. ✅
listaAnimale = ["catel", "pisica", "peste", "tigru"]
print(listaAnimale[1], listaAnimale[-1])

# ✨ 2. Adaugă un animal nou în listă și elimină altul după nume. ✅
listaAnimale.append("leu")
print(listaAnimale)
listaAnimale.remove("peste")
print(listaAnimale)

# ✨ 3. Creează un tuplu cu 5 numere. Afișează elementele de la indexul 1 la 3 (slicing). ✅
tupluNumere = (5, 19, 398, 29, 18)
print(tupluNumere[1:4])

# ✨ 4. Verifică dacă numărul 10 există în tuplu. ✅
if 10 in tupluNumere:
    print("Exista in tuplu")
else:
    print("Nu exista in tuplu")

# ✨ 5. Creează un dicționar cu cheile: "produs", "cantitate", "pret". Afișează fiecare pereche cheie-valoare ✅.
dictProdus = {"produs": "Lapte", "cantitate": 100, "pret": 15}

for cheie, valoare in dictProdus.items():
    print(cheie, " → ", valoare)

# ✨ 6. Modifică valoarea cheii "cantitate" și adaugă cheia "categorie". ✅
dictProdus["cantitate"] = 50
print(dictProdus)
dictProdus["categorie"] = "Lactate"
print(dictProdus)

# ✨ 7. Creează o listă de tupluri, fiecare conținând două elemente: nume produs + preț. Afișează lista. ✅
listaProduse = [("Lapte", 10), ("Salam", 35), ("Paine", 5)]
print(listaProduse)

# ✨ 8. Creează un dicționar care conține: nume student + tuplu cu 3 note. Calculează media.✅
studentDictionar = {"nume": "Matei", "note": (10, 8, 5)}
print(round(sum(studentDictionar.get("note")) / len(studentDictionar.get("note")), 2))

# ✨ 9. Sortează lista de animale în ordine alfabetică și afișează-o. ✅
listaAnimale.sort()
print(listaAnimale)

# ✨ 10. Parcurge lista de tupluri de la exercițiul 7 și afișează fiecare produs cu prețul său. ✅
for element in listaProduse:
    print(element[0], " → ", element[1])

# sau

for nume, pret in listaProduse:
    print("Produsul ", nume, " costa ", pret)

print(len(dictProdus))
