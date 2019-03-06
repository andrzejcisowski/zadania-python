# ACDell\pulpit\zadania1\\
# - UTC-8 \\
range(101)
print('"NIE DZIELIMY ZERA"')            # dla 0 zwróci fizz,buzz,FizzBuzz\\
for liczba in range(1, 101):            # wartość  w przedziale 1-100\\
    if liczba % 3 == 0:               # liczba podzielna przez 3 bez reszty\\
        print(liczba, "fizz")
    if liczba % 5 == 0:
        print(liczba, 'buzz')
    if liczba % 3 == 0 and liczba % 5 == 0:
        print(liczba, "=", 'FizzBuzz')
else:
        print("'Nie dzielimy zera'")
