#first (pip install prcode) in terminal
#second (pip install pillow) in terminal
import qrcode

# Link for website will be our input data
input_data = "https://www.youtube.com/watch?v=c_WhJwgIDqE&t=6s"

#Creating an instance of qrcode (sets demensions)
qr = qrcode.QRCode(version=1, box_size=10,border=5)

#sets data
qr.add_data(input_data)
qr.make(fit=True)

#makes our image.
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
