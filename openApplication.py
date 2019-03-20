from Tkinter import *
import detector as dt
import os
import dataSetGenerator as generate
import trainData as train
import storeDictionary as save
from subprocess import Popen
import random
import pickle
import CheckFace as checkFace
import createAndHide as CreateFolder


window = Tk()
window.title("FaceLock")
window.geometry('400x400')

empCode=StringVar()
userName=StringVar()
duration=StringVar()
errorLabel=Label(text="")


def saveDictionary():
  errorLabel.config(text='')
  if userName.get() == '':
      errorLabel.config(text="User name cant be left blank")
      return
  if empCode.get() == '':
      errorLabel.config(text=" Employee code Cant be left blank")
      return
  try:
      val = int(empCode.get())
  except ValueError:
      errorLabel.config(text="Enter a valid employee ID")
      return
  if duration.get() == '':
      errorLabel.config(text="Duration cant be left blank")
      return
  try:
      val = int(duration.get())
  except ValueError:
      errorLabel.config(text="Enter a valid Duration")
      return
  if int(duration.get())<1 or int(duration.get())>61:
      errorLabel.config(text="Enter between 0 and 60 min")
      return

  if(save.findName(empCode.get())!='not' or save.findEmpCode(userName.get())!='not'):
      errorLabel.config(text="User with this employee id or user name has already been registered")
      return
  flag=checkFace.checkFace()

  if(flag==False):
      errorLabel.config(text="This face is already a known face")
      return

  range_start = 10 ** (4 - 1)
  range_end = (10 ** 4 ) - 1
  rndmnumber= str(random.randint(range_start, range_end))

  if len(duration.get()) == 1:
    foldername=rndmnumber+'0'+duration.get()+empCode.get()
  else:
    foldername = rndmnumber +duration.get() + empCode.get()
  dict={empCode.get():str(userName.get())}
  save.store(dict)
  dict2={userName.get():foldername}
  save.storeFolder(dict2)

  generateData()
  trainData()


def recogniseFace():
    flag=dt.detector()
    print flag
    window.destroy

print empCode.get()

def generateData():
    generate.generateDataSet(empCode.get())

def trainData():
    pickle_in_foldername = open('./utilities/folderdictionary.pickle','rb')
    dictionary_foldername = pickle.load(pickle_in_foldername)
    answer_folder = dictionary_foldername[userName.get()]
    answer_folder=str(answer_folder)


    CreateFolder.createFolder(answer_folder)

    #Popen("./utilities/createAndHide.bat "+ userName.get() + " "+answer_folder)
    flag=train.trainDataSet(empCode.get())
    if(flag==True):
        Label(text="trained").grid()
    else:
        Label(text="not trained").grid()


Label(text="Welcome to the admin Screen").grid()
Label(text="enter your username").grid()
Entry(textvariable=userName).grid()
Label(text="enter your employeeCode").grid()
Entry(textvariable=empCode).grid()
Label(text="Duration for which Folder should be opened ").grid()
Entry(textvariable=duration).grid()
button=Button(text="DataSet Generation",command=saveDictionary).grid()
errorLabel.grid()
window.mainloop()