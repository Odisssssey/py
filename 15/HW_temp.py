import osa
import os.path

def coantCelsius(a):
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.Client(URL)

    response1 = client.service.ConvertTemp(Temperature=a, FromUnit='degreeFahrenheit' , ToUnit='degreeCelsius')

    return response1

def workWithLineTemp(f):
    text = []
    for line in f:
        my_str = line.replace(" F\n", "").replace(" F", "")
        text.append(int(my_str))
    # text = f.read()
    return text


def printTemp(myDir):
    pathfile = os.path.join(myDir, "temp.txt")
    with open(pathfile, encoding = "utf-8") as f:
        text = workWithLineTemp(f)
    a = int(sum(text)/len(text))
    temp = coantCelsius(a)
    temp = (round(temp, 2))
    return temp

myDir = os.path.dirname(os.path.realpath(__file__))

print("Средняя температура " + str(printTemp(myDir)) + " градусов по Цельсию.")
