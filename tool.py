import os
import time
import shutil

path = ""

def path_check():
    if(os.getcwd() == "C:\\Users\\pro\\Desktop"):
        return os.getcwd()
    else:
        return False
    
def confirm_path(path):
    print path+"\\desktop_files\\"
    return os.path.exists(path+"\\desktop_files\\")


def check_create_dir(path):
    if path and not confirm_path(path):
        os.mkdir("desktop_files")

def move_files(path):
    for fil in os.listdir(path):
        src = os.path.join(path,fil)
        dest = os.path.join(path,"desktop_files")
        if fil == "tool.py":
            continue
        if(os.path.isfile(fil)):
            shutil.copy(src,dest)
            os.remove(fil)


if __name__ == "__main__":
    path = path_check()
    check_create_dir(path)
    move_files(path)












files_on_desktop = os.listdir(path)

for file in files_on_desktop:
    print file



#def pro(ra,dirs,files):
    #global all_files
    #all_files.append(files)

#os.path.walk(path,pro,"er")

#print all_files
