import subprocess
import sys

"""

"""

if __name__ == "__main__":
    pr =  subprocess.Popen("../r/binom.r 10 20",\
        shell=True,stdout=subprocess.PIPE)        
    print pr.communicate()








