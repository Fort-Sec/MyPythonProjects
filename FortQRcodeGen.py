# install all the libraries needed / # create a function that collects a text and coverts it to QR code

from asyncio import constants
from curses.panel import version
import qrcode 

def generate_QRcode(text):

    QR = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    # create a function that collects a text and coverts it to QR code
# save the QR code as an image
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('QRimg.png')

url = input('Enter your url:')
generate_QRcode()    
 
# run the function
