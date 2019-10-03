#PROCESS FORKING
#Run with Python3

import os
import sys

#Function for child process to run
def child():
    print ("I'm the child!", os.getpid())
    #os._exit(0)

#Function for parent process to run
def parent():
    while True:
        #Store return value of fork
        forkPID = os.fork()
        
        #If this process is the child
        if forkPID == 0:
            child()

        #If this fork returned error
        elif forkPID < 0:
            print >> sys.stderr, "FORK ERROR"
        
        #If fork was successful
        else:
            tupPID = (os.getpid(), forkPID)
            print("PARENT: %d, CHILD: %d\n" % tupPID)
        
        forkPROMPT = input("Fork parent? y/n\n")
        if forkPROMPT == 'y':
            continue
        else:
            break

parent()