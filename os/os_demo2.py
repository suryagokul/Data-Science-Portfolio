import os

os.mkdir("my_dir")

print("created my_dir")

# for renaming files 
os.rename("my_dir", "new_directory")

print("Renamed my_dir to new_directory")


# to get all stats about the given file or folder
print(os.stat("new_directory"))

# to change directory one step back
os.chdir('../')
#print("changed directory to one step back..")
