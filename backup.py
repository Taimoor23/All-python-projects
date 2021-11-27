import os
import shutil

path=input("enter the name of the directory to be sorted:-")

list_dir=os.listdir(path)

for file in list_dir:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    #this forces the next iteration even there is a folder
    if ext=='':
        continue

    #this may move the file to the directory
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)    
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)  
