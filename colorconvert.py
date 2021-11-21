import os
import numpy as np
import cv2
import tqdm

fol="Gray"
os.makedirs(fol,exist_ok=True)

for i in tqdm.tqdm(os.listdir('test')):
  image = cv2.imread('test/'+i,cv2.IMREAD_UNCHANGED)
#   image[:,:,0] = np.zeros([image.shape[0], image.shape[1]])
  image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image=cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

  cv2.imwrite(fol+'/'+i,image)
