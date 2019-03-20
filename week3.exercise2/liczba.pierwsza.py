#ACDell\desktop \\
#  - UTC 8 -   \\

def libp(pierw):
    for a in range(2, pierw):
        if pierw % a == 0:  # można dodac and a!=1
            print(pierw, "nie jest liczba pierwsza")
            break
    else:
        print(pierw, 'jest liczbą pierwszą')


libp(89)