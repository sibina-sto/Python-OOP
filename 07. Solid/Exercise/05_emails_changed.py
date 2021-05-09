from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class MyContent:
    def __init__(self):
        self.formats = {"myml": self.myml_format, "basic": self.basic_format}
        self.__content = ""

    def __repr__(self):
        return self.__content

    @property
    def available_formats(self):
        return f"Formats: {', '.join(self.formats)}"

    def format(self, content, type_format):
        if type_format not in self.formats:
            print("Format unavailable")

        self.__content = self.formats[type_format](content)

    @staticmethod
    def myml_format(content):
        return f"'<myML>' {content} '</myML>'"

    @staticmethod
    def basic_format(content):
        return content


class Email(IEmail):

    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM', 'MyML')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent()
content.format("Hello, there!", "myml")
email.set_content(content)
print(email)
