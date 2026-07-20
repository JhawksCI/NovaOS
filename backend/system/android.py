import subprocess


class Android:

    def get_property(self, prop):
        try:
            result = subprocess.check_output(
                f"getprop {prop}",
                shell=True
            ).decode().strip()

            return result if result else "Inconnu"

        except:
            return "Non disponible"


    def info(self):

        print("""
╔════════════════════════════╗
║      ANDROID ANALYZER      ║
╚════════════════════════════╝
""")

        print("🏭 Fabricant :", 
              self.get_property("ro.product.manufacturer"))

        print("📱 Modèle :", 
              self.get_property("ro.product.model"))

        print("🔢 Version Android :", 
              self.get_property("ro.build.version.release"))

        print("📦 Marque :", 
              self.get_property("ro.product.brand"))

class AndroidService:

    def __init__(self):
        self.android = Android()


    def start(self):
        print("[✓] Android Service démarré")

