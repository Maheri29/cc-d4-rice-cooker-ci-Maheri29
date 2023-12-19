import time

def choisir_mode():
    print('Modes disponibles :')
    print('1. Riz Blanc')
    print('2. Riz Complet')
    print('3. Cuisson Vapeur')
    print('4. Autre aliment')

    choix = input('Choisissez un mode de cuisson (1/2/3/4) : ')

    temps_cuisson = 0

    if choix == '1':
        print('Mode Riz Blanc sélectionné')
        temps_cuisson = 2
    elif choix == '2':
        print('Mode Riz Complet sélectionné')
        temps_cuisson = 2
    elif choix == '3':
        print('Mode Cuisson Vapeur sélectionné')
        temps_cuisson = 2
    elif choix == '4':
        temps_personnalise = int(input("Entrez le temps de cuisson en secondes pour l'autre aliment : "))
        if temps_personnalise > 0:
            print(f"Mode Autre Aliment sélectionné - Cuisson pendant {temps_personnalise} secondes.")
            temps_cuisson = temps_personnalise
        else:
            print('Temps invalide.')
    else:
        print('Choix non valide')

    if temps_cuisson > 0:
        print('Types d\'alertes disponibles :')
        print('1. Son')
        print('2. Lumières clignotantes')

        choix_alerte = input('Choisissez le type d\'alerte pour signaler la fin de la cuisson (1/2) : ')

        print(f"La cuisson se déroulera pendant {temps_cuisson} secondes.")

        if choix_alerte == '1':
            time.sleep(temps_cuisson)
            print('*BIP*BIP*BIP* La cuisson est terminée !')
        elif choix_alerte == '2':
            time.sleep(temps_cuisson)
            print('*lumières clignotantes* La cuisson est terminée !')
        else:
            print('Choix non valide. Aucune alerte ne sera déclenchée.')

        time.sleep(temps_cuisson)

        choix_apres_cuisson = input('Que voulez-vous faire maintenant? (1. Éteindre / 2. Maintenir au chaud) : ')

        if choix_apres_cuisson == '1':
            print('Le rice cooker a été éteint.')
        elif choix_apres_cuisson == '2':
            print('Le riz est maintenu au chaud.')
        else:
            print('Choix non valide. Le rice cooker sera éteint par défaut.')

choisir_mode()
