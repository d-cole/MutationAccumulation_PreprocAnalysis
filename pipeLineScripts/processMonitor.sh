#!/bin/bash
# call: ./processMonitor.sh <id> <email> &
#Sends an email when the specified process no longer exists
PID=$1
email=$2
echo "Monitoring $PID, notify $email"

#Get command that initiated process
CMD=$(< /proc/$PID/cmdline )
while :
do
#get name of the specific process
RES=$(ps -p $PID -o comm=)
size=${#RES}

#ps returns nothing if the PID does not exist, process doesn't exist
if  [ $size == 0 ]
    then
mail -s "Grandiflora tasks" $email <<EOF
Task $CMD has finished.
$PID
EOF
exit

else
    sleep 100
fi

done




