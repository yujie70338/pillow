# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:16:45 2022

@author: User
"""

from PIL import Image,ImageDraw
from PIL import ImageFont  # 繪製文字

img = Image.open('img01.jpg')
draw1 = ImageDraw.Draw(img) # 利用draw方法建立畫布

img2 = Image.new("RGB", (400,300), "lightgray")
# img2.show()
draw2 = ImageDraw.Draw(img2) # 利用draw方法建立畫布

# ---------------------------------------------
# 畫布的方法 point() 繪點
# 畫布的方法 line() 繪線
for i in range(0,400,10):  # 0 到 400 每隔10 pixel
    for j in range(0,300,10):    
        draw2.point([(i,j)],fill="red")  
#繪直線
for i in range(0,400,10):
    draw2.line([(i,300),(200,150)],width=2,fill="blue") 
    
img2.show()
# -----------------------------------------------------------------


# 畫布的方法 rectangle() 繪矩形
# 畫布的方法 ellipse() 繪圓形、橢圓形
# 畫布的方法 polygon() 繪多邊形
# 畫文字 text() 
# windows的系統字型位於 C:\Windows\Fonts ， 對想選擇的字形點選右鍵 -> 內容 -> 安全性，複製該物件名稱
# myfont=ImageFont.truetype("C:\Windows\Fonts\mingliu.ttc",16) 設定文字和大小

img3= Image.new("RGB", (400,300), "lightgray")
# img3.show()
draw3 = ImageDraw.Draw(img3) # 利用draw方法建立畫布

#繪多邊形
draw3.polygon([(200,100),(350,150),(50,150)],fill="blue",outline="red")#屋頂
#繪矩形
draw3.rectangle((100,150,300,250),fill="green",outline="black") #房間
#繪圓
draw3.ellipse((300,40,350,90),fill="red")#太陽 
#繪橢圓
draw3.ellipse((60,80,100,100),fill="white") #白雲一   
draw3.ellipse((100,60,130,80),fill="white") #白雲二 
#繪文字
draw3.text((120,170),"im happy",fill="orange")

myfont=ImageFont.truetype("C:\Windows\Fonts\mingliu.ttc",16) #字型
draw3.text((120,200),"宇傑",fill="red",font=myfont) #文字
img3.show()
# img3.save("house.png")
