def text1():
     global img

     import pytesseract
     path_to_tesseract = r'/usr/bin/tesseract'
     pytesseract.tesseract_cmd = path_to_tesseract
     from PIL import Image

     def program():

         img = Image.open("static/images/Passport-1.jpg")
         text = pytesseract.image_to_string(img)

         print(text)

     program()