#!/usr/bin/python
import os
args = ("16oh4", "com")

#Will replace the current process!
os.execvp("run.sh", args)