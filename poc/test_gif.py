import io
from PIL import Image

def decompress_gif_lzw(compressed_data):
    # Initialize the LZW dictionary with all possible 8-bit values
    dictionary = {bytes([i]): i for i in range(256)}
    clear_code = 256
    end_of_information_code = clear_code + 1

    # Initialize variables for the LZW decompression algorithm
    current_code_length = 9
    current_code = None
    previous_code = None
    output_data = []

    # Convert the compressed data to a byte stream
    compressed_data_stream = io.BytesIO(compressed_data)

    # Read the GIF header and skip to the compressed data section
    image = Image.open(compressed_data_stream)
    image.seek(0)
    image.seek(1)
    image.seek(2)
    image.seek(9)

    # Read and decompress the LZW compressed data
    compressed_byte = image.read(1)
    while compressed_byte:
        compressed_code = int.from_bytes(compressed_byte, byteorder='little')

        if current_code is None:
            current_code = compressed_code
            output_data.append(dictionary[bytes([current_code])])
        elif compressed_code == clear_code:
            dictionary = {bytes([i]): i for i in range(256)}
            dictionary[bytes([clear_code])] = clear_code
            dictionary[bytes([end_of_information_code])] = end_of_information_code
            current_code_length = 9
            current_code = None
            previous_code = None
        elif compressed_code == end_of_information_code:
            break
        else:
            if compressed_code in dictionary:
                entry = dictionary[compressed_code]
            elif compressed_code == len(dictionary):
                entry = bytes([previous_code[0]]) + bytes([previous_code[0]])
            else:
                raise ValueError('Invalid compressed code: {}'.format(compressed_code))

            output_data.append(entry)

            if previous_code is not None:
                dictionary[len(dictionary)] = bytes([previous_code[0]]) + bytes([entry[0]])

            previous_code = bytes([compressed_code])
            if len(dictionary) == 2 ** current_code_length:
                current_code_length += 1

            current_code = compressed_code

        compressed_byte = image.read(1)

    return b''.join(output_data)

with open('volk.gif', 'rb') as f:
    compressed_data = f.read()

decompressed_data = decompress_gif_lzw(compressed_data)