import glob
import os.path
import requests

def detect_lang(text):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': KEY,
        'text': text,
    }
    response = requests.get(URL, params=params)
    return response.json()['lang']

def translate_it(text, lang):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    lang += "-ru"
    
    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

def createTranslate(text, myFile):
    lang = detect_lang(text)
    print(lang)
    textTranslate = translate_it(text, lang)

    newFile = os.path.join(myDir, "Translates")
    newFile = os.path.join(newFile, myFile)

    
    with open(newFile, "w") as fTranslate:
        fTranslate.write(textTranslate)
    

def printFile(file, myFile):
    with open(file, encoding = "utf-8") as f:
        text = f.read()
        createTranslate(text, myFile)
        

def ollfiles(files, directory):
    stop = 0
    for myFile in files:
        if "." in myFile:
            if myFile.split(".")[1] == "txt":
                if stop == 0:
                    stop = 1
                print(myFile)
                pathfile = os.path.join(directory, myFile)
                printFile(pathfile, myFile)
                

def findtxt(directory):
    directory = os.path.join(directory, "Sourse")
    files = os.listdir(directory)
    ollfiles(files, directory)


myDir = os.path.dirname(os.path.realpath(__file__))
findtxt(myDir)
