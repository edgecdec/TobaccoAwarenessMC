from GenerateFolders import generateFolders
from GenerateFiles import generateFiles
from AddictionHelperGenerator import addictionHelperGenerator
import shutil
from Constants import *

generateFolders()
generateFiles()
addictionHelperGenerator()

shutil.make_archive('tobacco_awareness', 'zip', rootdir)



