#  [ 24 OCT - Here again ]

# Python Basics

# 4 Tipuri de variabile : int float bool string

integer = 5
floatingstuff = 5.5
isbool = True
anotherString = "I'm a string"

# print(integer, floatingstuff, isbool, anotherString)


# Exercitii

# TODO → Meniu pentru ziua asta.


# [1] - Calculator IMC ✅
def IMC_Calculator():
    """
    IMC_Calculator: Calculeaza Indicele de Masa Musculara (IMC) pe baza parametrilor inclusi.

    Returns:
        string: String cu indicele IMC.
    """
    try:
        weight = float(input("Introduceti greutatea in KG\n "))
        height = float(input("Introduceti inaltimea in M\n "))
        IMC = weight / height**2
        return f"Indicele IMC este {IMC:.2f}"
    except ValueError:
        return "Eroare. Introduceti date valide (float)."


# print(IMC_Calculator())


# [2] - Par sau Impar ✅
def ParImpar():
    """
    ParImpar: Verifica daca un numar este par sau impar.

    Returns:
        string: String de specificare daca numarul este par sau nu.
    """
    try:
        numar = float(input("Introduceti un numar \n "))
        rezultat = "par" if numar % 2 == 0 else "impar"
        return f"Numarul {numar} este {rezultat}"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(ParImpar())


# [3] - Calculator pret redus ✅
def calculatorPretRedus():
    """
    calculatorPretRedus: Calculeaza pretul unui produs dupa reducere.

    Returns:
        string: String de pretul unui produs.
    """
    try:
        pret = float(input("Introduceti pretul unui produs \n"))
        reducere = float(input("Introduceti reducerea produsului \n"))
        pretFinal = pret - (pret * reducere) / 100
        return f"Pretul final dupa reducere este {pretFinal}"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(calculatorPretRedus())


# [4] - Salut ✅
def salutare(nume):
    """
    salutare: Functie simpla de salut.

    Args:
        nume (string): Numele persoanei respective

    Returns:
        string: Un mesaj de salutare.
    """
    try:
        return f"Salut {nume}, ma bucur sa te cunosc! 😊"
    except AttributeError:
        return "Eroare. Introduceti un numar valid."


# print(salutare("Matei"))


# [5] - Verificare Majorat ✅
def este_major(varsta):
    """
    este_major : Verifica daca o persoana este majora (minim 18 ani.)

    Args:
        varsta (int): varsta persoanei de verificat.

    Returns:
        string: Speficica daca persoana este majora.
    """
    try:
        return f"Persoana {"este" if varsta >= 18 else "nu este"} majora"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(este_major(18))


# [6] - Convertor valutar ✅
def conversie_eur_ron():
    """
    conversieEurRon : Realizeaza conversia EURO RON

    Returns:
        string_: string care ii arata ce suma in euro e convertita la cursul curent.
    """
    curs_eur = 5.08
    try:
        suma = float(input("Introduceti suma in RON de convertit \n"))
        euro = suma / curs_eur
        return f"{suma} LEI in Euro la cursul {curs_eur} este {euro:.2f} Euro"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(conversie_eur_ron())


# [7] - Manipulare String ✅
def manipulare_string():
    """
    manipulare_string: Foloseste functii simple, upper si title pentru a manipula un string.

    Returns:
        string: Numele in mai multe formate.
    """
    try:
        nume = input("Care este numele tau? \n")
        return f"Uite numele tau, {nume} in urmatoarele formate \n {nume.upper()} \n {nume.title()}"
    except AttributeError:
        return "Eroare. Introduceti un numar valid."


# print(manipulare_string())


# [8] - An Bisect ✅
def este_an_bisect(an):
    """
    este_an_bisect : Verifica daca un an este bisect.

    Args:
        an (int): Anul trebuie sa fie intreg.

    Returns:
        string: String de confirmare care spune daca anul este bisect sau nu.
    """
    try:
        return f"Anul {an} {"este" if an % 4 == 0 and an % 100 != 0 or an % 400 == 0 else "nu este"} bisect"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(este_an_bisect(2025))


# [9] - Comparator de numere ✅
def compara_numere(a, b):
    """
    compara_numere Compara doua numere.

    Args:
        a (int/float): valoarea primului numar.
        b (int/float): valoarea celui de-al doilea numar.

    Returns:
        string: string de confirmare in vederea numerelor comparate.
    """
    try:
        if a > b:
            return "Primul numar este mai mare."
        elif b > a:
            return "Al doilea numar este mai mare."
        else:
            return "Numerele sunt egale."
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(compara_numere(5, 5))


#  [10] - Calculator Salariu Orar ✅
def calculator_salariu():
    """
    calculator_salariu : Calculeaza salariul in functie de numarul de ore si rata orara.

    Returns:
        string: String care specifica salariul in functie de numarul de ore si rata orara.
    """
    try:
        ore_lucrate = float(input("Cate ore a lucrat seful? \n"))
        rata_orara = float(input("Care este rata pe ora? \n"))
        return f"Salariul pentru {ore_lucrate} ore lucrate si o rata orara de {rata_orara} este de {(ore_lucrate*rata_orara):.2f}"
    except ValueError:
        return "Eroare. Introduceti un numar valid."


# print(calculator_salariu())
