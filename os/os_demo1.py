import os

# returns present working directory in the form of string
print(f"current working directory is : {os.getcwd()}")

# os.getcwdb() returns present working directory in the form of bytes which is deprecated in windows.

# returns list of files and folders in current directory
print(os.listdir())

os.mkdir("demo_folder")

print("Created demo_folder..")

os.makedirs("folder/subfolder")

print("created folder and subfolder also using makedirs..")

print("Before deleting folders in our dir are : ",os.listdir())

os.rmdir("demo_folder")

print("After deleting demo folder current folders are : ",os.listdir())

os.removedirs("folder/subfolder")

print("After deleting folder & subfolder  : ",os.listdir())