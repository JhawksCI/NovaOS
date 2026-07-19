import subprocess
import json


class BatteryService:

    def __init__(self):
        self.data = None


    def start(self):

        print("[✓] Battery Service démarré")


        try:
            result = subprocess.check_output(
                "termux-battery-status",
                shell=True
            ).decode()


            self.data = json.loads(result)

        except:
            self.data = None
            print("⚠️ Impossible de lire la batterie")



    def show(self):

        if self.data:

            print("\n🔋 Batterie")
            print("Pourcentage :", 
                  self.data["percentage"], "%")

            print("État :",
                  self.data["status"])

            print("Température :",
                  self.data["temperature"],
                  "°C")

        else:
            print("Données batterie indisponibles")


    def status(self):

        if self.data:

            print("🔋 Batterie :", self.data["percentage"], "%")
            print("⚡ État :", self.data["status"])
            print("🌡️ Température :", self.data["temperature"], "°C")

        else:
            print("🔋 Batterie : Données indisponibles")

