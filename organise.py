import os
import shutil

from_dir = "C:/Users/fritz/OneDrive/Desktop/VIsual Studio Code/C102_assets-main"
to_dir = "C:/Users/fritz/OneDrive/Desktop/VIsual Studio Code"

listoffiles = os.listdir(from_dir)
print(listoffiles)

for file_name in listoffiles:
    name,extenstion = os.path.splitext(file_name)
    print(name,extenstion)
    
    if extenstion == '':
        continue
    if extenstion in ['.gif','.png','.jfif','.jpg','.jpeg']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'imagefiles'
        path3 = to_dir + '/' + 'imagefiles' + '/' + file_name

        if os.path.exists(path2):
            print("Moving! " + file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving"+ file_name + "..................")
            shutil.move(path1,path3)