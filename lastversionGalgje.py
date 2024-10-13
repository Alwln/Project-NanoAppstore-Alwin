import random

def introductie():
    """
    Start het spel met een introductie en laat de speler een niveau kiezen.
    """
    print("                                     Welkom bij Galgje!")
    print("                         Kies een moeilijkheidsgraad om te beginnen:\n")
    print("                                  ===== 1. Makkelijk =====")
    print("                                  ===== 2. Gemiddeld =====")
    print("                                  ===== 3. Moeilijk ======")
    print("                           ===== 4. Terug naar Nano Appstore =====\n")

    keuze = input("                          Voer 1, 2, 3 of 4 in om een niveau te kiezen:\n")

    if keuze == '1':
        start_spel('makkelijk')
    elif keuze == '2':
        start_spel('gemiddeld')
    elif keuze == '3':
        start_spel('moeilijk')
    elif keuze == '4':
        print("Terug naar de Nano Appstore...\n")  # Geef een bericht dat ze teruggaan naar het menu
        return  # Stop de functie om terug te gaan naar het hoofdmenu
    else:
        print("Ongeldige keuze. Probeer het opnieuw.")
        introductie()  # Als de invoer ongeldig is, start de introductie opnieuw


def start_spel(niveau):
    """
    Start het Galgje-spel op basis van het geselecteerde niveau.
    """
    # Woordenlijsten voor elk niveau
    woorden_makkelijk = ['appel', 'auto', 'spiegel', 'cadeau', 'python', 'code', 'motor']
    woorden_gemiddeld = ['ananas', 'computer', 'software', 'hardlopen', 'batterij']
    woorden_moeilijk = ['encyclopedie', 'ondernemerschap', 'verantwoordelijkheid', 'communicatie']

    # Kies de juiste lijst op basis van het niveau
    if niveau == 'makkelijk':
        woorden_lijst = woorden_makkelijk
    elif niveau == 'gemiddeld':
        woorden_lijst = woorden_gemiddeld
    else:
        woorden_lijst = woorden_moeilijk

    # Kies een willekeurig woord uit de lijst en start het spel
    random_woord = random.choice(woorden_lijst).lower()
    speel_galgje(random_woord)


def speel_galgje(random_woord):
    """
    Voert het Galgje-spel uit met het gegeven woord.
    """
    gekozen_woord = ["_" for letter in random_woord]
    fouten = 0
    max_fouten = 7
    geraden_letters = []

    print("\nJe mag maximaal", max_fouten, "fouten maken om het woord te raden.")
    print(" ".join(gekozen_woord))  # Print de underscores voor het woord

    while fouten < max_fouten:
        # Vraag de speler om een letter te raden
        letter = input("Raad een letter: ").lower()

        # Controleer of de invoer geldig is (één enkele letter)
        if len(letter) != 1 or not letter.isalpha():
            print("Ongeldige invoer! Voer alstublieft slechts één enkele letter in.")
            continue

        # Controleer of de letter al geraden is
        if letter in geraden_letters:
            print("Je hebt deze letter al geraden. Probeer een andere.")
            continue

        # Voeg de letter toe aan de lijst van geraden letters
        geraden_letters.append(letter)

        # Controleer of de letter in het woord zit
        if letter in random_woord:
            print(f"Goed zo! De letter '{letter}' zit in het woord.")
            # Vervang de underscores door de juiste letters
            for index, char in enumerate(random_woord):
                if char == letter:
                    gekozen_woord[index] = letter
        else:
            fouten += 1
            print(f"Helaas! De letter '{letter}' zit niet in het woord. Je mag nog {max_fouten - fouten} fouten maken.")

        # Toon de huidige status van het woord
        print(" ".join(gekozen_woord))

        # Toon de lijst van geraden letters
        print("Geraden letters:", ", ".join(geraden_letters))

        # Controleer of het hele woord geraden is
        if "_" not in gekozen_woord:
            print("\nGefeliciteerd! Je hebt het woord geraden:", random_woord)
            break
    else:
        print("\nJammer! Je hebt te veel fouten gemaakt. Het woord was:", random_woord)

    # Vraag de speler of hij/zij opnieuw wil spelen of terug wil naar het menu
    while True:
        opnieuw_spelen = input("\nWil je opnieuw spelen of terug naar de Nano Appstore? (ja/nee): ").lower()
        if opnieuw_spelen == 'ja':
            introductie()  # Start de introductie opnieuw
            break
        elif opnieuw_spelen == 'nee':
            print("Bedankt voor het spelen! Terug naar de Nano Appstore.\n")  # Terug naar het menu
            break
        else:
            print("Ongeldige invoer! Voer 'ja' of 'nee' in.")  # Ongeldige invoer, vraag opnieuw


# Start het spel
if __name__ == "__main__":
    introductie()
