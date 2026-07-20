import os
import json


class AppManager:

    def __init__(self):

        self.path = "virtual/apps"
        self.apps = []


    def scan(self):

        self.apps = []

        if not os.path.exists(self.path):
            return


        for app in os.listdir(self.path):

            app_path = os.path.join(
                self.path,
                app
            )


            config = os.path.join(
                app_path,
                "app.json"
            )


            if os.path.exists(config):

                with open(config, "r") as file:

                    data = json.load(file)

                    self.apps.append(data)


        print(
            "[✓]",
            len(self.apps),
            "application(s) détectée(s)"
        )


    def list_apps(self):

        print("""
╔════════════════════════════╗
║       NOVA APPS            ║
╚════════════════════════════╝
""")


        for i, app in enumerate(self.apps):

            print(
                i + 1,
                "📦",
                app["name"],
                "v",
                app["version"]
            )


    def launch(self, index):

        app = self.apps[index]

        name = app["name"]

        path = os.path.join(
            self.path,
            name,
            "app.py"
        )


        if os.path.exists(path):

            print(
                "🚀 Lancement de",
                name
            )


            namespace = {}

            with open(path, "r") as file:

                code = file.read()

            exec(
                code,
                namespace
            )


            namespace["run"]()


        else:

            print(
                "❌ Application non exécutable"
            )

