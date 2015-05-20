import subprocess
import sys
import time
#x = call(["ls","-l"])
#print(x)
#x = subprocess.Popen("sleep 4",shell=True,stdout=subprocess.PIPE)
#print(subprocess.Popen.poll(x))
#print(type(subprocess.Popen.poll(x)))


def getCommands(file_name,commands):
    with open(file_name) as f:
        for line in f:
            commands.append(line[:-1])
    f.close()
    return 

def runCommands(commands,threadCount):
    print(commands)
    procs = [-1]*threadCount
    next_command = 0

    while next_command < len(commands):
        print(commands[next_command])
        for i in range(0,len(procs)):
            if procs[i] == -1:
                procs[i] = subprocess.Popen(commands[next_command],shell=True,stdout=subprocess.PIPE)
                next_command+=1
                break
        updateProcs(procs)
        time.sleep(100)   
         
    return

def updateProcs(procs):
    for i in range(0,len(procs)):
        if procs[i] != -1:
            if subprocess.Popen.poll(procs[i]) != None:
            #Process has ended
                procs[i] = -1
    return

if __name__ == "__main__":
    commands = []
    file_name = sys.argv[1]
    getCommands(file_name,commands)
    runCommands(commands,3)





