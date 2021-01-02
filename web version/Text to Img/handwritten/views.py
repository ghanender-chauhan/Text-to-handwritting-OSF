from django.shortcuts import render, redirect, HttpResponse
from PIL import Image
import shutil

def copy_file():
    source = "media/images/cr/@.jpg"
    destination = "media/images/save/@.jpg"
    shutil.copyfile(source, destination) 

def copy_intial_file():
    copy_file()
    source = "media/images/cr/line.jpg"
    destination = "media/images/save/line.jpg"
    shutil.copyfile(source, destination) 

def normalize(str):
    bad_chars = [';', ':', ',', '!', "."]
    str = str.lower()
    for i in bad_chars :
        str = str.replace(i, '')
    str = str.replace(" ", "@")
    return str


def solve(str):
    str = normalize(str)
    i=1
    pos = 1
    h=1
    copy_intial_file()
    for ch in str:
        if ch=='@' or ch.isalpha():
            pass
        else:
            continue
        i = i + 1
        pos = pos + 1
        if pos%52 == 0:
            i = 2
            h = h+1
            timg1 = Image.open("media/images/save/line.jpg")
            timg2 = Image.open(f"media/images/save/@.jpg")
            timg1_size = timg1.size
            timg2_size = timg2.size

            tnew_image = Image.new('RGB',(timg1_size[0], timg1_size[1]+35+timg2_size[1]),(250,250,250))
            tnew_image.paste(timg1 ,(0,0))
            tnew_image.paste(timg2, (0, 35+timg1_size[1]))

            tnew_image.save("media/images/save/line.jpg","JPEG")
            copy_file()

        print(ch)
        img1 = Image.open("media/images/save/@.jpg")
        img2 = Image.open(f"media/images/cr/{ch}.jpg")

        img1_size = img1.size
        new_image = Image.new('RGB',(i*150,150),(250,250,250))
        print("final size ", i*150, 150)
        new_image.paste(img1 ,(0,0))
        new_image.paste(img2,(img1_size[0], 0))

        new_image.save("media/images/save/@.jpg","JPEG")

    timg1 = Image.open("media/images/save/line.jpg")
    timg2 = Image.open(f"media/images/save/@.jpg")
    timg1_size = timg1.size
    timg2_size = timg2.size

    tnew_image = Image.new('RGB',(timg1_size[0], timg1_size[1]+20+timg2_size[1]),(250,250,250))
    tnew_image.paste(timg1 ,(0,0))
    tnew_image.paste(timg2, (0, 20+timg1_size[1]))

    tnew_image.save("media/images/save/line.jpg","JPEG")



def convert(request):
    if request.method == "POST":
        rawText = request.POST.get('rawtext')
        print("request post ", request.POST)
        print("raw text", rawText)
        solve(rawText)
        print("done")
        return render(request, 'index.html', {'solved':'yes', 'text':rawText})
    return render(request, 'index.html')

    