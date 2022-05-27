from dataclasses import dataclass


class Osoba1:
    imie: str
    nazwisko: str
    wiek: int


a = Osoba1()
b = Osoba1()

a.imie = 'Ala'
print(a.imie)
#print(b.imie)
########

@dataclass
class Osoba2:
    imie: str
    nazwisko: str
    wiek: int
    oceny = []

a = Osoba2('Ala', 'Kowalska', 30)
a.oceny.append(1)
print(a)

b = Osoba2('Ola', 'Malinowska', 30)
b.oceny.append(2)
print(b)

print(b.oceny)
