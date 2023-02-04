"""

TODO


Create at 04.02.2023 10:35:31
~/core/gif.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2022'
__license__ = 'LGPL'
__credits__ = [
    'pavelmstu',
]
__version__ = "20230204"
__status__ = 'Develop'  # "Production"


from Crypto.Cipher import AES

import hashlib

from core.base import Path
from core.base import Bit
from core.base import BaseStegoContainer
from core.base import bytes2bits


def full_color_gif(path_in: Path, path_out: Path) -> type(None):
    """
    Функция создаёт полноцветный GIF.

    :param path_in: путь к изображению *.bmp, *.png
    :param path_out: путь к полноцветному *.gif
    :return:
    """

    # TODO
    #  1. взять изображение и определить все его цвета
    #  2. перемешать цвета и разделить их на 256 -- это количество слоёв
    #  3. определить палитры.  i=0
    #  4. взять i-ю палитру. Пробежаться по изображению. Записать.
    #  5. i+=1. если не закончились цвета goto 4.
    pass
    pass

    return NotImplementedError()


class GifLayerContainer(BaseStegoContainer):
    """
    TODO
    :param BaseStegoContainer:
    :return:
    """

    def __init__(self):
        # TODO
        pass

    @classmethod
    def load(cls, path: Path):
        """
        # TODO
        :param path: путь к пустому стегоконтейнеру. Берётся как шаблон без изменений
        :return:
        """
        obj = GifLayerContainer()
        # TODO
        return obj

    def save(self, path: Path):
        """
        # TODO
        :param path:
        :return:
        """
        # TODO
        pass

    def useful_area(self):
        """
        # TODO
        :return:
        """
        # TODO
        pass


def gif_layer_embed(gif_path_in: Path, gif_path_out: Path, message: bytes, password: str):
    """
    Вкрапление в стегосообщение
    :param gif_path_in: пустой gif-контейнер (донор)
    :param gif_path_out: стеганографический gif-контейнер
    :param message: сообщение для записи
    :param password: пароль
    :return:
    """

    sh = hashlib.sha256()
    sh.update(password.encode())
    key = sh.digest()

    # TODO зашифровать message ключом key
    # from Crypto.Cipher import AES
    # ...
    # message = crypt(message, key)
    pass

    gl = GifLayerContainer.load(gif_path_in)

    if len(message)*8 > gl.len_useful_area:
        raise Exception("Размер полезной области контейнера меньше сообщения")

    message_bits = bytes2bits(message)

    for message_bit, container_bit in zip(message_bits, gl.useful_area):
        container_bit.write(message_bit)
        continue

    gl.save(gif_path_out)

    return


