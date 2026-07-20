import os


class VirtualSpace:

    def __init__(self):

        self.root = "virtual"


    def get_permission(self, path):

        if path.startswith("system"):
            return "READ ONLY"

        elif path.startswith("apps"):
            return "EXECUTE"

        elif path.startswith("user"):
            return "READ / WRITE"

        return "UNKNOWN"


    def create_file(self, path, content=""):

        file_path = os.path.join(
            self.root,
            path
        )

        folder = os.path.dirname(file_path)

        os.makedirs(
            folder,
            exist_ok=True
        )

        with open(
            file_path,
            "w"
        ) as file:

            file.write(content)


        print("✅ Fichier créé :", path)



    def read_file(self, path):

        file_path = os.path.join(
            self.root,
            path
        )

        try:

            with open(file_path, "r") as file:

                print(file.read())

        except:

            print("❌ Fichier introuvable")



    def list_files(self):

        print("\n🧪 NOVA VIRTUAL SPACE")

        for root, dirs, files in os.walk(self.root):

            for file in files:

                print(
                    os.path.join(
                        root,
                        file
                    )
                )

