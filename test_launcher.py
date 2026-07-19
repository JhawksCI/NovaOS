from core.app_manager import AppManager


manager = AppManager()

manager.scan()

manager.list_apps()

manager.launch(0)
