#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémente n pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    # Vérifie que l'utilisateur a passé un argument
    if len(sys.argv) > 1:
        try:
            # Convertit l'argument en entier
            n = int(sys.argv[1])
            if n >= 0:
                f = factorial(n)
                print(f)
            else:
                print("Veuillez entrer un entier positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    else:
        print("Veuillez fournir un nombre en argument.")
