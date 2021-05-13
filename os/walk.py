import os 

path = os.getcwd()

'''

walk yields 3 values i.e dirpath, dirname, filename expects an argument of path.
By iterating into generator object we can get  values.

for example current dir is os
       in that we have test1.py, test2.py, demo_folder
       in demo_folder we have  sub_folder in it

when we use walk with current path i.e os.walk(c:\users\surya\desktop\os)
it returns C:\Users\SURYA\Desktop\os
	   ['demo_folder']
	   ['test1.py', 'test2.py'].

 	   C:\Users\SURYA\Desktop\os\demo_folder
	   ['sub_folder']
	   []

 	   C:\Users\SURYA\Desktop\os\folder\sub_folder
	   []
	   []

'''

print(os.walk(path))  					# returns generator object 


for dirpath, dirname, filename in os.walk(path):
    print("Directory path : ",dirpath)
    print("Directory name : ",dirname)
    print("File name : ",filename)