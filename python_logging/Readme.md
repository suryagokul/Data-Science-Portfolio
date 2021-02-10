What is Logging?

    Logging is a means of tracking events that happen when some software runs. 
    Logging is important for software developing, debugging and running. If you 
    don't have any logging record and your program crashes, there are very 
    little chances that you detect the cause of the problem.

    It is used to get info and debug information of an particular application.

    For every application we have to log all the metrics and parameters that 
    are used into different log files.
    
    
Why Printing is not a good option instead of logging?

      Some developers use the concept of printing the statements to validate if 
      the statements are executed correctly or some error has occurred. But 
      printing is not a good idea. It may solve your issues for simple scripts 
      but for complex scripts, printing approach will fail.

      Logging provides various functionalities like debugging, timestamps, 
      severity of problem, line no's where actual program fails,writing status 
      messages, saving logs, comparing different models incase of machine 
      learning..etc

      But in case of print statement we just prints a statement into console 
      without any other information and any problem severity and all..
      
      
Levels Of Logging : 

    1. Critical       - 50

    2. Error          - 40

    3. Warning        - 30

    4. Info           - 20

    5. Debug          - 10

    6. NoSet          - 0 (Not widely used)


By default level is `Warning.`

If we set as warning then, all the above levels will logged.

    Ex         level      -         Warning

                              (logged warning,error,critical)


If we set level as info then, all the above levels will logged.


    Ex          level       -        Info

                                (logged info,warning,error,critical)

