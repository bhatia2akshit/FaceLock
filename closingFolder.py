from subprocess import Popen
import os
#import shutil

print 'entered'
reorg_dir = "./secretFolder/test44"
print reorg_dir
    #remove_dirs = ("akjain")
# ---------------------------------------------------------

for root, dirs, files in os.walk(reorg_dir):
    #for name in files:
        #print name
        #if name in remove_files:
            #os.system('explorer d:/Profiles/akjain/Desktop/FaceRegognitionproject/akjain')
            #os.remove(root+"/"+name)
            #os.system('taskkill /f /im '+name)
            #name.kill()
        for dr in dirs:
            print dr
           # Popen(
            #    "d:\\Profiles\\akjain\\Desktop\\FaceRegognitionproject\\lockFolder.bat " + dr)
            #print 'TASKKILL /F /FI "WINDOWTITLE eq '+dr+'" /IM explorer.exe'
            #subprocess.Popen('TASKKILL /F /FI "WINDOWTITLE eq '+dr+'" /IM explorer.exe')
        #print dr
        #if dr in remove_dirs:
           # print 'entered'
            #os.system('taskkill /f /fi "WINDOWTITLE eq ' + dr)


         #print dr
         #os.system('attrib -s -h d:/Profiles/akjain/Desktop/FaceRegognitionproject/akjain')
         #os.system('explorer d:/Profiles/akjain/Desktop/FaceRegognitionproject/akjain')
            #os.system('taskkill /im explorer.exe ')
           # os.system('explorer.exe')
            #shutil.rmtree(root+"/"+dr)
            #os.system('taskkill /f /fi "WINDOWTITLE eq '+ dr)
