# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:38:17 2022

@author: User
"""

from PIL import Image

img = Image.open('img01.jpg')

img.show() # 顯示照片

print(img.size) # 大小

print(img.filename) # 檔名

# ---------------------------

img1 = Image.new("RGB", (300, 200), "rgb(255,255,255)")
img1.show()
#img1.save('white.jpg') ### 存檔

img2 = Image.new("RGBA", (300, 200), "rgba(0,0,255,160)")  # A 代表alpha值, 0 代表全部透明
img2.show()
#img1.save('blue.png')

