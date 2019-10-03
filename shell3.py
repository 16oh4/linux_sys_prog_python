#PIPE REDIRECTIONS
import sys

#save current stdout
copySTDOUT = sys.stdout

#open file descriptor into G
G = open("file.txt", "w");

#stdout is set to the file descriptor G, so all print statements print to file G
sys.stdout = G
print("Testing")

#restore stdout to original
sys.stdout = copySTDOUT

#Close file descriptor
G.close()