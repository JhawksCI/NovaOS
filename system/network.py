import subprocess
import json


class NetworkService:

    def __init__(self):
        self.data = None

    def start(self):

        print("[✓] Network Service démarré")

        try:
            result = subprocess.check_output(
                "termux-wifi-connectioninfo",
                shell=True
            ).decode()

            self.data = json.loads(result)

        except:
            self.data = None

    def status(self):

        print("\n📶 Réseau")

        if self.data:

            print("SSID :", self.data.get("ssid", "Inconnu"))
            print("BSSID :", self.data.get("bssid", "Inconnu"))
            print("IP :", self.data.get("ip", "Inconnue"))
            print("Lien :", self.data.get("link_speed_mbps", "N/A"), "Mbps")

        else:

            print("Wi-Fi non connecté ou accès refusé")
