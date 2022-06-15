# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:09:22 2022

@author: User
"""

from PIL import Image, ImageFilter

img = Image.open('./astro.jpg.jpg')
#filtered_img = img.convert('L')
#print(img.format)
#print(img.size)
#print(img.mode)
#print(dir(img))
#filtered_img.save("blur.png",'png') 
#PNG supports image filters which JPEG don't
#resize = filtered_img.resize((300,300))
#resize.save("grey.png",'png')  
#filtered_img.show()

#CropImages
#box=(100,100,400,400)
#region = filtered_img.crop(box)
#region.save("grey.png",'png')  


#astro.jpg
print(img.size)
new_img = img.resize((400,400))
new_img.save('thumbnail.jpg')