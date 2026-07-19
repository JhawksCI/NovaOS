import os

from core.virtual_space import VirtualSpace


class VirtualFileExplorer:

    def __init__(self):

        self.space = VirtualSpace()


    def browse(self):

        path = "virtual"

        while True:

            print("\n📂", path)
            print("Permission :",
                  self.space.get_permission(
                      path.replace("virtual/", "")
                  ))

            items = os.listdir(path)

            for i, item in enumerate(items):

                full = os.path.join(path, item)

                if os.path.isdir(full):
                    print(
                        i + 1,
                        "📁",
                        item
                    )

                else:
                    print(
                        i + 1,
                        "📄",
                        item
                    )


            print("\n0. Retour")

            choice = input("> ")


            if choice == "0":
                break


            try:

                selected = items[int(choice)-1]

                new_path = os.path.join(
                    path,
                    selected
                )

                if os.path.isdir(new_path):

                    path = new_path

                else:

                    print(
                        "📄 Fichier :",
                        selected
                    )

            except:

                print("Choix invalide")


    def edit_file(self):

        path = input(
            "Fichier à modifier : "
        )

        file_path = os.path.join(
            "virtual",
            path
        )


        if os.path.exists(file_path):

            content = input(
                "Nouveau contenu : "
            )


            with open(
                file_path,
                "w"
            ) as file:

                file.write(content)


            print(
                "✅ Fichier modifié"
            )

        else:

            print(
                "❌ Fichier introuvable"
            )


    def create_file(self):

        path = input("Nom du fichier (ex: user/test.txt) : ")

        content = input("Contenu : ")

        self.space.create_file(
            path,
            content
        )


    def read_file(self):

        path = input("Fichier à lire : ")

        self.space.read_file(
            path
        )


    def delete_file(self):

        path = input("Fichier à supprimer : ")

        file_path = os.path.join(
            "virtual",
            path
        )

        if os.path.exists(file_path):

            os.remove(file_path)

            print("✅ Fichier supprimé")

        else:

            print("❌ Fichier introuvable")


    def start(self):

        while True:

            print("""
╔════════════════════════════╗
║    NOVA VIRTUAL FILES      ║
╚════════════════════════════╝

1. 📄 Créer un fichier
2. 📖 Lire un fichier
3. 📂 Explorer
4. 📝 Modifier
5. 🗑️ Supprimer
0. Retour
""")

            choice = input("> ")


            if choice == "1":
                self.create_file()

            elif choice == "2":
                self.read_file()

            elif choice == "3":
                self.browse()

            elif choice == "4":
                self.edit_file()

            elif choice == "5":
                self.delete_file()

            elif choice == "0":
                break

            else:
                print("Choix invalide")

