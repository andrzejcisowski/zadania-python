# AC Dell\\
#  - * - UTC-8 - * -
# policz parzyste / nieparzyste w zakresie

a = 0
b = 0
for liczba in range(100):
    if liczba % 2 != 0:
        a = a+1
    else:
        b = b+1
print("parzyste: {}), nieparzyste :{}".format(a, b))


# wersja 2
a = 0
b = 0
podaj_zakres = (input('Podaj zakres :'))
if podaj_zakres.isdigit():
    for liczba in range(int(podaj_zakres)):
        if liczba % 2 != 0:
            a += 1
        elif liczba % 2 == 0:
            b += 1
    print("parzyste : {}, nieparzyste :{}".format(a, b))
else:
    print('Niepoprawne dane , wprowadź cyfry :')
