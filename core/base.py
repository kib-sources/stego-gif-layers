"""
core.base -- базовые классы

Create at 04.02.2023 10:21:54
~/core/base.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2022'
__license__ = 'LGPL'
__credits__ = [
    'pavelmstu',
]
__version__ = "20230204"
__status__ = 'Develop'  # "Production"

import os


from typing import List

Path = str
Bit = bool


class BaseContainerBit:

    def read(self) -> Bit:
        return NotImplemented

    def write(self, obj):
        return NotImplemented


def bits2bytes(bitlist: List[Bit]) -> bytes:


    # TODO теперь нужно разбить bits по 8 бит, перевести в байты и выдать байты
    pass
    raise NotImplementedError()
    return ...


def bytes2bits(b: bytes) -> List[Bit]:

    # TODO
    pass
    raise NotImplementedError()
    return ...



class BaseStegoContainer:
    """
    Базовый стегоконтейнер
    """


    @classmethod
    def load(cls, path: Path):
        """
        Загрузить пустой стегоконтейнер в память
        :param path: путь к пустому стегоконтейнеру. Берётся как шаблон без изменений
        :return:
        """
        return NotImplemented

    def save(self, path: Path):
        """
        Сохранить стегоконтейнер по пути
        :param path:
        :return:
        """

    def useful_area(self):
        """
        Итератор, возвращающий биты полезной области контейнера

        Чтение

        bits = [bit.read() for bit in self.useful_area]
        bytes = bits2bytes(bits)

        Запись

        for bit in self.useful_area:
            bit.write(...)

        :return:
        """
        return NotImplemented

    @property
    def len_useful_area(self):
        count = 0
        for _ in self.useful_area:
            count += 1
            continue
        return count

