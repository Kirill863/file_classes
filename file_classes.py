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
    """
    функция - иницилизатор
    param - путь к файлу
    """
    def __init__(self, file_path):
        self.file_path = file_path
    """
    функция - чтения 
    param - путь к файлу
    """
    def read(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)
    """
    функция - записи 
    param - путь к файлу, данные из json файла
    """
    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
    """
    функция - дополнения 
    param - путь к файлу, данные из json файла
    исключения - ситуаци, когда файл не найден, или данные json - не корректны
    """
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

    """
    класс для работы с txt файлами
    """
class TxtFile(AbstractFile):
    """
    функция - иницилизатор
    param - путь к файлу
    """
    def __init__(self, file_path):
        self.file_path = file_path
    """
    функция - чтения 
    param - путь к файлу
    """       
    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()
    """
    функция - записи 
    param - путь к файлу, данные из txt файла
    """
    def write(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)
    """
    функция - дополнения 
    param - путь к файлу, данные из txt файла
    """
    def append(self, data):
        with open(self.file_path, 'a') as file:
            file.write(data)
    """
    класс для работы с сsv файлами
    """
class CsvFile(AbstractFile):
    """
    функция - иницилизатор
    param - путь к файлу
    """
    def __init__(self, file_path):
        self.file_path = file_path

    """
    функция - чтения 
    param - путь к файлу
    """   
    def read(self):
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    """
    функция - записи 
    param - путь к файлу, данные из csv файла
    """
    def write(self, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    """
    функция - дополнения 
    param - путь к файлу, данные из csv файла
    """
    def append(self, data):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == "__main__":
    # Пример использования JsonFile
    json_file = JsonFile('example.json')
    json_file.write([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}])
    json_file.append({'name': 'Charlie', 'age': 35})
    print("JSON File Content:")
    print(json_file.read())

    # Пример использования TxtFile
    txt_file = TxtFile('example.txt')
    txt_file.write('Hello, World!')
    txt_file.append('\nThis is a new line.')
    print("\nText File Content:")
    print(txt_file.read())

    # Пример использования CsvFile
    csv_file = CsvFile('example.csv')
    csv_file.write([['Name', 'Age'], ['Alice', 30], ['Bob', 25]])
    csv_file.append([['Charlie', 35]])
    print("\nCSV File Content:")
    print(csv_file.read())
