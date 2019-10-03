import sys
#save contents of stderror to restore later
copySTDERR = sys.stderr

#open text file to redirect stderr
linkSTDERR = open("stderror.txt","w")

#set stderror file descriptor to our file stderror.txt!
sys.stderr = linkSTDERR

#now whatever we write to stderr, we can see in stderror.txt
print >> sys.stderr, "Call me 16oh4!"

#this will not be printed to file because print belongs to STDOUT!
print sys.maxsize
#restore stderror to original fd
sys.stderr = copySTDERR

linkSTDERR.close()