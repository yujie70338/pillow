# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:56:10 2022

@author: User
"""

from PIL import Image

img = Image.open('img01.jpg')

img.show() # 顯示照片

w, h = img.size
print(w ,h)
#(320 240)

img1 =  img.resize((300,300), Image.NEAREST) # 改變圖片大小
img1.show()
print(img1.size)
# Image.NEAREST 最低品質
# ...
# Image.ANTIALIAS 最高品質

img2 = img.resize((w*2, h))
img2.show()

img3 = img.resize((w, h*2))
img3.show()

# ----------------------------------------------------------

img4 = img.rotate(45) # 旋轉45度
img4.show()

# ----------------------------------------------------------

img.transpose(Image.FLIP_LEFT_RIGHT).show()  # 左右轉置
img.transpose(Image.FLIP_TOP_BOTTOM).show()  # 上下轉置

# ----------------------------------------------------------

imggray = img.convert('L')  # 轉換灰階照片
imggray.show()

# ----------------------------------------------------------
imggray = img.convert('L')  # 轉換灰階照片
imggray.show()
x, y = imggray.size
# print(x,y)
# print(imggray.getpixel((300,200))) # 取得 (300,200) 位置的pixel值

for i in range(x):
    for j in range(y):
        if imggray.getpixel((i, j)) < 100:
            img.putpixel((i, j), (0)) # 設為黑色
        else:
            img.putpixel((i, j), (255)) # 設為白色
imggray.show()  # 變成黑白照片

