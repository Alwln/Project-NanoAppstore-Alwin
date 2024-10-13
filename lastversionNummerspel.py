import random

# Functie voor het spel "Raad het Nummer"
def raad_het_nummer():
    while True:
        print('             Welkom bij Raad het Nummer! Kies een moeilijkheidsgraad:')
        print('                      ----- 1. Makkelijk (tussen 1 en 20) -----')
        print('                      ----- 2. Gemiddeld (tussen 1 en 100) -----')
        print('                      ----- 3. Moeilijk (tussen 1 en 500) -----')
        print('                      ----- 4. Helderziend (tussen 1 en 1000, 1 gok) -----')
        print('                      ----- 5. Terug naar het hoofdmenu -----\n')

        moeilijkheid = input('                       Voer de moeilijkheidsgraad in (1-5): ')

        if moeilijkheid == '1':
            max_nummer = 20
            aantalGeraden = 8
            print(f'Je hebt {aantalGeraden} beurten om het nummer te raden.')
        elif moeilijkheid == '2':
            max_nummer = 100
            aantalGeraden = 8
            print(f'Je hebt {aantalGeraden} beurten om het nummer te raden.')
        elif moeilijkheid == '3':
            max_nummer = 500
            aantalGeraden = 5
            print(f'Je hebt {aantalGeraden} beurten om het nummer te raden.')
        elif moeilijkheid == '4':
            max_nummer = 1000
            aantalGeraden = 1
            print('Je hebt 1 gok om het nummer te raden.')
        elif moeilijkheid == '5':
            print("Terug naar het hoofdmenu...")
            return  # Stop de functie om terug te gaan naar het hoofdmenu
        else:
            print('Ongeldige keuze! Kies een getal tussen 1 en 5.')
            continue  # Herhaalt de loop als de keuze ongeldig is

        # Genereert een willekeurig getal tussen 1 en max_nummer
        antwoord = random.randint(1, max_nummer)

        count = 0  # Telt het aantal geraden pogingen

        # Loop voor het raden van het nummer
        while True:
            # Vraag de speler om een gok te doen
            userGuess = int(input(f'Welk getal denk je dat ik in gedachte heb? (tussen 1 en {max_nummer}): '))

            # Controle of het geraden getal binnen de toegestane grenzen ligt
            if userGuess < 1 or userGuess > max_nummer:
                print(f'Ongeldig getal! Kies een getal tussen 1 en {max_nummer}.')
                continue  # Herhaalt de loop als het getal ongeldig is

            count += 1  # Verhoogt het aantal geraden pogingen

            # Geeft informatie over het aantal resterende beurten
            if moeilijkheid != '4':
                aantalGeraden -= 1
                print('Je kan nog', aantalGeraden, 'x raden')
            else:
                # Als het helderziend niveau is, zijn er geen herhalingen
                aantalGeraden = 0  # Er is maar 1 gok

            # Controleert of de speler alle beurten heeft gebruikt
            if aantalGeraden < 0 or (moeilijkheid == '4' and count == 1):
                print('Je hebt het getal niet geraden, je bent af.')
                print('Het juiste getal was:', antwoord)
                break  # Stop het huidige spel om opnieuw te kunnen beginnen

            # Geeft aan of het getal kleiner of groter is dan het geraden getal
            elif antwoord < userGuess:
                print('Het getal is kleiner.')
            elif antwoord > userGuess:
                print('Het getal is groter.')

            # Als de speler het juiste nummer raadt
            elif antwoord == userGuess:
                print('Je hebt het getal geraden! Gefeliciteerd!')
                print('Je hebt het in', count, 'beurten geraden.')
                break  # Stop het huidige spel om opnieuw te kunnen beginnen

        # Vraag de speler of hij/zij opnieuw wil spelen
        while True:
            opnieuw_spelen = input('Wil je het spel opnieuw spelen of terug naar het hoofdmenu? (ja/nee): ').lower()
            if opnieuw_spelen == 'ja':
                break  # Herstart de outer loop om opnieuw te spelen
            elif opnieuw_spelen == 'nee':
                print("Terug naar het hoofdmenu...")
                return  # Stop de functie om terug te gaan naar het hoofdmenu
            else:
                print("Ongeldige invoer! Voer 'ja' of 'nee' in.")  # Ongeldige invoer, vraag opnieuw


# Start het spel direct wanneer dit bestand wordt uitgevoerd
if __name__ == "__main__":
    raad_het_nummer()
