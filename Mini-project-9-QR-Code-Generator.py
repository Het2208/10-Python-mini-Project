import qrcode
import os

url = input("Enter the URL: ")

folderPath = "E:\\Project\\Python-Mini-Project\\QRcodes"
os.makedirs(folderPath, exist_ok=True)  # create folder if not exists

filePath = os.path.join(folderPath, "qr.png")

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(filePath)

print("QR Code has been saved to " + filePath)