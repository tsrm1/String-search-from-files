import os
text = input("input text : ")
path = '.'
# os.chdir(path)
# def getfiles(path):
#     f = 0
#     file_list = []
#     os.chdir(path)
#     files = os.listdir()
#     print("Files: ", files)
#     for file_name in files:
#         abs_path = os.path.abspath(file_name)
#         if os.path.isdir(abs_path):
#             getfiles(abs_path)
#         if os.path.isfile(abs_path):
#             f = open(file_name, "r")
#             if text in f.read():
#                 f = 1
#                 print(text + " found in ")
#                 final_path = os.path.abspath(file_name)
#                 print(final_path)
#                 return True
#     if f == 1:
#         print(text + " not found! ")
#         return False

# getfiles(path)




# files = []
# def list_dir(current_dir='.'):
#     os.chdir(current_dir)
#     content = os.listdir(current_dir)

#     for file in content:
#         if os.path.isfile(os.path.join(current_dir, file)):
#             files.append(file)
#         # if os.path.isdir(os.path.join(current_dir, file)) and not file.startswith('.'):
#         #     list_dir(file)


# list_dir()
# print(files)


files = [] 

def search_text(file_name, text):
    with open(file_name, 'r', encoding='utf-8') as file:
        if text in file.read():
            return True
        else:
            return False

def list_dir(path='.'):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in list_dir(path):
    if search_text(file, text):
        print(f"[{file}]: {text} - found!")
    else:
        print(f"[{file}]: {text} - NOT found!")




