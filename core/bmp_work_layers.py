"""
Разбиение GIF на bmp, работа с bmp, сбор GIF из bmp
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

from PIL import Image
import random
import shutil
import os
import sys
import string


class Stego_gif:

    @classmethod
    def create_masks(cls, degree: int):
        text_mask = 0b11111111
        img_mask = 0b11111111
        text_mask <<= (8 - degree)
        text_mask %= 256
        img_mask >>= degree
        img_mask <<= degree

        return text_mask, img_mask

    @classmethod
    def encode_image(cls, txt_file: str) -> bool:
        
        BMP_HEADER_SIZE = 54
        degree = 1
        input_img_name = 'frames/frame_003.bmp'
        output_img_name = 'frames/frame_010.bmp'

        text_len = os.stat(txt_file).st_size

        img_len = os.stat(input_img_name).st_size

        if text_len >= img_len * degree / 8 - BMP_HEADER_SIZE:
            print("Too long text")
            return False

        text = open(txt_file, 'r')
        input_image = open(input_img_name, 'rb')
        output_image = open(output_img_name, 'wb')

        bmp_header = input_image.read(BMP_HEADER_SIZE)
        output_image.write(bmp_header)

        text_mask, img_mask = Stego_gif.create_masks(degree)

        while True:
            symbol = text.read(1)

            if not symbol:
                break

            symbol = ord(symbol)

            for byte_amount in range(0, 8, degree):
                img_byte = int.from_bytes(input_image.read(1), sys.byteorder) & img_mask
                bits = symbol & text_mask
                bits >>= (8 - degree)
                img_byte |= bits

                output_image.write(img_byte.to_bytes(1, sys.byteorder))
                symbol <<= degree

        output_image.write(input_image.read())

        text.close()
        input_image.close()
        output_image.close()
        os.remove('frames/frame_003.bmp')
        print(f'Password: f{Stego_gif.generate_password(str(text_len))}')
        return True

    @classmethod
    def decode_image(cls, encoded_img: str, output_txt: str, symbols_to_read: int) -> bool:
        BMP_HEADER_SIZE = 54
        degree = 1

        img_len = os.stat(encoded_img).st_size

        if symbols_to_read >= img_len * degree / 8 - BMP_HEADER_SIZE:
            print("Too much symbols to read")
            return False

        text = open(output_txt, 'w', encoding='utf-8')
        encoded_bmp = open(encoded_img, 'rb')

        encoded_bmp.seek(BMP_HEADER_SIZE)

        _, img_mask = Stego_gif.create_masks(degree)
        img_mask = ~img_mask

        read = 0
        while read < symbols_to_read:
            symbol = 0

            for bits_read in range(0, 8, degree):
                img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask
                symbol <<= degree
                symbol |= img_byte

            if chr(symbol) == '\n' and len(os.linesep) == 2:
                read += 1

            read += 1
            text.write(chr(symbol))

        text.close()
        encoded_bmp.close()
        return True

    @classmethod
    def split(cls, gif_filename: str) -> bool:
        # Open the GIF file
        global bmp_folder
        gif = Image.open(gif_filename)

        # Iterate over each frame in the GIF and save it as a BMP file
        for frame_index in range(gif.n_frames):
            # Seek to the current frame
            gif.seek(frame_index)

            # Create a filename for the BMP file
            bmp_filename = f'frame_{frame_index:03}.bmp'

            # Save the current frame as a BMP file
            gif.save(bmp_filename)

            # Move the BMP file to a specific folder
            bmp_folder = 'frames'
            if not os.path.exists(bmp_folder):
                os.mkdir(bmp_folder)
            os.rename(bmp_filename, os.path.join(bmp_folder, bmp_filename))

        # Set up the input and output filenames and paths
        output_filename = "stego_gif.gif"

        # Create a list of all BMP files in the input folder
        bmp_files = [f for f in os.listdir(bmp_folder) if f.endswith('.bmp')]

        return True

    @classmethod
    def collect_gif(cls) -> bool:
        bmp_folder = 'frames'
        output_filename = "stego_gif.gif"

        # Create a list of all BMP files in the input folder
        bmp_files = [f for f in os.listdir(bmp_folder) if f.endswith('.bmp')]

        # Create a list to hold all the image objects
        image_list = []

        # Loop through each BMP file and append the image object to the list
        for bmp_file in bmp_files:
            bmp_path = os.path.join(bmp_folder, bmp_file)
            bmp_image = Image.open(bmp_path)
            image_list.append(bmp_image)

        # Save the list of image objects as a single GIF file
        output_path = os.path.join(output_filename)
        image_list[0].save(output_path, save_all=True, append_images=image_list[1:], duration=500, loop=0)

        return True

    @classmethod
    def generate_password(cls, len_txt: str) -> str:
        words = (list(string.ascii_lowercase) + list(string.ascii_uppercase))
        random.shuffle(words)
        numb = list(string.digits)

        password = []
        for i in range(random.randint(1, 4)):
            password.append(random.choice(words))
        for i in len_txt:
            password.append(i)
        for i in range(random.randint(1, 4)):
            password.append(random.choice(words))
        for i in range(len(len_txt)):
            password.append(random.choice(numb))

        result = "".join(password)

        return result

    @classmethod
    def delet_bmp(cls) -> bool:
        shutil.rmtree('frames')
        return True
