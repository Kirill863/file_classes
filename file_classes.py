from abc import ABC, abstractmethod

class AbstractFile(ABC):

    @abstractmethod
    def read(self):
        """Абстрактный метод для чтения данных из файла."""
        pass

    @abstractmethod
    def write(self, data):
        """Абстрактный метод для записи данных в файл."""
        pass

    @abstractmethod
    def append(self, data):
        """Абстрактный метод для добавления данных в файл."""
        pass
