from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


### Word Cloud ###
text_file = open('../text.txt')
text = text_file.read()
worldcloud = WordCloud().generate(text)
plt.figure(figsize=(12,12))
plt.imshow(worldcloud)
plt.axis('off')
plt.show()


char_mask = np.array(Image.open('circle.png'))
worldcloud = WordCloud(background_color='black', mask=char_mask).generate(text)
plt.figure(figsize=(8,8))
plt.imshow(worldcloud)
plt.axis('off')
plt.show()