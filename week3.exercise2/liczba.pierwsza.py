#ACDell\desktop \\
#  - UTC 8 -   \\

def libp(pierw):
    for a in range(2, pierw):
        if pierw % a == 0: #można dodać warunek and a!=1:
            print(pierw, "nie jest liczba pierwsza")
            break
    else:
        print(pierw, 'jest liczbą pierwszą')

print (libp(int(input('podaj liczbe: '))))

