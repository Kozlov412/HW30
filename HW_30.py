import abc
import json
import csv
from typing import List, Dict, Any


class AbstractFile(abc.ABC):
    """Абстрактный класс для работы с файлами."""

    @abc.abstractmethod
    def read(self) -> Any:
        """Читает данные из файла."""
        pass

    @abc.abstractmethod
    def write(self, data: Any) -> None:
        """Записывает данные в файл."""
        pass

    @abc.abstractmethod
    def append(self, data: Any) -> None:
        """Добавляет данные в файл."""
        pass

class JsonFile(AbstractFile):
    """Класс для работы с JSON-файлами."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> Dict:
        """Читает данные из JSON-файла."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка при чтении JSON-файла: {e}")
            return {}

    def write(self, data: Dict) -> None:
        """Записывает данные в JSON-файл."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {e}")

    def append(self, data: Dict) -> None:
        """Добавляет данные в JSON-файл."""
        try:
            with open(self.file_path, 'r+') as f:
                try:
                    existing_data = json.load(f)
                    # Проверяем, является ли existing_data списком. Если нет - превращаем в список
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    existing_data = [] # Если файл пуст или поврежден, создаем пустой список
                existing_data.append(data)
                f.seek(0)
                json.dump(existing_data, f, indent=4)
                f.truncate()
        except IOError as e:
            print(f"Ошибка при добавлении данных в JSON-файл: {e}")

class TxtFile(AbstractFile):
    """Класс для работы с текстовыми файлами."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        """Читает данные из текстового файла."""
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError as e:
            print(f"Ошибка при чтении текстового файла: {e}")
            return ""

    def write(self, data: str) -> None:
        """Записывает данные в текстовый файл."""
        try:
            with open(self.file_path, 'w') as f:
                f.write(data)
        except IOError as e:
            print(f"Ошибка при записи в текстовый файл: {e}")

    def append(self, data: str) -> None:
        """Добавляет данные в текстовый файл."""
        try:
            with open(self.file_path, 'a') as f:
                f.write(data)
        except IOError as e:
            print(f"Ошибка при добавлении данных в текстовый файл: {e}")

class CsvFile(AbstractFile):
    """Класс для работы с CSV-файлами."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> List[List[str]]:
        """Читает данные из CSV-файла."""
        try:
            with open(self.file_path, 'r') as f:
                reader = csv.reader(f)
                return list(reader)
        except FileNotFoundError as e:
            print(f"Ошибка при чтении CSV-файла: {e}")
            return []

    def write(self, data: List[List[str]]) -> None:
        """Записывает данные в CSV-файл."""
        try:
            with open(self.file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except IOError as e:
            print(f"Ошибка при записи в CSV-файл: {e}")

    def append(self, data: List[List[str]]) -> None:
        """Добавляет данные в CSV-файл."""
        try:
            with open(self.file_path, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except IOError as e:
            print(f"Ошибка при добавлении данных в CSV-файл: {e}")            