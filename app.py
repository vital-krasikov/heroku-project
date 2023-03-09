

import streamlit as st
from PIL import Image 
from recognize_number import process

st.title('Number recognition demo')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # Добавление загрузчика файлов

if not image_file is None:                                           # Выполнение блока, если загружено изображение
    col1, col2 = st.columns(2)                                  # Создание 2 колонок # st.beta_columns(2)
    image = Image.open(image_file)                                   # Открытие изображения
    result = process(image_file)                                     # Обработка изображения с помощью функции, реализованной в другом файле
    col1.text('Source image')
    col1.image(image)                                                # Вывод в первой колонке исходного изображения
    col2.text('Number ' + str(result))
    col2.image(result[1])                                            # Вывод результат во второй колонке
