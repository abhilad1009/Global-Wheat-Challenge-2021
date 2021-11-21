import os
import glob
import pandas as pd
import tqdm

data=pd.read_csv('submission_normal_v1.csv')
class_id=0
boxcount=0
noboxcount=0
for idx,row in data.iterrows():

    print_buffer = []    
    # boxes=row['BoxesString'].split(';')
    boxes=row['PredString'].split(';')
    if boxes[0]=="no_box":
        noboxcount+=1
        continue
    for j in boxes:
            boxcount+=1
            box=[int(cord) for cord in j.split(" ")]
            b_center_x = (box[0] + box[2]) / 2 
            b_center_y = (box[1] + box[3]) / 2
            b_width    = (box[2] - box[0])
            b_height   = (box[3] - box[1])
            
            # Normalise the co-ordinates by the dimensions of the image
            image_w, image_h = 1024,1024
            b_center_x /= image_w 
            b_center_y /= image_h 
            b_width    /= image_w 
            b_height   /= image_h 
            
            #Write the bbox details to the file 
            print_buffer.append("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(class_id, b_center_x, b_center_y, b_width, b_height))
        
    # Name of the file which we have to save 
    
    save_file_name = 'labels/test2/'+row['image_name']+'.txt'
    
    # Save the annotation to disk
    print("\n".join(print_buffer), file= open(save_file_name, "w"))

print(boxcount)
print(noboxcount)