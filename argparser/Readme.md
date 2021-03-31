### The argparse module in Python helps create a program in a command-line-environment in a way that appears not only easy to code but also improves interaction. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

Types Of Arguments : 

    1) Positional Arguments
    2) Optional Arguments

**Positional Arguments Syntax : **

    python filename.py arg1 arg2 arg3       
    
        we can give any number of arguments.
        
  
  Ex :  python main.py 10 20 add
        

**Optional Arguments Syntax : **

    python filename.py --flag1 arg1 --flag2 arg2
    
        we can specify in any order with --flag and then argument.
        
   
   Ex  : python main.py --number1 10 --number2 20 --operation add
