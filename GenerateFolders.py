import os
import shutil
from Constants import *
def generateFolders():
    if os.path.isdir(rootdir):
        shutil.rmtree(rootdir)

    os.mkdir(rootdir)
    os.mkdir(datadir)
    os.mkdir(minecraftdir)
    os.mkdir(tagsdir)
    os.mkdir(functionsdir)
    os.mkdir(tobacco_awarenessdir)
    os.mkdir(funcsdir)
    os.mkdir(addictiondir)
    os.mkdir(addiction_helperdir)