from PIL import Image
import os
 
def split(word): 
    return list(word)

store = split("hi")

# store = store + ".jpg"
# print(store)


# size = 0


def merged(alpha1,alpha2):
    alpha1 = "images/Alphabet/" + alpha1 + ".jpg"
    alpha2 = "images/Alphabet/" + alpha2 + ".jpg"
    img1 = Image.open(alpha1)
    img2 = Image.open(alpha2)
    img1 = img1.resize((50,50))
    img2 = img2.resize((50,50))
    img1_size = img1.size
    img2_size = img2.size
    new_image = Image.new('RGB',(2*img1_size[0],img1_size[1]),(250,250,250))
    new_image.paste(img1 ,(0,0))
    new_image.paste(img2,(img1_size[0],0))
    new_image.save("images/save/newww.jpg","JPEG")
    
    #This will rename all the files as and when they are added and the program runs.
    path = os.chdir(#Path to save folder
        )

    i = 1
    for file in os.listdir(path):
        new_file_name = "pic{}.jpg".format(i)
        os.rename(file , new_file_name)

	i += 1

    new_image.show()




x = 0 
for i in store:
    if(x+1 < len(store)):
    # i = i +'.jpg'
        store[x] = i
        merged(store[x],store[x+1])
        # print(i)
        x = x + 1
        # print(len(store))

    

# print(store)

        
    
    
    
 # return merged
    
    





