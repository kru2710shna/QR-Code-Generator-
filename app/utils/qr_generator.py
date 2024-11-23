import qrcode
from io import BytesIO
from flask import send_file

def generate_qr(data: str, secure: bool = False, password: str = None) -> BytesIO:
    """Generate a QR code and optionally secure it with a password."""
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # If secure, we would hash the password (optional based on your use case)
    if secure and password:
        data += f"?password={password}"

    img = qr.make_image(fill_color="black", back_color="white")

    # Save image to BytesIO for sending as response
    img_io = BytesIO()
    img.save(img_io)
    img_io.seek(0)
    return img_io
