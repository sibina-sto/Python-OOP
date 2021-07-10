from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.__file = filename
        self.data = None

    def write_data(self, data):
        self.data = data
        print(f'Writing {data} to {self.__file}')

    def read_data(self):
        return self.data


class EncryptionDecoratorDataSource(DataSource):
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def __encrypt(self, data):
        return f'___{data}___'

    def __decrypt(self, data):
        return data[3:-3]

    def write_data(self, data):
        data = self.__encrypt(data)
        return self.data_source.write_data(data)

    def read_data(self):
        data = self.data_source.read_data()
        return self.__decrypt(data)


# fds = FileDataSource('file-name.txt')
# fds.read_data()
# fds.write_data('random data')

fds = EncryptionDecoratorDataSource(FileDataSource('file-name.txt'))
fds.write_data('random data')
fds.read_data()