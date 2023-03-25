import pillow 

from PIL import Image

def resize_image(size1, size2):

    image = Image.open('')

    print(f"Current size: {image.size}")

    resized_image = Image.resize((size1, size2))

    resized_image.save('')

size1 = int(input('Enter Length: '))
size2 = int(input('Enter width: '))

resize_image()
