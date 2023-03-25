import qrcode  
import Image 

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 1,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "black")
    img.save("qrimage.png")

url = input("Enter your URL: ")
generate_qrcode(url)