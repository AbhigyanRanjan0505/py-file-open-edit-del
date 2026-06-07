import os
import shutil
import time

def delete_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")

    else:
        print(f"Unable to delete the "+path)


def delete_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")

    else:
        print("Unable to delete the "+path)


def get_file_folder_exist_time(path):
    ctime = os.stat(path).st_ctime
    return ctime


path = input("Path to the folder to delete old files: ")
seconds = time.time() - 2592000

folder_delete_count = 0
file_delete_count = 0

if os.path.exists(path):
    for root, folders, files in os.walk(path):
        if seconds >= get_file_folder_exist_time(root):
            delete_folder(root)
            folder_delete_count += 1
            break
        else:
            for folder in folders:
                folder_path = os.path.join(root, folder)

                if seconds >= get_file_folder_exist_time(folder_path):
                    delete_folder(folder_path)
                    folder_delete_count += 1

            for file in files:
                file_path = os.path.join(root, file)

                if seconds >= get_file_folder_exist_time(file_path):
                    delete_file(file_path)
                    file_delete_count += 1
    else:
        if seconds >= get_file_folder_exist_time(path):
            delete_file(path)
            file_delete_count += 1
else:
    print(f"[{path}] is not found")
    file_delete_count += 1

print("Files and folders deleted successfully")
