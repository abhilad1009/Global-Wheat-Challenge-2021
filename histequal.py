import os
import numpy as np
import albumentations as A
import cv2

def infunc(img_path):
  img=cv2.imread(img_path)
  img=np.array(img)
  return img

target_image=['train/'+i for i in os.listdir('train')[:]]

aug = A.Compose([A.HistogramMatching(target_image,blend_ratio=(0.5,0.6), p=1, read_fn=infunc)])


for i in os.listdir('train'):
  image = cv2.imread('train/'+i)
  result = aug(image=image)
  cv2.imwrite('train1/'+i,result['image'])


# transform=A.augmentations.transforms.CLAHE(clip_limit=1.5,p=1)

# for i in os.listdir('train1'):
#   image = cv2.imread('train1/'+i)
#   result = transform(image=image,mask=image)
#   cv2.imwrite('train2/'+i,result['image'])