import time
import sys


Reg1 = None # global to get pause parameters

toMinutes = 60 # multiply by 60 sec
singleLoopTime = 10  # time in minutes for one task to multiply by $toMinutes
countLoop=3 # After this no of Tasks set longBreak, starts at 0 :)
shortBreak = 5  # time in minutes for shortBreak to multiply by $toMinutes
longBreak = 5  # time in minutes for longBreak to multiply by $toMinutes


def getFileWithTasks(fileName):
  f = open(fileName, "r")
  x = f.readlines()
  f.close()
  return x

def clearLine():
  sys.stdout.write("\033[K")

def setLoopForTask(string,lT): 

  printOnConsole(string)

  while lT >= 0:
    printOnConsole(str('%02d:%02d' % (lT / 60, lT % 60)))
    lT = lT - 1   
    Reg1['time'] = lT
  else: 
    return

def printOnConsole(Str):
  print (Str+'\r', end="", flush=True)
  time.sleep(1)

def setBreak(string,sB):  
  setLoopForTask(string,sB)
  return

def loopForTask(fileName,sl,i):
  o = i
  global Reg1
  Reg1={'time':0,'loopItem':0}
  print("\nS-T-A-R-T    T-A-S-K-S")
  mylist = getFileWithTasks(fileName)
  breakTime = 0
  listLenghth=len(mylist)

  while (o < listLenghth):
    clearLine()
    startString="---\nStart task no #%d: %s\n\r" % (o+1,mylist[o])  
    Reg1['loopItem'] = o
    setLoopForTask(startString, sl)   
    
    if(o % countLoop == 0 and o != 0 ):   
      breakTime=longBreak      
    else:
      breakTime=shortBreak  

    endString="\rYou have break for: %d:%02d minutes  \r\n"  %  (breakTime / 60, breakTime % 60)
    setBreak(endString,breakTime)
    o += 1
    sl = singleLoopTime


print("To stop the script execution type CTRL-C")

while 1:
  sl = Reg1['time'] if Reg1 else singleLoopTime
  i =  Reg1['loopItem'] if Reg1 else 1
  
  try:
    loopForTask("tasks.txt",sl,i)
  except KeyboardInterrupt:
    resume = input('\nIf you want to resume type r\nor any other key to stop and exit:')
    if resume != 'r':
      break
