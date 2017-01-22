import os
import glob
import subprocess

def ollImage(myDir):
    files = glob.glob(os.path.join(myDir, "*.jpg"))
    return files

def createImage(convertProgram, inputDir, outputDir, outputName):
    subprocess.run([convertProgram,
                     "mogrify", str(os.path.join(inputDir, outputName)),
                     "-resize", "200", 
                     str(os.path.join(outputDir, outputName))])

directory = os.path.dirname(os.path.realpath(__file__))
convertProgram = os.path.join(directory, "convert.exe")
myDir = os.path.join(directory, "Source")
result = os.path.join(directory, "Result")
myImage = ollImage(myDir)

for nameMyImage in myImage:
    nameMyImage = nameMyImage.split(myDir)[1].split("\\")[1]
    createImage(convertProgram, myDir, result, nameMyImage)
