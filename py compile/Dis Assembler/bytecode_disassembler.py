def add_func():
    a,b = 50,100
    print(a+b)

import dis

dis.dis(add_func)