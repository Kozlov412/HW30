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