import os


def unlock(checkName, answer_folder):
    os.chdir('./secretFolder')
    print checkName,answer_folder
    os.system('attrib -s -h ' + answer_folder)
    os.rename(answer_folder,checkName)
    os.system('attrib +h +s ' + checkName)
    os.system('explorer ' + checkName)
    os.chdir('../')
767601664637