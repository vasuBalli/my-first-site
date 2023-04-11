from PIL import Image

def text_render(text):
    bg = Image.open("og.jpg")
    base_img = Image.open("base_img.png")
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
    for letter in text:
        if letter == " ":
            img  = Image.open("images/blank.png")
            img.thumbnail((1365,2048), Image.Resampling.LANCZOS)
            base_img.paste(img,(x,500),img)
            x+=60
        else:
            
            img  = Image.open("images/"+letter.upper()+".png")
            img.thumbnail((500,500), Image.Resampling.LANCZOS)
            base_img.paste(img,(x,500),img)
            x+=80
        
    bg.paste(base_img,(y,920),base_img)
    return bg.show()
bg = Image.open("base_img.png")
print("1365, 2048,625",682/8)
text_render("vasuvvrko")