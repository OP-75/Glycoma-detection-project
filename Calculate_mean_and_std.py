from pathlib import Path
import numpy as np
import cv2

path = r"D:\Folders to backup!!!\Glycoma DS\MyACRIMA_splitted\train"  # for windows

test_acrima = r"D:\Folders to backup!!!\Glycoma DS\MyACRIMA_splitted\test"
# test_g1020 = r"D:\Datasets\MyG1020\test"
# test_origa = r"D:\Datasets\MyOrigaFolder\test"
# test_githubDS = r"D:\Datasets\dataset\test"

imageFilesDir = Path(test_acrima)
files = list(imageFilesDir.rglob('*.jpg'))

# Since the std can't be calculated by simply finding it for each image and averaging like  
# the mean can be, to get the std we first calculate the overall mean in a first run then  
# run it again to get the std.

mean = np.array([0.,0.,0.])
stdTemp = np.array([0.,0.,0.])
std = np.array([0.,0.,0.])

numSamples = len(files)

for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.
    
    for j in range(3):
        mean[j] += np.mean(im[:,:,j])

mean = (mean/numSamples)

for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.
    for j in range(3):
        stdTemp[j] += ((im[:,:,j] - mean[j])**2).sum()/(im.shape[0]*im.shape[1])

std = np.sqrt(stdTemp/numSamples)

print(f"mean = {mean}")
print(f"std = {std}")


