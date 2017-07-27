import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/media/milton/Data/embedded systems/python/python/secret message/message")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/media/milton/Data/embedded systems/python/python/secret message/message")
    # (2) for each file, rename filename
    for file_name in file_list:
        print(file_name)
        print("New name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
