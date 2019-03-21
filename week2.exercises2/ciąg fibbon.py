# ACDell\user\desktop\\
# -UTF - 8 \\

a, b = (0, 1)    #start - cyfry pierwsze w ciągu\\
n = int(input("Podaj zakres, do jakiego obliczymy ciąg  : "))
while b < n:
    if n > 10000:                              # ograniczenie przed zapętleniem - wykonanie do 10000\\
        print('przekroczyłeś zakres')
        break
    else:
        a, b = b, a + b
    print(b)


