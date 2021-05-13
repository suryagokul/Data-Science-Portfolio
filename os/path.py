import os

print(os.environ.get('USERPROFILE'))       #  USERPROFILE is a root directory in windows,returns C:\Users\SURYA. incase of linux use os.environ.get('HOME')

cwd = os.getcwd()

# check if path exists or not,returns True or False.
print(os.path.exists(cwd + 'new'))

# check given path is directory or not
print(os.path.isdir("folder"))

# check given path is file or not
print(os.path.isfile("walk.py"))


print(os.path.basename('folder/sub_folder'))   # returns sub_folder i.e base name

print(os.path.dirname('folder/sub_folder'))    # returns folder i.e dirname


print(os.path.split('folder/sub_folder'))     # splits based on / returns ('folder', 'sub_folder')

print(os.path.splitext('os_demo1.py'))        # splits text and extension. returns ('os_demo1', '.py')


directory = os.getcwd()      # C:\Users\desktop\os

print(os.path.join(directory, "folder"))    # concatenates path which returns C:\Users\desktop\os\folder
