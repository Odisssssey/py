import glob
import os.path

def printFile(file):
    with open(file, encoding = "utf-8") as f:
        print(f.read())
        
def ollDir(files):
    stop = 0
    for myFile in files:
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

def actionFiles(files, key, directory):
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
    

def ollFilesInKey(keyFiles, directory):
    n = 0
    for keyFile in keyFiles:
        keyFiles[n] = keyFile.split(directory)[1].split("\\")[1]
        n += 1
    
    ollfiles(keyFiles)  
    ollDir(keyFiles)
        
def findsql(directory):
    files = os.listdir(directory)

    
    ollfiles(files)  
    ollDir(files)

    keyInFil = input("Для поиска совпадений в открытой папке введите часть названия. Если вы знаете полное название или хотите войти в другую папку, то пропустите данный вопрос.:")

    
    if keyInFil == "":
        key = input("Введите иля папки/файла для дальнейшего взаимодействия:")

        actionFiles(files, key, directory)
        
    else:
        go = 0
        while keyInFil != "":
            if go == 1:
                keyInFil = input("Для поиска совпадений в открытой папке введите часть названия. Если вы знаете полное название или хотите войти в другую папку, то пропустите данный вопрос.:")
                if keyInFil == "":
                    break
            #print(directory)
            keyInFile = "*" + keyInFil + "*"
            keyFiles = glob.glob(os.path.join(directory, keyInFile))
            ollFilesInKey(keyFiles, directory)
            go = 1

        key = input("Введите иля папки/файла для дальнейшего взаимодействия:")
        actionFiles(files, key, directory)
        
        
             
myDir = os.path.dirname(os.path.realpath(__file__))
#print(myDir)

findsql(myDir)

#files = glob.glob(os.path.join(migrations, "*.sql"))
