from core.virtual_space import VirtualSpace


space = VirtualSpace()


space.create_file(
    "user/test.txt",
    "Bienvenue dans NovaOS Virtual Space"
)


space.list_files()


space.read_file(
    "user/test.txt"
)
