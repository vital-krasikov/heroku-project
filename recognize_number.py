

from tensorflow.keras.models import load_model
MODEL_NAME =   'model_fmr_all.h5'
import numpy as np
from PIL import Image 
model = load_model(MODEL_NAME)                                              # Загрузка весов модели
INPUT_SHAPE = (1, 28, 28, 1)


def process(image_file):
    image = Image.open(image_file)  # Открытие обрабатываемого файла
    resized_image = np.asarray(image.resize(INPUT_SHAPE[1:-1]).convert('L'))
    resized_image.resize(INPUT_SHAPE)          # Изменение размера изображения в соответствии со входом сети
    
    return model.predict(resized_image).argmax()
