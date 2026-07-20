import platform


def show_dashboard(session):

    print("""
╔════════════════════════════╗
║       NOVA DASHBOARD       ║
╚════════════════════════════╝
""")

    print("📱 Appareil : TECNO CE9")
    print("🤖 Système  : Android")

    print("\n🔋 Batterie")

    if session.battery.data:
        print(
            "   ",
            session.battery.data.get("percentage"),
            "%"
        )

    print("\n💾 Stockage")

    if session.storage.total:
        print(
            "   ",
            session.storage.used,
            "/",
            session.storage.total
        )

    print("\n📶 Réseau")

    if session.network.data:
        print(
            "   ",
            session.network.data.get(
                "ssid",
                "Inconnu"
            )
        )

    print("\n⚙️ Architecture :",
          platform.machine())
