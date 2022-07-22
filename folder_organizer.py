import os
def createIfNotPresent(folder_name):
    if(not(os.path.isdir(folder_name))):
        os.mkdir(folder_name)
def move_to_respective_folder(name, folder):
    path = folder+"/"+name
    # print(path)
    createIfNotPresent(folder)
    os.rename(name, path)
docs = [".pdf", ".docx", ".txt"]
setups = [".exe"]
pictures = [".jpg", ".png"]
videos = [".mp4"]
# others = []
file_list = os.listdir()
file_list.remove("organizing_folder.py")
# file_list.remove("check.py")
# print(file_list)
exclude = ["Docs", "Videos", "Setups", "Others", "Pictures"]
for file in file_list:
    if file not in exclude:
        ext = os.path.splitext(file)
        # print(ext)
        if ext[1] in docs:
            move_to_respective_folder(file, "Docs")
        elif ext[1] in setups:
            move_to_respective_folder(file, "Setups")
        elif ext[1] in pictures:
            move_to_respective_folder(file, "Pictures")
        elif ext[1] in videos:
            move_to_respective_folder(file, "Videos")
        else:
            move_to_respective_folder(file, "Others")