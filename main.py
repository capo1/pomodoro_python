#! python3
import time
import sys

REGISTRY = None # Global to get pause parameters
toMinutes = 60 # Multiply by 60 sec, disabled for tests
singleLoopTime = 10  # * toMinutes | Time in minutes for one task to multiply by $toMinutes
countLoop = 3 # * toMinutes | After this no of Tasks set longBreak, starts at 0 :)
shortBreak = 5  # * toMinutes | Time in minutes for shortBreak to multiply by $toMinutes
longBreak = 15  # * toMinutes | Time in minutes for longBreak to multiply by $toMinutes

def getFileWithTasks(fileName):
  taksFile = open(fileName, "r")
  taskList = taksFile.readlines()
  taksFile.close()
  return taskList

def clearLine():
  sys.stdout.write("\033[K")

def setLoopForTask(string,loop_time): 

  printOnConsole(string)

  while loop_time >= 0:
    printOnConsole(str('%02d:%02d' % (loop_time / 60, loop_time % 60)))
    loop_time -= 1   
    REGISTRY['time'] = loop_time
  return

def printOnConsole(string):
  print (string+'\r', end="", flush=True)
  time.sleep(1)

def setBreak(string,short_break):  
  setLoopForTask(string,short_break)
  return

def loopForTask(fileName,single_loop_time,interation):
  print("\n*** Pomodoro Method ***")

  global REGISTRY
  REGISTRY={'time':0,'loopItem':0}
  taskList = getFileWithTasks(fileName)
  breakTime = 0
  listLenghth=len(taskList)

  while (interation < listLenghth):
    clearLine()
    startString="---\nStart task no #%d: %s\n\r" % (interation+1,taskList[interation])  
    REGISTRY['loopItem'] = interation
    setLoopForTask(startString, single_loop_time)   
    
    if(interation % countLoop == 0 and interation != 0 ):   
      breakTime=longBreak      
    else:
      breakTime=shortBreak  

    endString="\rYou have break for: %d:%02d minutes  \r\n"  %  (breakTime / 60, breakTime % 60)
    setBreak(endString,breakTime)
    interation += 1
    single_loop_time = singleLoopTime

print("\nTo stop the script execution type <CTRL+C>")

while True:
  single_loop_time = REGISTRY['time'] if REGISTRY else singleLoopTime
  interation =  REGISTRY['loopItem'] if REGISTRY else 0
  
  try:
    loopForTask("tasks.txt",single_loop_time,interation)
    clearLine()
    break
  except KeyboardInterrupt:
    resume = input('\nIf you want to resume type <r> and press <Enter>\nor any other key to stop and exit script\ntype:')
    if resume != 'r':
      break
