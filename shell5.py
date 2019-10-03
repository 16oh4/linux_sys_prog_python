#SIMPLE BASH SHELL EXECUTION
import os

#this function uses bash to read in a key press without return
#in python, we need to press return when reading a key 
def getch():
    #execute bash, with the command in quotes
    os.system("bash -c 'read -n 1' ")

getch()