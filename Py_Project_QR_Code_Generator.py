# Installing Py lib
# Create a function that collcets a text and converts it inot qrcode
# save a code as image 
# run the function 

import qrcode

# Define the data you want to encode in the QR code
data = "Hello, QR Code!"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save("my_qr_code.png")

# Display the QR code
img.show()


   
    
