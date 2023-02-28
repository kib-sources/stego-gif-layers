# <h1 align="center"> Steganography in GIF
### (Russian)
___


### __Цели проекта__
+ Изучить структуру _gif images_
+ Изучить методы сокрытия информации в _gif images_
+ Разработать алогритма сокрытия информации в _gif images_







### __Алгоритм__
1. Хешируем пароль и получаем key

![stego_gif_1](https://github.com/kib-sources/stego-gif-layers/blob/issue001/docs/stego_gif_1.png)

2. .Используя изображение формата *.bmp *.png создаем полноцветное гиф изображение

![stego_gif_2](https://github.com/kib-sources/stego-gif-layers/blob/issue001/docs/stego_gif_2.png)

  
3. Разделяем полноцветное гиф на имеющиеся слои получаем gif_obj
  
  ![stego_gif_3](https://github.com/kib-sources/stego-gif-layers/blob/issue001/docs/stego_gif_3.png)

  
  
4. С помощью алгоритма собираем массив working area 
5. Массив  состоит из байтов перезаписываемых следующим слоем

![stego_gif_4](https://github.com/kib-sources/stego-gif-layers/blob/issue001/docs/stego_gif_4.png)


6. С помощью key зашифровываем сообщение и внедряем его в working area
  
  ![stego_gif_5](https://github.com/kib-sources/stego-gif-layers/blob/issue001/docs/stego_gif_5.png)
  

+Сложность обнаружения информации по сравнению с другими алгоритмами стеганографии

-Алгоритм работает только в полноцветных гиф изображениях