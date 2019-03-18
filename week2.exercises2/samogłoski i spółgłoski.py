#ACDell\pulpit\zadania \\
# - UTC - 8
#liczba samogłosek i spółgłosek

samogloski = 0
spolgloski = 0
print('wpisz słowo i naciśnij enter:')

for litera in input():
    if litera.lower() in ('aeioyu'):
        samogloski = samogloski + 1
    else:
        spolgloski += 1
print(f"Samoglosek: {samogloski}, spolglosek {spolgloski}")