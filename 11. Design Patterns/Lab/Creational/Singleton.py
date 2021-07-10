def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DataImporter:
    def __init__(self):
        pass


importer1 = DataImporter()
print(importer1)
importer2 = DataImporter()
print(importer2)
print(importer1 == importer2)