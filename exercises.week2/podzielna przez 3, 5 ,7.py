# - user - \\
# - UTF -8 - \\
print('Podaj liczbę')
cyfra = input()
if cyfra.isdigit():
    cyfra = int(cyfra)
    if cyfra % 3 == 0:
        print('podana liczba jest podzielna przez 3')
    if cyfra % 5 == 0:
        print('Podana liczba jest podzielna przez 5')
    if cyfra % 7 == 0:
        print('Podana liczba jest podzielna przez  7')
    else:
        print('Podana liczba nie jest podzielna przez 3,5  lub 7')

# wersja krótsza\\
#print('Podaj liczbę')
#cyfra = input()
#if cyfra.isdigit():
 #   cyfra = int(cyfra)
 #   if cyfra % 3 == 0 or cyfra % 5 == 0 or cyfra % 7 == 0:
 #       print('Podana liczba jest podzielna przez 3, 5 lub 7')
#else:
 #   print('Podana liczba nie jest podzielna przez 3 , 5 i 7')

