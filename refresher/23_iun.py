# Python refresher - Day 1

# Tipuri de variabile : int, bool, str, float

number = 5
isSomething = False
name = "Matei"
pi = 3.141592


# Task 1 - Variabile Basic ✅
nume = "Matei"
varsta = 24
inaltime = 1.86
suntStudent = True


def propozitie(nume, varsta, inaltime, suntStudent):
    """
    Functie care genereaza o propozitie pe baza unor
    simplii parametrii.

    Args:
        nume (string): numele persoanei
        varsta (int): varsta persoanei
        inaltime (float): inaltimea exprimata in metrii
        suntStudent (boolean): specifica daca este student sau nu

    Returns:
        string: Propozitie care confirma datele studentului.
    """
    return f"Salut, ma numesc {nume}, am {varsta} ani, sunt foarte inalt, am {inaltime}, iar in prezent, sunt student?: {suntStudent}"


# Task 2 - Input si Type Conversion ✅
def simpleInput():
    """
    simpleInput : Intreaba utilizatorul cateva date esentiale
    si dupa face cateva calcule cu ele.
    """
    name = input("Care este numele tau?")
    numarFavorit = int(input("Care este numarul tau favorit?"))

    numarFavorit += 10
    return (
        f"Imi pare bine sa te cunosc, {name}, numarul tau favorit este {numarFavorit}"
    )


# print(simpleInput())


# Task 3 - Age Calculator ✅
def ageCalculator():
    """
    ageCalculator : Calculeaza varsta pe baza anul nasterii.

    Returns:
        string: Returneaza un f-string cu datele necesare
    """
    nume = input("Care este numele tau?\n")
    anNastere = int(input("In ce an te-ai nascut?\n"))
    return f"Imi pare bine sa te cunosc, {nume}, ai varsta de {2025-anNastere} ani."


# print(ageCalculator())


# Task 4 - Convertor Temperatura Celsius ➡ Fahrenheit + Kelvin ✅
def convertorTemperatura(temperatura):
    """
    convertorTemperatura : Functie care converteste temperatura din grade Celsius in
    Fahrenheit si Kelvin

    Args:
        temperatura (float): temperatura in Celsius

    Returns:
        f-string: F-String care afiseaza
    """
    return f"Temperatura este {temperatura * 9 / 5 + 32}° Fahrenheit si {temperatura+273}° Kelvin"


# Task 5 - Eligibil pentru permis? ✅
def eligibilPentruPermis():
    """
    eligibilPentruPermis : Verifica daca o persoana este eligibila pentru permis
    pe baza varstei.

    Returns:
        string: string de confirmare in functie de varsta pe care o are
    """
    try:
        varsta = int(input("Care este varsta ta?\n"))
        if varsta < 0 or varsta > 130:
            return "Fi realist!"
        elif varsta < 18:
            return "Nu esti eligibil pentru permis, mai asteapta."
        else:
            return "Da, esti eligibil pentru permis"
    except ValueError:
        return "Eroare: te rog introdu un numar valid"


# print(eligibilPentruPermis())


# Task 6 - Ore si minute ✅
def oreSiMinute(minute):
    """
    oreSiMinute : Converteste numarul de minute in ore si minute.

    Args:
        minute (int): Numarul de minute necesar pentru conversie.
        _nota_- Trebuie sa fie obligatoriu pozitiv!

    Returns:
        F-String: F-String cu output-ul specificat.
    """
    try:
        if minute <= 0:
            return f"Eroare! > Numarul de ore trebuie sa fie pozitiv!"
        else:
            ore = minute // 60
            return f"Sunt{ore} ore si {minute%60} minute."
    except ValueError:
        return "Eroare! > Numarul introdus nu este de tipul valid!"


# print(oreSiMinute(-205))


# Task 7 - Calculator de perimetru, arie si volum ✅
def unitatiFundamentale(lungime: float, latime: float, inaltime: float = 0):
    """
    unitatiFundamentale: Calculeaza perimetrul, aria si volumul unui obiect atunci cand este nevoie.

    Args:
        lungime (float): lungimea unui obiect
        latime (float): latimea unui obiect
        inaltime (float, optional): Inaltimea unui obiect, optionala. Daca obiectul referitor nu este tridimensional, este implicit 0.

    Returns:
        f-string: f-String cu variabilele necesare.
    """
    try:
        arie = lungime * latime
        perimetru = 2 * lungime + 2 * latime
        volum = lungime * latime * inaltime
        return f"Pentru obiectul respectiv, aria este {arie}, perimetrul este {perimetru}, iar volumul este {volum if inaltime else 0}"
    except ValueError:
        return "Eroare! > Numarul introdus nu este de tipul valid!"


# print(unitatiFundamentale(2.23, 2, 30))


# Task 8 - Ne jucam cu literele ✅
def jocCuStringuri(nume: str):
    """
    jocCuStringuri : Jocuri cu stringuri, idk.

    Args:
        nume (str): numele de oferit pentru cateva operatii cu stringurile

    Returns:
        f-string: un simplu f-string care prezinta functii de upper, lower si capitalize
    """
    try:
        return f"Numele {nume} este \n 1- Majuscule :{nume.capitalize()} \n 2- Litere Mici :{nume.lower()} \n 3- Litere Mari :{nume.upper()}"
    except AttributeError:
        return "Eroare! > Tipul pus este nespecificat!"


print(jocCuStringuri(123))
