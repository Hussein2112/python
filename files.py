#!/usr/bin/python3
import stat
import os
import subprocess  # Replaced deprecated 'commands' module
import shlex       # Safely split the command string
from pprint import pprint  # Better printing of data structures

try:
    pattern = input("Enter the file pattern to search for:\n")  # Changed 'raw_input' to 'input' for Python 3 compatibility
    commandString = "find " + pattern

    # Using subprocess.Popen to execute the command and capture its output
    process = subprocess.Popen(shlex.split(commandString), stdout=subprocess.PIPE)
    commandOutput = process.communicate()[0].decode("utf-8").strip()
    
    findResults = commandOutput.split("\n")

    print("Files:")
    pprint(findResults)  # Changed print to pprint for better formatting
    print("================================")

    for file in findResults:
        mode = os.lstat(file).st_mode  # Simplified, no need for S_IMODE here
        print("\nPermissions for file ", file, ":")
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode & getattr(stat, "S_I" + perm + level):
                    print(level, " has ", perm, " permission")
                else:
                    print(level, " does NOT have ", perm, " permission")
except Exception as e:  # Catching all exceptions, not just any
    print("There was a problem - check the message below:")
    print(e)
