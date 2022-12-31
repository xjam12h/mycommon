import os
from glob import glob as gl
import json

def create_dir(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

def is_exists_file(filepath):
    return os.path.isfile(filepath)

def get_filename_list(dir,extension=""):
    filename= "*"+("."+extension if len(extension)!=0 else "")
    filepaths=gl(dir+filename)
    file_list=[os.path.splitext(os.path.basename(filepath))[0] for filepath in filepaths]
    return file_list

def save_file(save_filepath,data):
    with open(save_filepath,mode="w") as jf:
        json.dump(data,jf,indent=4)
