import sys

from PIL.features import codecs





def nib(text: str) -> str:
    res = ''
    for nibbles in text:
        res += nibbles.encode('ascii').hex()



    return res


def retrieve_tex_from_gif(filepath):

    decod_text = ''
    with open(filepath, 'rb') as f:
        count_layers = 0
        gif_hex = f.read().hex()


        for i in range(len(gif_hex)):
            if gif_hex[i] == '2' and gif_hex[i + 1] == '1' and gif_hex[i + 2] == 'f' and gif_hex[i + 3] == '9':
                count_layers += 1
                if count_layers == gif_hex.count('21f9') - 1:
                    for j in range(i-1, 1, -1 ):
                        if gif_hex[j] == '0' and gif_hex[j-1] == '0':
                            break
                        decod_text += gif_hex[j]


        decod_text = decod_text[::-1]

        b = bytes.fromhex(decod_text)
        b.decode('utf-8')

        return b






def create_text_in_gif (filepath):
    arr = []
    print("Введите текст, который хотите спрятать: ")
    text = input()


    with open(filepath, 'rb') as f:
        count_layers = 0
        gif_hex = f.read().hex()

        for i in range(len(gif_hex)):
            if gif_hex[i] == '0' and gif_hex[i + 1] == '0' and gif_hex[i + 2] == '2' and gif_hex[i + 3] == '1':
                count_layers += 1
                if count_layers == gif_hex.count('0021') - 1:
                    t1 = gif_hex[:i+2]
                    t2 = gif_hex[i+2:]
                    t3 = t1 + nib(text) + t2
                    break
        for i in t3:
            arr.append(str(i))
        arr = "".join(arr)
        return bytes.fromhex(arr)


print("Что вы ходите сделать?")
print("1 - Спрятать текст")
print("2 - Извлечь текст")
choice = int(input())



if choice == 1:
    print("Введите название GIF: ")
    gif_name = input()

    print("Введите название нового GIF: ")
    name_new_gif = input()
    with open(name_new_gif, 'wb+') as fh:
        fh.write(create_text_in_gif(gif_name))

elif choice == 2:
    print("Введите название GIF: ")
    gif_name = input()
    print(retrieve_tex_from_gif(gif_name))










