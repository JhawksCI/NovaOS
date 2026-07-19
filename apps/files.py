import os


def file_explorer():

    path = "/sdcard"

    while True:

        print("\n📂 NOVA FILES")
        print("Chemin :", path)

        try:

            files = os.listdir(path)

            for i, file in enumerate(files):
                print(
                    i + 1,
                    file
                )

            print("\n0. Retour")

            choice = input("> ")

            if choice == "0":
                break

            index = int(choice) - 1

            selected = files[index]

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

        except Exception as e:

            print(
                "Erreur :",
                e
            )
            break
