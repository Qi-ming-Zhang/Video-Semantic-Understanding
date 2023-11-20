'''测试文件'''
import io
import os

import requests
from PIL import Image
from model import get_caption_model, generate_caption





caption_model=get_caption_model()


def predict():
    captions = []
    CNcaptions = []
    pred_caption = generate_caption('test2.png', caption_model)


    captions.append(pred_caption)

    for _ in range(3):
        pred_caption = generate_caption('test2.png', caption_model, add_noise=True)
        print(pred_caption)
        if pred_caption not in captions:
            captions.append(pred_caption)



predict()