import os


def lockFolders(userName,answer_folder):
    #os.chdir('./utilities')   this is for nircmd if it is used
    os.chdir('./secretFolder')
    #reorg_dir = "../secretFolder"
    currentPath=os.getcwd()

    os.chdir('c:')   #so that we can force kill any file with the name

    for root, dirs, files in os.walk(currentPath):

        for dr in dirs:
            print 'directory name: ',dr,'current directory',os.getcwd()
            os.system('taskkill.exe /f /fi "Windowtitle eq '+dr+'*"')

        for file in files:
            print 'file name: ',file,'current directory',os.getcwd()
            os.system('taskkill.exe /f /fi "Windowtitle eq ' + file + '*"')

    os.chdir(currentPath)

    os.system('attrib -s -h '+userName)
    #os.chdir('./secretFolder')
    os.rename(userName,answer_folder)
    os.system('attrib +h +s  '+answer_folder)

    os.chdir('..')



