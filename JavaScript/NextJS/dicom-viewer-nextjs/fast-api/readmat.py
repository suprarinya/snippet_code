from scipy.io import loadmat
import numpy as np
import pandas as pd

mat = loadmat('IIIT5K/traindata.mat')

keys = []
for key in mat.keys():
    keys = np.array(key)

print(keys)

data = np.array(mat['traindata'])
df = pd.DataFrame(data[0])
# print(df.head())
# print(df.columns)
# print(data['GroundTruth'][0][0], type(data['GroundTruth'][0][0]))
# print(data['ImgName'][0][0], type(data['ImgName'][0][0]))

totalcount = len(data[0])
images, labels = [], []
for i in range(totalcount):
    groundtruth, imgname = data['GroundTruth'][0][i][0], data['ImgName'][0][i][0]
    if groundtruth: labels.append(groundtruth)
    if imgname: images.append(imgname)

print(images, totalcount)



# df.to_csv('IIIT5K/testdata.csv')




# df = pd.DataFrame(mat['testdata'])

# print(keys)