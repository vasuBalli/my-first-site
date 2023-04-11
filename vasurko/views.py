from django.shortcuts import render
from django.http import HttpResponse
from vasurko.models import Title

import random
from PIL import Image

def text_render(text):
    bg = Image.open("vasurko/static/imgs/og.jpg")
    base_img = Image.open("vasurko/static/imgs/base_img.png")
    pngs=[]
    x = 0
    y = -120
    if len(text) == 1:
        y += 625
    elif len(text) == 2:
        y +=625-57
    elif len(text) == 3:
        y +=625-57-57
    elif len(text) == 4:
        y +=625-57-85
    elif len(text) == 5:
        y +=625-57-85-57
    elif len(text) == 6:
        y +=625-57-170    
    elif len(text) == 7:
        y +=625-114-130
    elif len(text) == 8:
        y +=625-114-130-30
    elif len(text) == 9:
        y +=625-114-130-30-57
    elif len(text) == 10:
        y +=625-114-130-30-85
    elif len(text) == 11:
        y +=625-114-130-30-85-57
    elif len(text) == 12:
        y +=625-114-130-30-85-85
    for letter in text:
        if letter == " ":
            img  = Image.open("vasurko/static/imgs//blank.png")
            img.thumbnail((1365,2048), Image.Resampling.LANCZOS)
            base_img.paste(img,(x,500),img)
            x+=60
        else:
            
            img  = Image.open("vasurko/static/imgs/"+letter.upper()+".png")
            img.thumbnail((500,500), Image.Resampling.LANCZOS)
            base_img.paste(img,(x,500),img)
            x+=80
        
    bg.paste(base_img,(y,920),base_img)
    name = random.randint(1,1000)
    if text =="":
        return "empty input"
    return bg.save('vasurko/static/imgs/'+text+'.jpg')

# Create your views here.
def home(request):
    name = Title.objects.all()
    
    return render(request,'text_editor.html',{"name":name})
def form(request,pk):
    name = request.GET.get('name1')
    if pk == "4":
        if name:
            text_render(name)
    y = {"pkk":pk,"x": name}
    
    
    return render(request,'form.html',y)

