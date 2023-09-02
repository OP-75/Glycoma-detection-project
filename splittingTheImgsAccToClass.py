from PIL import Image
import csv
import os

allRows = []
with open(r"D:\Datasets\Glycoma dataset 1 - 6gb\G1020\G1020.csv") as file:
    myData = csv.reader(file)
    for row in myData:
        allRows.append(row)

allRows = allRows[1:] # skip first row since its header

print(len(allRows))
print(allRows[1])


path = r"D:\Datasets\Glycoma dataset 1 - 6gb\G1020\Images_Cropped"
dataAndLables = []


for row in allRows:
    imgName = row[0]
    imgObj = Image.open(os.path.join(path, imgName))
    label = int(row[1])

    dataAndLables.append((imgObj, label, imgName)) # img is the name of the image



print(len(dataAndLables))


class1path = r"D:\Datasets\MyG1020\class1"
class0path = r"D:\Datasets\MyG1020\class0"

for img,label,name in dataAndLables:

    # print(img,label,name)

    if(label==0):
        img.save(os.path.join(class0path, name))
    elif(label==1):
        img.save(os.path.join(class1path, name))
    else:
        print(f"Error in saving image {name}")
        break





