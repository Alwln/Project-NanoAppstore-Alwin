from lastversionGalgje import introductie
from lastversionNummerspel import raad_het_nummer

def show_menu():
    print("     =======Welkom bij de Nano Appstore!=======")
    print("               1. Speel Nummerspel ")
    print("               2. Speel Galgje ")
    print("               3. Afsluiten")

def main():
    while True:
        show_menu()
        keuze = input("     ===========Maak je keuze: ================\n                      ")

        if keuze == '1':
            raad_het_nummer()  # Start het Nummerspel
        elif keuze == '2':
            introductie()      # Start Galgje
        elif keuze == '3':
            print("Bedankt voor het gebruiken van de Nano Appstore!")
            break  # Stop het programma
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main()



