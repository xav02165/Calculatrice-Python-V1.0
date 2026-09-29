# Fichier : calculatrice.py
from fonction import addition, division, multiplication, soustraction


def main():
    print("========================================")
    print("          CALCULATRICE PYTHON           ")
    print("========================================\n")

    while True:
        # 1. Demande directement le premier nombre
        saisie = (
            input("Saisis le premier nombre (ou 'Q' pour quitter) : ")
            .strip()
            .upper()
        )

        if saisie == "Q":
            print("Fermeture de la calculatrice. À bientôt !")
            break

        try:
            nombre1 = float(saisie)
        except ValueError:
            print("⚠️ Nombre invalide, recommence.\n")
            continue

        # 2. Choix de l'opération
        print("Opérations : [1] + | [2] - | [3] * | [4] /")
        choix = input("Choisis l'opération (1-4) : ").strip()

        if choix not in ["1", "2", "3", "4"]:
            print("⚠️ Opération invalide, recommence.\n")
            continue

        # 3. Deuxième nombre
        try:
            nombre2 = float(input("Saisis le deuxième nombre : "))
        except ValueError:
            print("⚠️ Nombre invalide, recommence.\n")
            continue

        # 4. Calcul et enchaînement immédiat
        try:
            if choix == "1":
                res = addition(nombre1, nombre2)
            elif choix == "2":
                res = soustraction(nombre1, nombre2)
            elif choix == "3":
                res = multiplication(nombre1, nombre2)
            elif choix == "4":
                res = division(nombre1, nombre2)

            print(f"--> RÉSULTAT : {res:g}\n")
            # Le programme repart DIRECTEMENT au début du 'while' ici !

        except ValueError as e:
            print(f"⚠️ Erreur : {e}\n")


if __name__ == "__main__":
    main()
