import json
import os

def countWord(word, j):
    stop = 0
    n = 0
    for key, sumWord in j.items():
        n += 1
        if word == key:
            sumWords = int(sumWord)
            sumWords += 1
            j[word] = sumWords
            stop = 1
            break
    if stop == 0:
        j[word] = 1
    return j            
    

def eachWord(line, j):
    for word in line.split(" "):
        words = word.replace(',', '').replace('.', '').replace('<', '').replace('>', '').replace('/', '')
        if len(words) >= 6:
            countWord(words, j)
    return j

def perceptionData(item, j):
    for new in item:
        cdata = new["description"]["__cdata"]
        eachWord(cdata, j)
    return j

def openFile(myFile):
    with open(myFile) as f:    
        data = json.load(f)
        item = data["rss"]["channel"]["item"]
    return item

def sortWord(j):
    n = 0
    for word in sorted(j.items(), key=lambda item: item[1], reverse=1):
        print(word)
        n += 1
        if n == 10:
            break
def newTopList(myFile):
    j = {}
    item = openFile(myFile)
    j = perceptionData(item, j)
    sortWord(j)
        
def findJson(directory):
    files = os.listdir(directory)
    for myFile in files:
        if myFile.split(".")[1] == "json":
            print(myFile.split(".")[0])
            newTopList(myFile)
        
directory = "./"
findJson(directory)    


