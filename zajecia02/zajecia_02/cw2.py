import this
# Zadanie 6
dane = (2024, 'Python', 3.8)
rok, język, wersja = dane


print("Rok:", rok)
print("Język:", język)
print("Wersja:", wersja)
# Zadanie 7
oceny = [4, 3, 5, 2, 5, 4]

pierwsza = oceny[0]
ostatnia = oceny[-1]
srodek = oceny[1:-1]

print("Pierwsza: ", pierwsza)
print("Ostatnia: ", ostatnia)
print("Środkowe: ", srodek)

# Zadanie 8
info = ('Jan', 'Kowalski', 40, 'Polska', 'malarz')

imie, nazwisko,* _, zawod = info

print("Imię:", imie)
print("Nazwisko:", nazwisko)
print("Zawód:", zawod)

# Zadanie 9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, (jezyk, wersja, (opis,_)) = dane

print("Rok:", rok)
print("Nazwa języka:", jezyk)
print("Wersja:", wersja)
print("Opis wersji:", opis)
# Zadanie 10

a = b = [1, 2, 3]

b[0] = 'zmieniono'

print("Lista a:", a)
print("Lista b:", b)
# tak są obiektami mutowalnymi (Dlatego się oba zmieniły)

# Zadanie 11

a = b = [1, 2, 3]
c = list(a)  

c[0] = 'nowa wartość'

print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
#tworzy nowa liste w pamieci i dzieki temu nie wpływa ona na pamieci, która jest wykorzystana dla a i b

#Zadanie 12

x = y = 10

y += 1

print("x:", x)
print("y:", y)

# poprzez dodanie do zmiennej y+1 tworzymy nowego integera z wartosia 11

#Zadanie 13
K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print("K:", K)
print("L:", L)
print("M:", M)
print("N:", N)

#Zadanie 14

imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3, 2]

pary = zip(imiona, oceny)

for imie, ocena in pary:
    print(f"{imie}: {ocena}")

# Zadanie 15
liczby=[1,2,3,4,5]
def kwadrat(x):
    return x**2

kwadraty=list(map(kwadrat, liczby))
print(kwadraty)

#Zadanie 16
def zmien_wartosc(arg):
    if isinstance(arg,list):
        arg[0]="dzem"
    if isinstance(arg,int):
        arg=102349

liczba = 10
lista = [1, 2, 3]

zmien_wartosc(liczba)
zmien_wartosc(lista)

print(liczba)  # Output: 10
print(lista)  

#lista sie zmienia a integer nie 

# Zadanie 17
#szczerze naprawde nie mam pojecia o co chodzi w tym zadaniu,
#jak w funkcji które jest wyko

# def zamowienie_produktu(nazwa_produktu,*,cena,ilosc=1):
#     pass
#     if zamowienia !=None:
#         for i in len(zamowienia):
#             suma=suma+zamowienia[i[cena*ilosc]]
#     print(suma)
    
#     return f"Nazwa produktu: {nazwa_produktu}, Wartosc zamowienia: {cena*ilosc}, Ilość: {ilosc}"


# products = [
#     {'Nazwa Produktu': 'Jablko', 'ilosc': 2, 'cena': 10},
#     {'Nazwa Produktu': 'gruszka', 'ilosc': 3, 'cena': 5},
#     {'Nazwa Produktu': 'banan', 'ilosc': 1, 'cena': 20},
# ]

# zamowienia = [zamowienie_produktu(produkt['Nazwa Produktu'], produkt['cena'], produkt['ilosc']) for produkt in products]

# # lista_zakupow=list()
# # lista_zakupow[0]=zamowienie_produktu("jablko",cena=10,ilosc=25)
# # lista_zakupow[1]=zamowienie_produktu("sliwka",cena=3,ilosc=3)
# # lista_zakupow[2]=zamowienie_produktu("pomarancza",cena=2,ilosc=10)
# print(zamowienia)

#Zadanie 18

def stworz_raport(*args, **kwargs):
    for id_produktu in args:
        print(f"Informacje o produkcie o ID {id_produktu}:")
        for key, value in kwargs.items():
            if str(id_produktu) in key:
                print(f"{key.split('_')[0]}: {value}")

stworz_raport(101, 102, nazwa_101='Kubek termiczny', cena_101='45.99 zł', nazwa_102='Długopis', cena_102='4.99 zł')

#Zadanie 19
def stworz_funkcje_potegujaca(wykladnik):

    def poteguj(podstawa):
        return podstawa ** wykladnik

    return poteguj

# Example usage
potega_2 = stworz_funkcje_potegujaca(2)
potega_3 = stworz_funkcje_potegujaca(3)

print(potega_2(4))  # Output: 25
print(potega_3(5))  # Output: 125



#Zadanie 21
from typing import Callable

def licznik_funkcja() -> Callable[[], int]:
    if not hasattr(licznik_funkcja, 'count'):
        licznik_funkcja.count= 0

    def inner() -> int:
        licznik_funkcja.count += 1
        return licznik_funkcja.count

    return inner

counter = licznik_funkcja()
for i in range(10):
    print(counter())


#Zadanie 22

ksiazki = [
    {'tytul': 'Książka 1', 'autor': 'Autor 1', 'rok_wydania': 2005},
    {'tytul': 'Książka 2', 'autor': 'Autor 2', 'rok_wydania': 2002},
    {'tytul': 'Książka 3', 'autor': 'Autor 3', 'rok_wydania': 2010},
    {'tytul': 'Książka 4', 'autor': 'Autor 4', 'rok_wydania': 1999},
]
#a
# ksiazki_sorted = sorted(ksiazki,lambda x: x['rok_wydania'])

# print(ksiazki_sorted)

#b
# ksiazki_filterred=filter(lambda x: x['rok_wydania'] > 2000, ksiazki)
# ksiazki_filterred=list(ksiazki_filterred)
# print(ksiazki_filterred)

#c
ksiazki_tytuly = map(lambda x: x['tytul'], ksiazki)

ksiazki_tytuly = list(ksiazki_tytuly)

print(ksiazki_tytuly)

#Zadanie 23

def days_of_week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

for day in days_of_week():
    print(day)


days = days_of_week()
first_three_days = [next(days) for _ in range(3)]
print(first_three_days)


from itertools import islice

days = days_of_week()
first_three_days = list(islice(days, 3))
print(first_three_days)