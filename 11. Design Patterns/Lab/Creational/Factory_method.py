from abc import ABC, abstractmethod
from json import loads


class DataConverter(ABC):
    @abstractmethod
    def to_dict(self, data):
        pass


class JsonDataConverter(DataConverter):
    def to_dict(self, data):
        return loads(data)


class CsvDataConverter(DataConverter):
    def to_dict(self, data):
        return


class DataConverterFactory(ABC):
    @abstractmethod
    def get_converter(self, type) -> DataConverter:
        pass


class JsonDataConverterFactory(DataConverterFactory):
    def get_converter(self, type=None) -> DataConverter:
        return JsonDataConverter()


class ConcreteDataConverterFactory(DataConverterFactory):
    def get_converter(self, type) -> DataConverter:
        if type == 'json':
            return JsonDataConverter()
        elif type == 'csv':
            return CsvDataConverter()

        raise ValueError('invalid convertor type')


json = '''
{
    "name": "Elena",
    "age": 23
}
'''

csv = '''
name, age
Elena, 23
'''


def convert(type, data):
    factory = ConcreteDataConverterFactory()
    return factory.get_converter(type).to_dict(data)


converter = JsonDataConverter()
print(converter.to_dict(json))