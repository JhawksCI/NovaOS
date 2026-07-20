import os
import time

def clear():
    os.system("clear")

def start():
    clear()
    print("""
╔══════════════════════════════╗
║          NOVA OS v0.1        ║
╠══════════════════════════════╣
║ 1. Informations téléphone    ║
║ 2. Fichiers                  ║
║ 3. Terminal                  ║
║ 4. Quitter                   ║
╚══════════════════════════════╝
""")

while True:
    start()
    choix = input("NovaOS > ")

    if choix == "1":
        print("📱 Analyse du téléphone...")
        time.sleep(1)
        os.system("termux-battery-status")
        input("\nEntrée pour revenir")

    elif choix == "2":
        os.system("ls")
        input("\nEntrée pour revenir")

    elif choix == "3":
        os.system("bash")

    elif choix == "4":
        print("Arrêt de NovaOS...")
        break

    else:
        print("Commande inconnue")
        time.sleep(1)
