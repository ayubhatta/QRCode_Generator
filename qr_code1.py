# Use this code if you want to generate a plain QR Code . 
import qrcode as qr

img = qr.make("https://www.linkedin.com/in/ayub-bhatta-31a6b3269/")
img.save("Ayub_LinkedIn.png")
img.show()
