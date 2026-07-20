import os
import time
from system.scanner import Scanner, ScannerService
from system.services import ServiceManager
from system.device import DeviceService
from system.android import AndroidService
from system.battery import BatteryService
from system.storage import StorageService
from system.network import NetworkService


VERSION = "0.7 Alpha"


def clear():
    os.system("clear")


def logo():
    print(r"""
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║██║   ██║███████║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
""")


def boot():

    clear()

    logo()

    print(f"\nNovaOS {VERSION}")
    print("\nInitialisation...\n")

    time.sleep(1)

    print("[✓] Chargement du noyau")
    time.sleep(0.5)

    manager = ServiceManager()

    manager.register(DeviceService())
    manager.register(AndroidService())
    manager.register(ScannerService())
    manager.register(BatteryService())
    manager.register(StorageService())
    manager.register(NetworkService())

    manager.start()
    manager.report()

    time.sleep(1)

    print("[✓] Lancement du scanner système")
    time.sleep(0.5)

    scanner = Scanner()
    scanner.scan()

    input("\nAppuie sur Entrée pour continuer...")

