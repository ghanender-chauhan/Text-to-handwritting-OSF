from django.shortcuts import render, redirect, HttpResponse
from PIL import Image

fill_color = (255,255,255)
lineSpacing = 20

def normalize(str):
    """
    In current version we are not supporting special characters, So
    this is utility function to filter them out
    """
    bad_chars = [';', ':', ',', '!', "."]
    str = str.lower()
    for i in bad_chars :
        str = str.replace(i, '')
    str = str.replace(" ", "@")
    return str

def change_background(img):
    """
    Utility function to change background it accepts a image object and
    returns modified img
    """
    img = img.convert("RGBA")   
    if img.mode in ('RGBA', 'LA'):
        background = Image.new(img.mode[:-1], img.size, fill_color)
        background.paste(img, img.split()[-1]) # omit transparency
        img = background
    return img


def copy_file():
    source = "media/images/cr/@.png"
    destination = "media/images/save/@.png"
    img = Image.open(source)
    img = change_background(img)
    img.save(destination)


def copy_intial_file():
    copy_file()
    source = "media/images/cr/line.png"
    destination = "media/images/save/line.png"
    img = Image.open(source)
    img = change_background(img)
    img.save(destination)

def mergeImg(img1, img2, horizontally):
    """
    It takes two images object and its orientation and returns the merged object.
    """
    img1Size = img1.size
    img2Size = img2.size
    newImgSize = (img1Size[0]+img2Size[0], img1Size[1]+img2Size[1])

    newImage = None
    if horizontally:
        newImage = Image.new('RGB',(newImgSize[0],img1Size[1]), fill_color)
        newImage.paste(img1 ,(0,0))
        newImage.paste(img2,(img1Size[0], 0))
    else:
        newImage = Image.new('RGB',(img1Size[0], newImgSize[1]+lineSpacing), fill_color)
        newImage.paste(img1 ,(0,0))
        newImage.paste(img2,(0, img1Size[1]+lineSpacing))
    return newImage
    



def solve(str):
    str = normalize(str)
    pos = 1
    copy_intial_file()
    for ch in str:
        if ch=='@' or ch.isalpha():
            pass
        else:
            continue

        if pos%62 == 0:
            pos = 1
            timg1 = Image.open("media/images/save/line.png")
            timg2 = Image.open(f"media/images/save/@.png")
            tnew_image = mergeImg(timg1, timg2, False)
            tnew_image.save("media/images/save/line.png","PNG")
            copy_file()

        img1 = Image.open("media/images/save/@.png")
        img2 = Image.open(f"media/images/cr/{ch}.png")
        img2 = change_background(img2)
        newImg = mergeImg(img1, img2, True)
        newImg.save("media/images/save/@.png","PNG")
        pos += 1
    img1 = Image.open("media/images/save/line.png")
    img2 = Image.open(f"media/images/save/@.png")
    new_image = mergeImg(img1, img2, False)
    new_image.save("media/images/save/line.png","PNG")
    


def convert(request):
    if request.method == "POST":
        rawText = request.POST.get('rawtext')
        solve(rawText)
        return render(request, 'index.html', {'solved':'yes', 'text':rawText})
    return render(request, 'index.html')

    