class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    @staticmethod
    def get_path(path):
        names = path.split('\\')[1:]
        node = Folder('/')
        for name in names:
            node = node.children[name]
        return node

    def move(self, new_path):
        new_folder = self.get_path(new_path)


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child


class File(Component):
    def __init__(self, name, content):
        super().__init__(name)
        self.content = content