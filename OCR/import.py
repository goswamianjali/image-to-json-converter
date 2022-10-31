import pytesseract
path_to_tesseract = r'/usr/bin/tesseract'
pytesseract.tesseract_cmd = path_to_tesseract
#tess.pytesseract.tesseract_cmd = r'usr/bin/tesseract.exe'
from PIL import Image


img = Image.open("../static/images/Passport-1.jpg")

text = pytesseract.image_to_string(img)

print(text)
import json
json.loads(text)

import requests
json.loads(requests)

json = requests.get('http://127.0.0.1:8000/convert/').json()