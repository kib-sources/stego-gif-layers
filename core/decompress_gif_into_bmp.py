"""
Программа использует библиотеку Pillow для расшифровки gif изображения с помощью алгоритма LZW, разбивает отдельные слои на
bmp файлы, затем снова собирает их в gif
"""
from PIL import Image
import os
__author__ = 'Parinova Diana', 'Belyuchenko Dmitryi'
__copyright__ = 'KIB, 2023'
__credits__ = [
    'Parinova Diana' 
    'Belyuchenko Dmitryi'
]

__license__ = 'LGPL'
__version__ = "20230320"
__status__ = "Production"

# Открыть гиф изображение
gif_image = Image.open("3.gif")

# Проходим по слоям гиф
for i in range(gif_image.n_frames):
     gif_image.seek(i)

     # Конвертируем слой в bmp
     bmp_image = gif_image.convert("RGB")

     # Сохраняем bmp файлы
     bmp_image.save(f"frame_{i}.bmp")


# указываем папки к bmp файлам и папку для сохранения нового гиф
input_folder = ".bmp path"
output_folder = ".gif path"
output_filename = "stego_gif.gif"

# создаем лист bmp файлов
bmp_files = [f for f in os.listdir(input_folder) if f.endswith('.bmp')]

image_list = []

# Проходим каждый файл BMP и добавьте объект изображения в список.
for bmp_file in bmp_files:
    bmp_path = os.path.join(input_folder, bmp_file)
    bmp_image = Image.open(bmp_path)
    image_list.append(bmp_image)

# Сохраняем список объектов изображения в виде одного файла GIF.
output_path = os.path.join(output_folder, output_filename)
image_list[0].save(output_path, save_all=True, append_images=image_list[1:], duration=50, loop=0)
