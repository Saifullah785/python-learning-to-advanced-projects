
# importing the qrcode library

import qrcode as qr

img = qr.make("https://github.com/Saifullah785")
 
img.save("Github_profile_of_saif.png")

# solution 2
from PIL import Image

qr =  qr.QRCode(version=1,
                
                error_correction=qr.constants.ERROR_CORRECT_H,

                box_size=10,border=4,)
qr.add_data("https://github.com/Saifullah785/")

qr.make(fit= True)

img=qr.make_image(fill_color="black",back_color="white")

img.save('Github_profile_of_saif.png')



