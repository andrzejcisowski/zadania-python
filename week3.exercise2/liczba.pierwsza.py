#ACDell\desktop \\
#  - UTC 8 -   \\
# sposób 1

nr = int(input("Podaj liczbe "))

if nr >= 1:
    for i in range(2, nr):
        if (nr % i) == 0:
            print(nr, "nie jest liczbą pierwszą")
            print(i, "razy", nr // i, "jest", nr)
            break
    else:
        print(nr, "to jest liczba pierwsza")

#sposób z funkcją

"""def libp(pierw):

    for a in range(2, pierw):
        if pierw % a == 0: #można dodać warunek and a!=1:
            print(pierw, "nie jest liczba pierwsza")
            break
    else:
        print(pierw, 'jest liczbą pierwszą')
        #return libp(int(input('podaj liczbe: ')))
libp(wpisz liczbę,aby sprawdzić, czy jest liczbą pierwszą)"""
