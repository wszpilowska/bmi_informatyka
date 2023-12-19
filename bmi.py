def metric():
    m = float(input("Wpisz swoją wagę: "))
    h = float(input("Podaj swój wzrost: "))
    bmi = (m / h ** 2)
    bmif = round(bmi, 2)
    print("BMI wynosi:", bmif)
    bmis = status(bmif)
    print(bmis)
    txt(m, h, bmif, bmis)


def imperial():
    m = float(input("Wpisz swoją wagę:"))
    h = float(input("Podaj swój wzrost:"))
    bmi = (m/h**2)*703
    bmif = round(bmi, 2)
    print("Bmi wynosi:", bmif)
    bmis = status(bmif)
    print(bmis)
    txt(m, h, bmif, bmis)


def status(bmif):
    if bmif < 16:
        return "Wygłodzenie"
    elif 16 <= bmif < 16.99:
        return "Wychudzenie"
    elif 17 <= bmif < 18.49:
        return "Niedowaga"
    elif 18.5 <= bmif < 24.99:
        return "Pożądana masa ciała"
    elif 25 <= bmif < 29.99:
        return "Nadwaga"
    elif 30 <= bmif < 34.99:
        return "Otyłość 1 stopnia"
    elif 35 <= bmif < 39.99:
        return "Otyłość 2 stopnia"
    else:
        return "Otyłość 3 stopnia"


def txt(m, h, bmif, bmis):
    with open("bmi.txt", "a") as plik:
        plik.write(f"Waga: {m}, Wzrost: {h}, BMI: {bmif}, Status: {bmis}\n")


while True:
    a = int(input("Wpisz 1 jesli wybierasz system metryczny lub 2 jeśli wybierasz system imperialny:"))
    if a == 1:
        metric()
    elif a == 2:
        imperial()
    else:
        print("Błędne dane")
