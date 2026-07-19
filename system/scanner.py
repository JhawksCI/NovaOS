from system.device import Device
from system.android import Android


class Scanner:

    def __init__(self):
        self.device = Device()
        self.android = Android()


    def scan(self):

        print("""
╔════════════════════════════╗
║       NOVA OS SCANNER      ║
╚════════════════════════════╝
""")

        print("🔍 Analyse du système...\n")

        self.device.detect()

        print("🖥️ Système :", self.device.system)
        print("⚙️ Architecture :", self.device.architecture)
        print("🔧 Kernel :", self.device.kernel)
        print("🧠 RAM :", self.device.ram, "Go")
        print("💾 Stockage :", self.device.storage)
        print("🚀 CPU :", self.device.cpu)

        print("\n📱 Informations Android :\n")

        print("🏭 Fabricant :",
              self.android.get_property("ro.product.manufacturer"))

        print("📱 Modèle :",
              self.android.get_property("ro.product.model"))

        print("🔢 Android :",
              self.android.get_property("ro.build.version.release"))

        print("\n✅ Scan terminé")

class ScannerService:

    def __init__(self):
        self.scanner = Scanner()


    def start(self):
        print("[✓] Scanner Service démarré")

