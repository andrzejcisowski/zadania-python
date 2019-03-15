# rok przestępny lub nie //

year = input("Podaj rok")
if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Rok przestępny")
    else:
        print("Nie jest przestępny")