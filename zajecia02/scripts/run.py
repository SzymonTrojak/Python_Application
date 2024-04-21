import sys
import os
parent_path = os.path.dirname(sys.path[0])
sys.path.append(parent_path)
from zajecia_02.liczniki_stanu import licznik_atrybut, licznik_class, licznik_globalny, licznik
from zajecia_02 import cw2 as c
inkrementacja = licznik.licznik()
print(inkrementacja()) 
print(inkrementacja())  

print(licznik_globalny.licznik_globalny())  
print(licznik_globalny.licznik_globalny())  

licznik_instancji = licznik_class.Licznik()
print(licznik_instancji())
print(licznik_instancji()) 

print(licznik_atrybut.licznik_atrybut())  
print(licznik_atrybut.licznik_atrybut())

print(f'rok :{c.rok}, jezyk :{c.jezyk}, wersja :{c.wersja}')
print(f'pierwsza :{c.pierwsza}, srodek: {c.srodek}, wersja: {c.ostatnia}')
print(f'imie :{c.imie}, nazwisko: {c.nazwisko}, zawod: {c.zawod}')
print(f'rok :{c.rok}, jezyk: {c.jezyk}, wersja: {c.wersja}, opis: {c.opis}')
print(f'pary :{c.pary}')
print("Wartość przed wykonaniem funkcji:", c.lista)
print("Wartość po wykonaniu funkcji:", c.zmien_wartosc(c.lista))
c.stworz_raport(101, 102, nazwa_101='Kubek termiczny', cena_101='45.99 zł', nazwa_102='Długopis', cena_102='4.99 zł')
potega_2 = c.stworz_funkcje_potegujaca(2)

#Wywołanie funkcji potęgującej do kwadratu
print(potega_2(4)) 
print(c.licznik())  
print(c.licznik())  