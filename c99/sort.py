import os
import shutil

i = input('Enter folder path')
list = os.listdir(i)
for something in list :
    name,ext = os.path.splitext(something)
    ext = ext[1:]
    if ext==" " :
        continue
    if os.path.exists(i+'/'+ext):
        shutil.move(i+'/'+something,i+'/'+ext+'/'+something)

    else:
        os.makedirs(i+'/'+ext)    
        shutil.move(i+'/'+something,i+'/'+ext+'/'+something)