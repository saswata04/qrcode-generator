import qrcode

data = "It's me Mario!"

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="green",
                    back_color="white")
img.save('MyQRCode2.png')

# REFERENCE: https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/
