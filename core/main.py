"""
Стеганография в GIF
Create at 09.04.2023 00:00:00
~core/main.py
"""

__authors__ = [
    'DipoPY',
    'Diana3002'
]
__copyright__ = 'KIB, 2023'
__license__ = 'LGPL'
__credits__ = [
    'DipoPY',
    'Diana3002'
]
__version__ = "20230409"
__status__ = "Production"

from bmp_work_layers import Stego_gif

def main():
    while True:
        choice = int(input('Enter number:\n 1 - encode\n 2 - decode\n 3 - quit\n'))

        if choice == 1:
            gif_filename = input('Enter the name of the gif: ')
            Stego_gif.split(gif_filename)
            Stego_gif.encode_image('gggg.txt')
            Stego_gif.collect_gif()
            # Split_gif.delet_bmp()

        elif choice == 2:
            password = input('Enter password: ')

        elif choice == 3:
            pass


if __name__ == "__main__":
    main()
