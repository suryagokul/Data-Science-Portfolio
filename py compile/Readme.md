![alt text](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/how-python-interpreter-works.jpg)

when we import a file from another python script, then python interpreter automatically creates __pycache__ folder and in that .pyc files which is nothing but compiled file.

`But how do we convert .py file to compiled file manually?`

for that open compile_manually.py script which is given here and in that replace python filename as your wish and then run script 

    python compile_manually.py

After getting compiled python file (.pyc) `how to run it?`

    Simple goto command line
    
           goto directory where this .pyc file exists
           
           type python filename.pyc   
           
           for example python matrix_mul.cpython-37.pyc
           
    It will runs the code.

![how cpython and jython works](https://uploads.toptal.io/blog/image/127/toptal-blog-C.png)

`References to know more about python implementations and compilation`

        https://www.toptal.com/python/why-are-there-so-many-pythons

        https://stackoverflow.com/questions/17130975/python-vs-cpython
