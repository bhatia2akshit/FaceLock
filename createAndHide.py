import os


def createFolder(rename_folder):
    if not os.path.exists('./secretFolder'):
        os.makedirs('secretFolder')

    os.chdir('./secretFolder')
    os.makedirs(rename_folder)  # in the secretFolder only
    # os.rename(username,rename_folder)
    os.system('attrib +h +s ' + rename_folder)
    os.chdir('../')

