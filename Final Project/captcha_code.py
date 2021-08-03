# -*- coding: utf-8 -*-
"""captcha_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Q9MbcTHHFGYdoY80TsLbnx5gghu657w
"""

!pip install captcha

from captcha.image import ImageCaptcha
import random as r
import string

length = 6
captcha_text = ''
characters = string.ascii_letters + string.digits

for i in range(length):
  captcha_text += r.choice(characters)
  
img = ImageCaptcha(width = 280, height = 90)
image = img.generate(captcha_text)
img.write(captcha_text, 'CAPTCHA.png')