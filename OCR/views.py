from django.shortcuts import render
from PIL import Image
from .forms import ImageForm
from .image import text1
import pytesseract

# Create your views here.
def homePage(request):
     return render(request, "index.html") 




def convert(request):
    if request.method=="POST":
        form=ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request, "convert.html",{"obj":obj}) 
        else:
            form=ImageForm()
        img = Image.open("static/images/Passport-1.jpg")
        text = pytesseract.image_to_string(img)

        print(text)
        
        return render(request, "convert.html",{"img":img, "form":form})

def text2(request):
    text1()




    


        
    


   
   
    


    