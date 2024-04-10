class MiejsceNieistniejace(Exception):
    def __init__(self, wiadomosc="Podane miejsce nie istnieje w sali kinowej."):
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)

class MiejsceZajete(Exception):
    def __init__(self, wiadomosc="To miejsce jest już zarezerwowane."):
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)

class BrakWolnychMiejsc(Exception):
    def __init__(self, wiadomosc="Nie ma wolnych miejsc na seans."):
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)

class TeSameRezerwacje(Exception):
    def __init__(self, wiadomosc="Ten sam użytkownik nie może zarezerwować więcej niż jednego miejsca."):
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)

class SalaKinowa:
    def __init__(self, szerokosc, dlugosc):
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc
        self.sala = {}

        for i in range(0,dlugosc):
            for j in range(0,szerokosc):
                self.sala[f'{i}{j}'] = None

    def rezerwuj(self, miejsce, rezerwant):
        try:
            wolne_miejsce = sum(1 for seat, user in self.sala.items() if user is None)
            
            if wolne_miejsce == 0:
                raise BrakWolnychMiejsc()
            if miejsce not in self.sala:
                raise MiejsceNieistniejace()
            if self.sala[miejsce] is not None:
                raise MiejsceZajete()
            
            
            for seat, user in self.sala.items():
                if user == rezerwant:
                    raise TeSameRezerwacje()
                
            self.sala[miejsce] = rezerwant
            print(f"Miejsce {miejsce} zostało zarezerwowane przez {rezerwant}.")
        
        except (MiejsceNieistniejace, MiejsceZajete, BrakWolnychMiejsc, TeSameRezerwacje) as e:
            print(f"Wystąpił błąd: {e}")


sala = SalaKinowa(2, 2)
sala.rezerwuj('01', 'Kowalski')
sala.rezerwuj('77', 'Nowak')
sala.rezerwuj('01', 'Nowak')
sala.rezerwuj('00', 'Grzechynia')
sala.rezerwuj('10', 'Kurski')
sala.rezerwuj('11', 'Pawlowicz')
sala.rezerwuj('11', 'Niedojda')
sala.rezerwuj('10', 'Skarpeta')