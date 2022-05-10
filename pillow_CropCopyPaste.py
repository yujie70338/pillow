# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:33:09 2022

@author: User
"""

from PIL import Image

img = Image.open('img01.jpg')

img.show() # 顯示照片
w, h = img.size
# print(w ,h) #(320 240)

img1 = img.crop((0,0,160,160))  # (左上x, 左上y, 右下x, 右下y)  # 裁切照片
img1.show()

# ------------------------------------------

imgcopy = img.copy()  # 複製照片
imgcopy.show() 

# ------------------------------------------

panda = Image.open('panda.jpg')
panda.show()

pandacopy = panda.copy()

panda1 = panda.crop((190,184,415,350))
panda1.show()  # 裁切出小panda
panda.paste(panda1, (40,30)) # 貼上合成照片 # 底圖.paste(圖,(位置))
panda.show()

panda2 = panda1.transpose(Image.FLIP_LEFT_RIGHT) # 貼上合成照片
panda.paste(panda2, (220,30))
panda.show()
