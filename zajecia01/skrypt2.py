import random
import math
import json
import os
# wartosc=100
# dodawanie=wartosc+123.15
# potega=dodawanie**12
# tekst = str(potega)
# wartosc_pi=math.pi
# losowa=random.choice([1, 2, 3, 4, 5])
# tekst = f"Wartosc: {tekst}"
# # print(len(tekst))
# art_index = tekst.find("art")
# if art_index != -1:
#     print(tekst[art_index:art_index + 3])
# else:
#     print("NIC")

# # # print(dir(tekst))
# # # tekst.upper()
# # # print(tekst.upper())
# # # tekst[2]='p'

# lista=list(tekst)
# # print(lista)
# lista = lista[:lista.index(':')] + [':']
# # print(lista)
# nowa_lista = [1, 2, 3, 4, 5]
# lista.append(nowa_lista)
# lista.remove(':')
# print(lista)


# lista2 = [1, 2, 3, "banan", 100]
# lista3 = [x**2 for x in lista2 if x != "banan"]
# lista4 = list(range(2, 17, 2))

# print("Lista2: ", lista2)
# print("Lista3: ", lista3)
# print("Lista4: ", lista4)

# ja: {}

# ja = {
#     "imie": "Jan",
#     "nazwisko": "Kowalski",
#     "wiek": 30,
#     "rodzice": [
#         {
#             "imie": "Adam",
#             "wiek": 60
#         },
#         {
#             "imie": "Ewa",
#             "wiek": 55
#         }
#     ]
# }

# print(ja["rodzice"])
# print(ja["rodzice"][0]["imie"])
# for key in ja.keys():
#     print("Klucz: ", key)

# rodzenstwo = 'rodzenstwo' in ja
# print( bool(rodzenstwo))

# #krotki

# krotka1 = (1, 2, "3", 4, 2, 5)

# print("Długość: ", len(krotka1))
# print("Pierwszy wyraz: ", krotka1[0])

# ile_razow = krotka1.count(2)
# print("Wartosc 2 wystepuje ", ile_razow ,"razy")

# # try:
# #     krotka1[0] = 2
# # except TypeError as e:
# #     print(e)
# # print("Krotka1: ", krotka1)

# # ZBIORY

# X = set("kalarepa")
# Y = set("lepy")

# wspolna = X & Y
# print("X i Y: ", wspolna)

#Instrukcje
#zadanie 1
# imiona = ["Jan", "Anna", "Tomasz", "Maria", "Wojciech"]

# for i, imie in enumerate(imiona):
#     print(f"Indeks: {i}; Imię: {imie}")

# #Zadaine 2
# #a 
# liczba=int(input("prosze wpisac liczbę: "))
# if liczba > 0 and liczba % 2 == 0:
#     print("Liczba jest dodatnia i parzysta")

# #b
# if liczba != 0:
#     print("Liczba jest różna od zera")
# #c
#     owocki = ['jabłko', 'banan', 'pomarańcza']
# owoce = str(input("wporwadz nazwę owocu: "))
# if owoce not in owocki:
#     print("Owoc nie jest dostępny")
# else:
#     print("Owoc jest dostępny")

# Zdanie 3
# suma=0
# while suma<100:
#     number=int(input("Proszę podaj liczbę"))
#     suma+=number
# print(suma)

# Dziwactwa
# #1. Przypisanie tworzy referencje, a nie kopie
# L = [1,2,3,4]
# M = [1,2,3,L,4]
# print(f"Wartość zmiennej M przed zmianą L: {M}")
# L[1] = "woooow"
# print(f"Wartość zmiennej M po zmianie L: {M}")
# #2. Powtórzenie dodaje jeden poziom zagłębienia
# L = [4,5,6]
# X = L * 4
# Y = [L] * 4
# print(f"X: {X}, Y: {Y}")
# L[1] = "wow"
# print(f"X: {X}, Y: {Y}")
# L = [4,5,6]
# Y = [list(L)] * 4
# L[1] = "wow"
# print(f"Y: {Y}")
# Y[0][1] = "wow"
# print(f"Y: {Y}")

#Zadanie sprawdzajace

sciezka = "C:/Users/szymo/6_semestr/Python_application/zajecia01/zajecia01/teksty.json"  

with open(sciezka, 'r') as f:
    content = f.read().lower()

punctuation = ['.', ',']
for p in punctuation:
    content = content.replace(p, ' ')

words = [word for word in content.split() if 'a' in word or 'a' in word.upper()]

words = [''.join(word[:-1] + word[-1].upper()) for word in words]

unique_words = set(words)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

data = {
    'words': list(words),
    'unique_words': list(unique_words),
    'word_count': word_count
}

with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)