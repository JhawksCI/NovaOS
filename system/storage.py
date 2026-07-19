import subprocess


class StorageService:

    def __init__(self):
        self.total = None
        self.used = None
        self.free = None


    def command(self, cmd):
        try:
            return subprocess.check_output(
                cmd,
                shell=True
            ).decode().strip()

        except:
            return None


    def start(self):

        print("[✓] Storage Service démarré")

        result = self.command("df -h /data")

        if result:

            lines = result.split("\n")

            if len(lines) > 1:

                info = lines[1].split()

                self.total = info[1]
                self.used = info[2]
                self.free = info[3]


    def status(self):

        print("\n💾 Stockage")

        if self.total:

            print("Total :", self.total)
            print("Utilisé :", self.used)
            print("Libre :", self.free)

        else:

            print("Données indisponibles")
