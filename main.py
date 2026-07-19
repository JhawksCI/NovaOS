from core.boot import boot
from core.menu import main_menu
from core.session import NovaSession


if __name__ == "__main__":

    boot()

    session = NovaSession()
    session.start()

    main_menu(session)
