from PIL import Image
import csv
import os

allRows = []
with open(r"D:\Datasets\Glycoma dataset 1 - 6gb\ORIGA\OrigaList.csv") as file:
    myData = csv.reader(file)
    for row in myData:
        allRows.append(row)

print(len(allRows))




path = r"D:\Datasets\Glycoma dataset 1 - 6gb\ORIGA\Images_Square"
dataAndLables = []

for indx,img in enumerate(os.listdir(path)):
    imgObj = Image.open(os.path.join(path, img))
    if(allRows[indx+1][1]==img):
        label = int(allRows[indx+1][4])
        dataAndLables.append((imgObj, label, img)) # img is the name of the image

    else:
        print("Error!")
        print(img)
        break


print(len(dataAndLables))


class1path = r"D:\Datasets\MyOrigaFolder\class1"
class0path = r"D:\Datasets\MyOrigaFolder\class0"

for img,label,name in dataAndLables:
    if(label==0):
        img.save(os.path.join(class0path, name))
    elif(label==1):
        img.save(os.path.join(class1path, name))
    else:
        print(f"Error in saving image {name}")
        break


