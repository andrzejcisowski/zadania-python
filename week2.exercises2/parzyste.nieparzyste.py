# AC Dell\\
#  - * - UTC-8 - * -
# policz parzyste / nieparzyste w zakresie

a = 0
b = 0
for liczba in range(0, 100):
    if liczba % 2 != 0:
        a = a+1
    else:
        b = b+1
print("parzyste: {}), nieparzyste :{}".format(a, b))


# wersja 2
a = 0
b = 0
print('podaj zakres')
podaj_zakres = int(input())
for liczba in range(int(podaj_zakres)):
    if liczba % 2 != 0:
        a = a+1
    else:
        b = b+1
print("parzyste : {}, nieparzyste :{}".format(a, b))