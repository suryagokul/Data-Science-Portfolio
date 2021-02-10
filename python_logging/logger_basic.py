import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='w',format='%(asctime)s:%(levelname)s',datefmt='%d/%m/%Y %H:%M:%S %p')


'''by default file mode is 'a'.everytime we run the code, it appends logs into file.


when we use mode as 'w' then logs will be overrided.Previous logs will gone and new logs are appended into the file.


we can also set level as 50,40,30,20,10.Level name must be capital in basiConfig format.


levelname  = gives only names of levels


asctime    = gives full form of time 


We can format the time as we want using 'datefmt'


%d = date              (%d=%D) same

%m = month             %M = Minutes

%y = year (21)         %Y = Full Form of year (2021)

%I = 12 hr format

%H = 24 hr format 

%S = Seconds 

%p = Gives AM or PM

'''


logging.critical("CRITICAL")


logging.error("Error")


logging.warning("Warning")


logging.info("INFO")


logging.debug("Debugging")


'''This will be the output in log.txt file. as we set to warning level, so it only gives above levels.

CRITICAL:root:CRITICAL
ERROR:root:Error
WARNING:root:Warning
'''