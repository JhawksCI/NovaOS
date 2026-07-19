from system.services import ServiceManager


manager = ServiceManager()

manager.register("Device Service")
manager.register("Android Service")
manager.register("Scanner Service")

manager.start()
