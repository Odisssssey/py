import json
import os          

def countWord(word, j):
    if word in j:
        j[word] +=1
    else:    
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
    with open(myFile, encoding = "windows-1251") as f:    
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
