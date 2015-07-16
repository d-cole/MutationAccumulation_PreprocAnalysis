import subprocess
import sys
import time
"""
autoProc.py
Runs commands from a file containing commands. Commands are processed in parallel
with a specified number of threads.
"""

def getCommands(file_name,commands):
    """
    Loads commands from the given file into commands list
    """
    with open(file_name) as f:
        for line in f:
            commands.append(line[:-1])
    f.close()
    return 

def runCommands(commands,threadCount):
    """
    Executes commands, checking for free threads every 100sec
    """
    #initialize dead subprocesses 
    procs = [-1]*threadCount
    next_command = 0

    while next_command < len(commands):
        for i in range(0,len(procs)):
            if not procActive(procs[i]):
                procs[i] = subprocess.Popen(commands[next_command],shell=True,stdout=subprocess.PIPE)
                next_command+=1

                if next_command >= len(commands):
                    break

        time.sleep(100)   
    return

def procActive(proc):
    """
    Returns whether a given proccess is active
    """
    if proc == -1:
        return False
    else:
        if subprocess.Popen.poll(proc) != None:
            return False
    return True

if __name__ == "__main__":
    commands = []
    file_name,threads = sys.argv[1],sys.argv[2]
    getCommands(file_name,commands)
    runCommands(commands,int(threads))
