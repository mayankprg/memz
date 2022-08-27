
from PIL import Image, ImageDraw, ImageFont
import os


import io

# path = os.path.dirname(__file__)

def textOnImg(text: str, image):
    if len(text) > 20:
        return "Lenght to big"
    img = Image.open(image)
    img1 = ImageDraw.Draw(img)
    # font = ImageFont.load_default()

    font = ImageFont.truetype("arial", size=20)
    img1.text((2, 2), text, fill=(225, 0, 0), font=font, stroke_width=5, stroke_fill="#000")
    buff = io.BytesIO()
    img.show()
    # img.save(buff, format=)

    return buff
   
