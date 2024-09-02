#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            if n >= 0:
                f = factorial(n)
                print(f)
            else:
                print("Veuillez entrer un entier positif ou nul.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    else:
        print("Veuillez fournir un nombre en argument.")
