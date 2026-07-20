from system.battery import BatteryService
from system.storage import StorageService
from system.network import NetworkService


class NovaSession:

    def __init__(self):

        self.battery = BatteryService()
        self.storage = StorageService()
        self.network = NetworkService()


    def start(self):

        self.battery.start()
        self.storage.start()
        self.network.start()
