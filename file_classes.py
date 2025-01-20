import csv
import json
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

class JsonFile(AbstractFile):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def append(self, data):
        try:
            existing_data = self.read()
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        if isinstance(existing_data, list):
            existing_data.append(data)
        else:
            raise ValueError("Existing data is not a list")

        self.write(existing_data)

class TxtFile(AbstractFile):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)

    def append(self, data):
        with open(self.file_path, 'a') as file:
            file.write(data)

class CsvFile(AbstractFile):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def write(self, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)