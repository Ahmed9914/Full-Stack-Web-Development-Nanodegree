import os

def rename_files():

    file_list = os.listdir(r"G:\prank\prank")
    for file in file_list:
        print(file)
        saved_path = os.getcwd()
        os.chdir(r"G:\prank\prank")
        table = file.maketrans("", "", "0123456789")
        new_name = file.translate(table)
        os.rename(file, new_name)
    os.chdir(saved_path)

rename_files()
