from pathlib import Path
import numpy as np
import cv2

train_path = r"D:\Datasets\dataset\train"  # for windows
test_path = r"D:\Datasets\dataset\test"  # for windows

imageFilesDir = Path(test_path)
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

print(mean)
print(std)