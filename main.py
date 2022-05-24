from pickle import TRUE


class Biblioteka:
    wypozyczone = []

    def wypozycz(tytul, nazwisko):
        for i in range(len(Ksiazka.ksiazki)):
            if Ksiazka.ksiazki[i][0] == tytul and Ksiazka.ksiazki[i][2] > 0:
                Ksiazka.ksiazki[i][2] -= 1
                Biblioteka.wypozyczone.append([nazwisko, tytul])
                return True
            else: 
                return False
    
    def oddaj(tytul, nazwisko):
        for i in range(len(Biblioteka.wypozyczone)):
            if Biblioteka.wypozyczone[i][0] == nazwisko and Biblioteka.wypozyczone[i][1] == tytul:
                Biblioteka.wypozyczone.pop(i)
                for j in range(len(Ksiazka.ksiazki)):
                    if Ksiazka.ksiazki[j][0] == tytul:
                        Ksiazka.ksiazki[i][2] += 1
                return True
        return False

class Czytelnik:
    czytelnicy = []
    
    def __init__(self, nazwa, licznik):
        self.nazwa = nazwa
        self.licznik = licznik

    def sprawdz_dostpenosc(tytul):
        pass

    


class Ksiazka:
    ksiazki = []
    def __init__(self, tytul, autor, liczba_sztuk = 1):
        self.tytul = tytul
        self.autor = autor
        self.liczba_sztuk = liczba_sztuk

    def __repr__(self):
        return f"('{self.tytul}', '{self.autor}', {self.liczba_sztuk})"
    
    def sprawdz_ksiazke(nazwa, tworca):
            if Ksiazka.ksiazki != []:

                for i in range(len(Ksiazka.ksiazki)):
                    if Ksiazka.ksiazki[i][0] == nazwa:
                        Ksiazka.ksiazki[i][2] += 1
                        break
                    elif Ksiazka.ksiazki[i][0] != nazwa and i+1 == len(Ksiazka.ksiazki):
                        Ksiazka.ksiazki.append([nazwa, tworca, 1])
                        
            else:
                Ksiazka.ksiazki.append([nazwa, tworca, 1])      

class Egzemplarz():
    def __init__(self, tytul, autor, rok):
        self.rok = rok
        self.tytul = tytul
        self.autor = autor
        Ksiazka.sprawdz_ksiazke(self.tytul, self.autor)

        
    def __repr__(self):
        return f"('{self.tytul}', '{self.autor}', {self.rok})"

n = input()
n = int(n)
for i in range(n):
    x = eval(input())
    if x[0] == "dodaj":
        Egzemplarz(x[1],x[2],x[3])
    elif x[0] == "wypozycz":
        Biblioteka.wypozycz(x[2],x[1])
    elif x[0] == "oddaj":
        Biblioteka.oddaj(x[2],x[1])
# Ksiazka.ksiazki = sorted(Ksiazka.ksiazki, key=lambda x: x[0])
# # for i in range(len(Ksiazka.ksiazki)):
# #     print(Ksiazka(Ksiazka.ksiazki[i][0],Ksiazka.ksiazki[i][1],Ksiazka.ksiazki[i][2]))
# print(Biblioteka.wypozycz("Quo Vadis ", " Henryk Sienkiewicz "))
# print(Biblioteka.oddaj("Quo Vadis ", " Henryk Sienkiewicz "))
# print(Biblioteka.oddaj("Quo Vadis ", " Henryk Sienkiewicz "))
# for i in range(len(Ksiazka.ksiazki)):
#     print(Ksiazka(Ksiazka.ksiazki[i][0],Ksiazka.ksiazki[i][1],Ksiazka.ksiazki[i][2]))





        

        
