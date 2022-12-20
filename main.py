import os

options = ['Dodawanie', 'Odejmowanie', 'Mnożenie', 'Dzielenie', 'Potęgowanie', 'Silnia', 'Wyjście']
exit = False

### checking if input string can be converted to float
def can_convert_to_float(string):
    try:
        result = float(string)
        return True
    except ValueError:
        return False

### checking if input string can be converted to int
def can_convert_to_int(string):
    try:
        result = int(string)
        return True
    except ValueError:
        return False

## funkcja obliczajaca silnie
def silniaZ(liczba):
    wynik = 1
    for i in range(liczba):
        if i == 0: return
        wynik = wynik * i

    return wynik

### menu function
def menu():
    os.system('cls')
    print('*****')
    print('Jan Mager K23, id: 120117')
    print('*****')
    print('Kalkulator 2022')
    print('*****')
    print('MENU')
    print('*****')

    for index in range(len(options)): print("%s. %s" % (index+1, options[index]))

    inputOk = False
    print('*****\nWybierz opcję z MENU\nwprowadzając odpowiednią liczbę,\na potwierdź ENTER: ')
    while not inputOk:
        menuChoose = input()
        if(menuChoose.isdigit() and (int(menuChoose) >= 1 and int(menuChoose) <= len(options))): inputOk = True
        else: print("###\nWprowadź liczbę z zakresu 1 do %s\n###" % (len(options)))
    return menuChoose

### dodawanie
def dodawanie():
    os.system('cls')
    print('*****')
    print('Wybrałeś dodawanie')
    print('*****')

    firstNum = input('Podaj pierwszą liczbę: ')
    while not can_convert_to_float(firstNum):
        firstNum = input('Podaj poprawną liczbę: ')
    secondNum = input('Podaj drugą liczbę: ')
    while not can_convert_to_float(secondNum):
        secondNum = input('Podaj poprawną liczbę: ')

    ### print wynik dodawania
    os.system('cls')
    print('*****')
    print('Wynik twojego dodawania:')
    print("%s + %s = %s" % (firstNum, secondNum, float(firstNum) + float(secondNum)))

### odejmowanie
def odejmowanie():
    os.system('cls')
    print('*****')
    print('Wybrałeś odejmowanie')
    print('*****')

    firstNum = input('Podaj pierwszą liczbę: ')
    while not can_convert_to_float(firstNum):
        firstNum = input('Podaj poprawną liczbę: ')
    secondNum = input('Podaj drugą liczbę: ')
    while not can_convert_to_float(secondNum):
        secondNum = input('Podaj poprawną liczbę: ')

    ### print wynik odejmowania
    os.system('cls')
    print('*****')
    print('Wynik twojego odejmowania:')
    print("%s - %s = %s" % (firstNum, secondNum, float(firstNum) - float(secondNum)))

### mnozenie
def mnozenie():
    os.system('cls')
    print('*****')
    print('Wybrałeś mnożenie')
    print('*****')

    firstNum = input('Podaj pierwszą liczbę: ')
    while not can_convert_to_float(firstNum):
        firstNum = input('Podaj poprawną liczbę: ')
    secondNum = input('Podaj drugą liczbę: ')
    while not can_convert_to_float(secondNum):
        secondNum = input('Podaj poprawną liczbę: ')

    ### print wynik mnozenia
    os.system('cls')
    print('*****')
    print('Wynik twojego mnożenia:')
    print("%s * %s = %s" % (firstNum, secondNum, float(firstNum) * float(secondNum)))

### dzielenie
def dzielenie():
    os.system('cls')
    print('*****')
    print('Wybrałeś dzielenie')
    print('*****')

    firstNum = input('Podaj pierwszą liczbę: ')
    while not can_convert_to_float(firstNum):
        firstNum = input('Podaj poprawną liczbę: ')
    secondNum = input('Podaj drugą liczbę: ')
    while not can_convert_to_float(secondNum):
        secondNum = input('Podaj poprawną liczbę: ')

    ### print wynik dzielenia
    os.system('cls')
    print('*****')
    print('Wynik twojego dzielenia:')
    print("%s / %s = %s" % (firstNum, secondNum, float(firstNum) / float(secondNum)))

### potegowanie
def potegowanie():
    os.system('cls')
    print('*****')
    print('Wybrałeś potegowanie')
    print('*****')

    firstNum = input('Podaj liczbę, którą chcesz podnieść do potęgi: ')
    while not can_convert_to_int(firstNum):
        firstNum = input('Podaj poprawną liczbę: ')
    secondNum = input('Do której potęgi podnieść liczbę %s?: ' % (firstNum))
    while not can_convert_to_int(secondNum):
        secondNum = input('Podaj poprawną liczbę: ')

    ### print wynik potegowania
    os.system('cls')
    print('*****')
    print('Wynik twojego potęgowania:')
    print("%s do potęgi %s = %s" % (firstNum, secondNum, float(firstNum) ** float(secondNum)))

### silnia
def silnia():
    os.system('cls')
    print('*****')
    print('Wybrałeś silnię')
    print('*****')

    firstNum = input('Podaj liczbę, z której chcesz obliczyć silnię (max 10): ')
    while not can_convert_to_int(firstNum) or int(firstNum) > 10:
        firstNum = input('Podaj poprawną liczbę: ')

    ### print wynik dzielenia
    os.system('cls')
    print('*****')
    print('Wynik twojej silni:')
    print("%s! = %s" % (firstNum, silniaZ(int(firstNum))))

### start program
while not exit :
    os.system('cls')

    wyborUsera = menu()
    wyborUsera = int(wyborUsera)

    if wyborUsera == 1: dodawanie()
    elif wyborUsera == 2: odejmowanie()
    elif wyborUsera == 3: mnozenie()
    elif wyborUsera == 4: dzielenie()
    elif wyborUsera == 5: potegowanie()
    elif wyborUsera == 6: silnia()
    elif wyborUsera == len(options): exit = True
    else:
        print('Brak przypisanego programu')

    print('*****')
    if not exit: input('Wciśnij ENTER aby otworzyć ponownie MENU.')
    else: print('Zamknięto kalkulator.')
