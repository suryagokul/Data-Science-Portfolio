After running above python file we can see this type of output..

2             0 LOAD_CONST               1 ((50, 100))
              2 UNPACK_SEQUENCE          2
              4 STORE_FAST               0 (a)
              6 STORE_FAST               1 (b)

3             8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                0 (a)
             12 LOAD_FAST                1 (b)
             14 BINARY_ADD
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE
