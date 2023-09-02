from PIL import Image
import csv
import os



path = r"D:\Datasets\glycoma dataset 2 - 421mb\ACRIMA\Images"
dataAndLables = []

str = "img567_g_ACRIMA.jpg"
myl = str.split("_")
print(myl)
str = "img567_ACRIMA.jpg"
myl = str.split("_")
print(myl)

for imgName in os.listdir(path):

    imgObj = Image.open(os.path.join(path, imgName))

    if(imgName.split("_")[1]=="g"):
        label = 1
    else:
        label = 0

    dataAndLables.append((imgObj, label, imgName)) # img is the name of the image



print(len(dataAndLables))


class1path = r"D:\Datasets\MyACRIMA\class1"
class0path = r"D:\Datasets\MyACRIMA\class0"

for img,label,name in dataAndLables:

    # print(img,label,name)

    if(label==0):
        img.save(os.path.join(class0path, name))
    elif(label==1):
        img.save(os.path.join(class1path, name))
    else:
        print(f"Error in saving image {name}")
        break





