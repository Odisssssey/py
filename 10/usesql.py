import glob
import os.path

def printFile(file):
    with open(file, encoding = "utf-8") as f:
        print(f.read())
        
def ollDir(files):
    stop = 0
    for myFile in files:
        #print("-", myFile)
        if os.path.isdir(myFile):
            if stop == 0:
                print('Вам доступны следующие папки:')
                stop = 1
            print(myFile)

def ollfiles(files):
    stop = 0
    for myFile in files:
        if "." in myFile:
            if myFile.split(".")[1] == "sql":
                if stop == 0:
                    print('Вам доступны следующие файлы:')
                    stop = 1
                print(myFile)      
    
def findsql(directory):
    files = os.listdir(directory)
 
    ollfiles(files)  
    ollDir(files)

    key = input("Введите иля папки/файла для дальнейшего взаимодействия:")

    for myFile in files:
        if myFile == key:
            if os.path.isdir(myFile):
                print("Вы открыли папку")
                newPath = os.path.join(directory, myFile)
                findsql(newPath)
            else:
                print("Вы открыли файл")
                newPath = os.path.join(directory, myFile)
                printFile(newPath)
        
    
myDir = os.path.dirname(os.path.realpath(__file__))
print(myDir)

findsql(myDir)
