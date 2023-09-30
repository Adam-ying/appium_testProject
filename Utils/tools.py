import os

# 删除目录下的文件
def del_path_files(path:str):
    file_list = os.listdir(path)

    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        os.remove(file_path)