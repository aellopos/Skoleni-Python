# Samostatné cvičení 1

## 1 - Jednoduché podmínky
Založte si program **prihlaseni.py**. V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo. Pokud se heslo neshoduje s heslem simsalabim, vypište na výstup **Vstup nepovolen** a zavolejte funkci exit(), aby uživatel neznalý hesla nemohl s programem dál pracovat.

Na konec programu vlož příkaz, který se uživatele zeptá na věk. Pokud je uživatel starší 18 let, vypište na výstup **Smíš vstoupit** Pokud je mladší, vypiš **Vstup povolen od 18 let**

## 2 - Cena vstupenky

Vytvořte program **vstupenky01.py**, vytvořte si proměnnou plnaCena, do které uložte hodnotu 12.
Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel
- 0 euro pro návštěvníky mladší 6 let,
- 65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
- 100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
- 50% ze základní ceny pro ostatní (senior).
Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech. (využijte funkci round())

Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup.

## 3 - Registrace

Založte si program **registrace.py**. Program nechá uživatele, aby si zvolil uživatelské jméno a heslo. Heslo jej nechejte zadat dvakrát a ověřte, že jej uživatel zadal dvakrát stejně. V opačném případě vypište varování, že hesla nejsou stejná. Při prvním zadávání ověřte, že heslo je bezpečné, což v tomto případě znamená, že je delší než 8 znaků (využijte funkci len()).

## 4 - Házení kostkami
Napište program **kostky.py**, který bude simulovat hod dvěma klasickými šestistěnnými kostkami. Jeho výstupu bude součet bodů na těchto dvou kostkách.

Nápověda:

- Generování náhodných čísel dělá funkce random.randint().
- Pokud chcete ve vašem programu použít modul random, musíte na jeho úplném začátku napsat příkaz import random

## 5 - Generátor čísel
Napište program **generator.py**, který si od uživatele vyžádá dvě celá čísla - dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích.