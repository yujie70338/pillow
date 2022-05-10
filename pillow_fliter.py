from PIL import Image,ImageFilter

img = Image.open("panda.jpg")
img.show()

imgFilter=img.filter(ImageFilter.BLUR).show()   #模擬
#imgFilter.save("BLUR.jpg") 
imgFilter=img.filter(ImageFilter.CONTOUR).show()#輪廓
#imgFilter.save("CONTOUR.jpg")
img.filter(ImageFilter.EMBOSS).show()  #浮雕
img.filter(ImageFilter.SHARPEN).show() #銳化

img.filter(ImageFilter.DETAIL).show() # 細節增強
img.filter(ImageFilter.EDGE_ENHANCE).show() # 邊緣增強
img.filter(ImageFilter.EDGE_ENHANCE_MORE).show() # 深度邊緣增強
img.filter(ImageFilter.FIND_EDGES()).show() # 邊緣資訊濾鏡
img.filter(ImageFilter.SMOOTH()).show()  # 平滑
img.filter(ImageFilter.SMOOTH_MORE()).show() # 深度平滑

