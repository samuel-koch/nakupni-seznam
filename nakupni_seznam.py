# Funkce pro správu nákupního seznamu
def pridat_polozku(seznam): 
    polozka = input("Zadejte název položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")

def odebrat_polozku(seznam):
    polozka = input("Zadejte název položky k odebrání: ")
    if polozka in seznam:
        seznam.remove(polozka)
        print(f"Položka {polozka} byla odebrána.")
    else:
        print(f"Položka {polozka} se v seznamu nenachází.")

def zobrazit_seznam(seznam):
    print("Aktuální seznam položek:", seznam)

def seradit_seznam(seznam):
    seznam.sort()
    print("Seznam byl seřazen podle abecedy.", seznam)

def zobrazit_pocet_polozek(seznam):
    print(f"Počet položek v seznamu: {len(seznam)}")

def ukoncit_program():
    print("Program byl ukončen.")
    exit()

# Hlavní program
def hlavni_program():
    seznam = []
    while True:
        print("\nVyberte akci:")
        print("1 - Přidat položku")
        print("2 - Odebrat položku")
        print("3 - Zobrazit seznam")
        print("4 - Seřadit seznam")
        print("5 - Zobrazit počet položek")
        print("6 - Ukončit program")

        volba = input("Zadejte číslo akce: ")

        if volba == '1':
            pridat_polozku(seznam)
        elif volba == '2':
            odebrat_polozku(seznam)
        elif volba == '3':
            zobrazit_seznam(seznam)
        elif volba == '4':
            seradit_seznam(seznam)
        elif volba == '5':
            zobrazit_pocet_polozek(seznam)
        elif volba == '6':
            ukoncit_program()
        else:
            print("Zadejte číslo akce.")

# Spuštění hlavního programu
hlavni_program()
