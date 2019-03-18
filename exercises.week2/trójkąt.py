# ACDell\pulpit\zadania1\\
# - UTC-8 \\
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

if c ** 2 == a ** 2 + b ** 2:
    print('Z podanych danych zbudujesz trójkąt pitagorejski, o przeciwprostokątnej =', c ** 2)
    if a == 3 and b == 4 and c == 5:
        print('Brawo, z wprowadzonych danych zbudujesz trójkąt egipski')
else:
        print('Z podanych danych nie zbudujesz trójkąta pitagorejskiego')