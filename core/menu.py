import os

from core.session import NovaSession
from core.dashboard import show_dashboard
from apps.files import file_explorer
from apps.virtual_files import VirtualFileExplorer
from system.scanner import Scanner
from system.android import Android
from system.battery import BatteryService
from system.storage import StorageService
from system.network import NetworkService


def clear():
    os.system("clear")


def header():

    print("""
═══════════════════════════════
          NOVA OS
       Interface v0.5
═══════════════════════════════
""")


def pause():

    input("\nAppuie sur Entrée pour revenir...")


def main_menu(session):

    while True:

        clear()
        header()

        print("""
1. 🖥️ Dashboard
2. 📂 Fichiers
3. 🔋 Batterie
4. 💾 Stockage
5. 📶 Réseau
6. 🧪 Nova Virtual Files
0. 🚪 Quitter
""")

        choice = input("> ")


        if choice == "1":
            clear()
            show_dashboard(session)
            pause()


        elif choice == "2":
            clear()
            file_explorer()
            pause()


        elif choice == "3":

            clear()
            battery = BatteryService()
            battery.start()
            battery.status()
            pause()


        elif choice == "4":

            clear()
            storage = StorageService()
            storage.start()
            storage.status()
            pause()


        elif choice == "5":

            clear()
            network = NetworkService()
            network.start()
            network.status()
            pause()


        elif choice == "6":

            clear()
            explorer = VirtualFileExplorer()
            explorer.start()
            pause()


        elif choice == "0":

            print("\nArrêt de NovaOS...")
            break


        else:

            print("Choix invalide")
            pause()

