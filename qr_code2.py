# Use this code for generating your QR Code as your preferences.
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, 
                   box_size=10, border=5 )  # version=1 means smallest size

qr.add_data("https://www.instagram.com/ayub_bhatta/")  # add your link you want to convert to a qrcode
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("Ayub_Instagram.png") # will save the generated qr code to your project folder
img.show()  # displays the image
