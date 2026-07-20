class ServiceManager:

    def __init__(self):
        self.services = []


    def register(self, service):
        self.services.append(service)


    def start(self):

        print("""
╔════════════════════════════╗
║     NOVA SERVICE MANAGER   ║
╚════════════════════════════╝
""")

        for service in self.services:
            service.start()


        print("\nTous les services sont actifs ✔")


    def report(self):

        print("""
╔════════════════════════════╗
║      SYSTEM REPORT         ║
╚════════════════════════════╝
""")

        for service in self.services:

            if hasattr(service, "status"):
                service.status()
