# ACDell\pulpit\zadania1\\
# - UTC-8 \\
a = int(input("Podaj bok a: "))
print(a)
b = int(input("Podaj bok b: "))
print(b)
c = int(input("Podaj bok c: "))
print(c)
if c ** 2 == a ** 2 + b ** 2:
    print('Z podanych danych zbudujesz trójkąt pitagorejski, o przeciwprostokątnej =', c ** 2)
else:
    print('Z podanych danych nie zbudujesz trójkąta pitagorejskiego')