from PIL import Image

 
def split(word): 
    return list(word)

store = split("rupin")

# store = store + ".jpg"
# print(store)


# size = 0
for i in store:
    i = i +'.jpg'

print(store)    



def merged():
    img1 = Image.open("images/Alphabet/e.jpg")
    img2 = Image.open("images/Alphabet/e.jpg")
    img1 = img1.resize((50,50))
    img2 = img2.resize((50,50))
    img1_size = img1.size
    img2_size = img2.size
    new_image = Image.new('RGB',(2*img1_size[0],img1_size[1]),(250,250,250))
    new_image.paste(img1 ,(0,0))
    new_image.paste(img2,(img1_size[0],0))
        

    # return merged
    
    




# new_image.save("images/save/new.jpg","JPEG")
# new_image.show()