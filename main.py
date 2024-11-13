# Inițializăm lista de cheltuieli
cheltuieli = []

# Funcția pentru adăugarea unei cheltuieli
def adauga_cheltuiala(cheltuieli):
    while True:
        try:
            suma = int(input("Introdu o suma: "))
            if suma <= 0:
                raise ValueError("Suma trebuie sa fie strict pozitiva!")
            descriere = input("Introdu o descriere: ")
            cheltuiala = {"suma": suma, "descriere": descriere}
            cheltuieli.append(cheltuiala)
            print("Cheltuiala a fost adăugată cu succes!")
            break
        except ValueError as e:
            print(e)
    return cheltuieli

# Funcția pentru afișarea cheltuielilor
def afiseaza_cheltuieli(cheltuieli):
    if not cheltuieli:
        print("Nu exista cheltuieli inregistrate!")
    else:
        print("\nLista cheltuielilor:")
        for i, item in enumerate(cheltuieli, start=1):
            print(f"{i}. Suma: {item['suma']} lei, Descriere: {item['descriere']}")
    return

# Funcția pentru calcularea sumei totale a cheltuielilor
def calculeaza_total(cheltuieli):
    if not cheltuieli:
        print("Nu exista cheltuieli inregistrate!")
    else:
        suma_totala = sum(item['suma'] for item in cheltuieli)
        print(f"Totalul cheltuielilor este: {suma_totala} lei")
    return

# Funcția pentru ștergerea unei cheltuieli pe baza descrierii
def sterge_cheltuiala_dupa_descriere(cheltuieli):
    descriere_de_sters = input("Introdu descrierea cheltuielii pe care vrei sa o stergi: ")
    cheltuieli_initiale = len(cheltuieli)
    cheltuieli[:] = [item for item in cheltuieli if item['descriere'] != descriere_de_sters]
    if len(cheltuieli) < cheltuieli_initiale:
        print(f"Cheltuielile cu descrierea '{descriere_de_sters}' au fost șterse.")
    else:
        print("Nu există cheltuieli cu descrierea introdusă.")
    return

# Funcția pentru modificarea unei cheltuieli după index
def modifica_cheltuiala(cheltuieli):
    try:
        index = int(input("Introdu indexul cheltuielii pe care vrei să o modifici: ")) - 1
        if index not in range(len(cheltuieli)):
            print("Indexul nu este corespunzător!")
            return
        suma_noua = int(input("Introdu noua suma, strict pozitiva: "))
        if suma_noua <= 0:
            print("Suma trebuie sa fie un numar strict pozitiv!")
            return
        descriere_noua = input("Introdu noua descriere: ")
        cheltuieli[index] = {"suma": suma_noua, "descriere": descriere_noua}
        print("Cheltuiala a fost modificată cu succes!")
    except ValueError:
        print("Eroare de introducere! Asigură-te că ai introdus valori numerice pentru suma și index.")
    return cheltuieli

while True:
    print("\n--- Meniu Gestionare Cheltuieli ---")
    print("1. Adaugă o cheltuială")
    print("2. Afișează cheltuielile")
    print("3. Calculează totalul cheltuielilor")
    print("4. Șterge o cheltuială după descriere")
    print("5. Modifică o cheltuială după index")
    print("6. Ieșire din program")

    alegerea = input("Alegerea ta este: ")

    if alegerea == "1":
        adauga_cheltuiala(cheltuieli)
    elif alegerea == "2":
        afiseaza_cheltuieli(cheltuieli)
    elif alegerea == "3":
        calculeaza_total(cheltuieli)
    elif alegerea == "4":
        sterge_cheltuiala_dupa_descriere(cheltuieli)
    elif alegerea == "5":
        modifica_cheltuiala(cheltuieli)
    elif alegerea == "6":
        print("La revedere!")
        break
    else:
        print("Eroare de introducere! Te rog să alegi o opțiune validă.")

