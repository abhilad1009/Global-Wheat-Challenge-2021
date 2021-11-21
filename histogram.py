import matplotlib.pyplot as plt
import cv2
import os

images = []
path = "../Mission Begins/test/"
for image in os.listdir(path):
    images.append(image)

for image in images:
     img = cv2.imread("%s%s"%(path, image))    # Load the image 
     channels = cv2.split(img)       # Set the image channels
     colors = ("b", "g", "r")        # Initialize tuple 
     plt.figure()    
     plt.title("Color Histogram")
     plt.xlabel("Bins")
     plt.ylabel("Number of Pixels")

     for (i, col) in zip(channels, colors):       # Loop over the image channels
          hist = cv2.calcHist([i], [0], None, [256], [0, 256])   # Create a histogram for current channel
          plt.plot(hist, color = col)      # Plot the histogram
          plt.xlim([0, 256])