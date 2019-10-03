import sys

#COMMAND LINE ARGUMENTS
print sys.version
cmd_vars = sys.argv

#range returns an iterator list from 0 to the argument
for i in range(len(cmd_vars)):
    print cmd_vars[i]

#more concise loop above the other one
for j in cmd_vars:
    print j

#STANDARD DATA STREAMS
sys.stdout.write("16oh4!!!!\n")
#user_in = raw_input("What's your name\n")
#print user_in

#print prompt, fetch, and output the first 3 characters in the same line!
print "fetch in value", sys.stdin.readline()[0:3]

while True:
    print "Iterating"
    try:
        num = raw_input("Favorite #")
    except EOFError:
        print "Reached end of file"
        break
    else:
        num = int(num)
        if num ==0:
            print >> sys.stderr, "error"
        else:
            print "inverse of %d is %f" % (num, 1.0/num)
