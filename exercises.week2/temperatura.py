# - user - \\
# - UTF -8 - \\
# - wprowadzamy dane \\

print('Wybierz jednostkę temperatury "c" lub "f" i naciśnij ENTER:')
j = str(input())
t = ("podaj temperaturę:")
j = j.lower()                              # zamienia wejściowe litery  małe ( nieważna jest wielkość liter)
if j == 'f' or j == 'c':
    print('Podaj temperaturę:')
    t = input()
    if j == 'c' and t.isdigit():
        print('Podaję temperaturę w stopniach Fahrenheit :', int(t) * 1.8 + 32,  'F')
        if j == 'f' and t.isdigit():
            print('Podaję temperaturę w stopniach Celcjusz :', (int(t) - 32) / 1.8, 'C')
    else:
        print('Błędne dane')
else:
    print('Błędne dane')
