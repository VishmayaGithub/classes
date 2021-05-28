import os
import shutil
import time
import datetime

def main():
    path =input('Enter Path : ')
    days =input('Enter last date')

    pathexits = os.path.exists(path)
    print(pathexits)
    if(pathexits == 'True'):
        files = os.listdir(path)
        seconds  = time.time() - days*24*60*60
        for root,file in files :
            
            full_path = os.path.join(root, file)
            presentTime = datetime.datetime.now()
            file_cre_time = datetime.datetime.fromtimestamp(os.path.getctime(full_path))
            no_of_days = (presentTime - file_cre_time).days
            if(no_of_days>days):
                os.remove(full_path)
                print('You have removed',full_path)
    else:
        print('Enter valid path')           

main()        