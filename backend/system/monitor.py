import platform


class SystemMonitor:

    def __init__(self, session):

        self.session = session


    def show(self):

        print("""
═══════════════════════════════
        NOVA SYSTEM MONITOR
═══════════════════════════════
""")

        print("📱 APPAREIL")
        print("Système :", platform.system())
        print("Architecture :", platform.machine())


        print("\n🔋 BATTERIE")

        if self.session.battery.data:

            print(
                self.session.battery.data.get(
                    "percentage",
                    "?"
                ),
                "%"
            )

            print(
                self.session.battery.data.get(
                    "status",
                    "?"
                )
            )

        else:

            print("Indisponible")


        print("\n💾 STOCKAGE")

        print(
            "Total :",
            self.session.storage.total
        )

        print(
            "Libre :",
            self.session.storage.free
        )


        print("\n📶 RÉSEAU")

        if self.session.network.data:

            print(
                "SSID :",
                self.session.network.data.get(
                    "ssid",
                    "?"
                )
            )

        else:

            print("Non connecté")
