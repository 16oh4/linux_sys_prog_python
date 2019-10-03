#!/usr/bin/env python
import subprocess
#subprocess.call("ls -al", shell=True)

#Popen arguments are command line arguments, returns and saves to proc
#stdout variable set to the subprocess PIPE to send to this script
proc = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)

#let's wait for process to terminate
proc.wait()

#read each line in the stdout variable
for line in proc.stdout.readlines():
    #rstrip removes whitespace and returns
    print line.rstrip()