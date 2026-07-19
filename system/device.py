import platform
import subprocess
import os

try:
    import distro
except ImportError:
    distro = None


class Device:

    def __init__(self):
        self.system = None
        self.device_name = None
        self.architecture = None
        self.kernel = None
        self.ram = None
        self.storage = None
        self.cpu = None


    def command(self, cmd):
        try:
            result = subprocess.check_output(
                cmd,
                shell=True
            ).decode().strip()

            return result

        except:
            return "Indisponible"


    def detect(self):

        self.system = platform.system()
        self.device_name = platform.node()
        self.architecture = platform.machine()
        self.kernel = self.command("uname -r")

        self.cpu = self.command("cat /proc/cpuinfo | grep Hardware | head -1")

        mem = self.command("grep MemTotal /proc/meminfo")

        if mem != "Indisponible":
            ram_kb = int(mem.split()[1])
            self.ram = round(ram_kb / 1024 / 1024, 2)


        disk = self.command("df -h /data | tail -1")

        if disk != "Indisponible":
            self.storage = disk.split()[1]


        return self



    def show(self):

        print("""
╔════════════════════════════╗
║          NOVA OS           ║
║     Device Analyzer v0.2    ║
╚════════════════════════════╝
""")

        print(f"🖥️ Système      : {self.system}")
        print(f"📱 Appareil     : {self.device_name}")
        print(f"⚙️ Architecture : {self.architecture}")
        print(f"🔧 Kernel       : {self.kernel}")
        print(f"🧠 RAM          : {self.ram} Go")
        print(f"💾 Stockage     : {self.storage}")
        print(f"🚀 CPU          : {self.cpu}")

        print("\n✅ Analyse terminée")

class DeviceService:

    def __init__(self):
        self.device = Device()


    def start(self):
        self.device.detect()
        print("[✓] Device Service démarré")

