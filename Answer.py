#http://stackoverflow.com/questions/44076094/how-to-rename-all-the-files-in-a-folder-in-numeric-order/44076350#44076350
#! /usr/bin/python3.4
import os

x = 0
photo_dir=os.path.dirname(__file__)+"\\photos\\"
extension = ".jpg"
for i in os.listdir(photo_dir): 
    if  i.endswith(extension):
        os.rename(photo_dir+i, photo_dir+str(x)+extension)
        x+=1