import qrcode
import image
qr=qrcode.QRCode(version=15,box_size=10,border=5)
#version is the qrcode version higher the number more complicated the code will be
#box_size is the size of box where the code will be displayed
#border is the white border of the  code image 

data="www.google.com"
qr.add_data(data)
img=qr.make_image(fill_color='black',black_color="white")
img.show()#shows the image
"""
you can save the file via
image.save("image.png")
"""
