from Tkinter import *
import storeDictionary as save
import detector as dt
from subprocess import Popen
import pickle
import time
from threading import Timer
import LockFolder, UnlockFolder

import os
#import closingFolder as closeFolder

window = Tk()
window.title("FaceLock")
window.geometry('400x400')

#while loop apply therecheck for finaltime

remaining=10
timer_active='no'
sub_folder='no'
userName=StringVar()
usertimer=StringVar()
errorLabel=Label(text="")
timerLabel=Label(text="")
timerlabelcountdown=Label(text="")

def checkTime():
    if getFolderName()!='not':
        duration=getFolderName()[4:6]
        return int(duration)


def getFolderName():
    checkName = userName.get()
    pickle_in_foldername = open(
        './utilities/folderdictionary.pickle',
        'rb')
    try:
        dictionary_foldername = pickle.load(pickle_in_foldername)
        answer_folder = dictionary_foldername[checkName]
    except:
        answer_folder = 'not'
    return answer_folder

def lockFolder():
    #print 'here'
    global timer_active
    timer_active = 'no'
    timerlabelcountdown.config(text='')
    timerLabel.config(text='')
    answer_folder = getFolderName()
    #closeSubFolders(userName.get())

    #os.system('nircmd win close title "%s"' %userName.get())
    LockFolder.lockFolders(userName.get(),answer_folder)
    #Popen("./utilities/lockFolder.bat "+userName.get()+" "+answer_folder)
    global sub_folder
    sub_folder = 'yes'
    user.configure(state=NORMAL)
    unlock.configure(state=NORMAL)
    lock.configure(state=DISABLED)
    user_timer.configure(state=NORMAL)



def lockFolder_crossButton():
    if userName.get()!='':
      answer_folder = getFolderName()

     #####check if the folder has already been locked or not!!!!*********
      if os.path.exists('./secretFolder/'+userName.get()):
          LockFolder.lockFolders(userName.get(), answer_folder)


      #Popen("./utilities/lockFolder.bat " + userName.get() + " " + answer_folder)
    global timer_active
    timer_active = 'no'
    window.destroy()

def unlockFolder(checkName,answer_folder):
    #Popen("./utilities/openFolder.bat " + checkName + " " + answer_folder)
    UnlockFolder.unlock(checkName,answer_folder)
    user.configure(state=DISABLED)
    unlock.configure(state=DISABLED)
    lock.configure(state=NORMAL)
    user_timer.configure(state=DISABLED)

def countdown():
     global timer_active
     global remaining
     if remaining <= 0 and timer_active=='yes':
         timerlabelcountdown.config(text="time's up!")
     elif timer_active=='yes':
         timerlabelcountdown.config(text="%d" % remaining)
         remaining = remaining - 1
         timer = Timer(1, countdown)
         timer.start()


def recogniseFace():
    errorLabel.config(text='')
    timerlabelcountdown.config(text='')
    if userName.get() == '':
        errorLabel.config( text='User Name be left blank')
        return
    if save.findEmpCode(userName.get()) == 'not':
        errorLabel.config(text='Please register yourself')
        return
    final_time = checkTime()
    if usertimer.get() != '':
        try:
            if int(usertimer.get()) < 1 or int(usertimer.get()) > 61:
                 errorLabel.config( text='Enter between 0 and 60 min')
                 return
            final_time = int(usertimer.get())
        except ValueError:
            errorLabel.config( text='Enter a valid duration')
            return
    flag=dt.detector()
    if flag==False:
        errorLabel.config(text='Could not recognize you')
        return
    checkName=userName.get()
    answer_folder = getFolderName()
    if(checkName==flag):
        global timer_active
        timer_active='yes'
        timerLabel.config(text='Session is active')
        global remaining
        remaining=final_time*60
        countdown()
        unlockFolder(checkName,answer_folder)
        timer = Timer(final_time*60, lockFolder)
        timer.start()

    window.destroy

Label(text="Welcome to the user Screen").grid()
Label(text="enter your username").grid()
user=Entry(textvariable=userName)
user.grid()
Label(text="Enter the required time").grid()
user_timer=Entry(textvariable=usertimer)
user_timer.grid()
unlock=Button(text="Unlock Folder",command=recogniseFace)
unlock.grid()
lock=Button(text="Lock Folder",command=lockFolder)
lock.configure(state=DISABLED)
lock.grid()
errorLabel.grid()
timerLabel.grid()
timerlabelcountdown.grid()
window.protocol('WM_DELETE_WINDOW', lockFolder_crossButton)
window.mainloop()