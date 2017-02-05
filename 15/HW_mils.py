import osa
import os.path

def printMils(count_mils, kilometers):
    URL = 'http://www.webservicex.net/length.asmx?WSDL'

    client2 = osa.Client(URL)
    response4 = client2.service.ChangeLengthUnit(LengthValue=100.00, fromLengthUnit='Mils', toLengthUnit='Kilometers')

    my_length = str(response4).split('-')
    my_length1 = my_length[0].replace("e", "")
    my_length2 = int(my_length[1])
    my_length3 = int("1" + ("0" * my_length2))
    my_length = float(my_length1) * my_length3
    return my_length

def workWithLineCurrencies(f):
    kilometers = 0
    for line in f:

        my_str = line.replace(" mi\n", "").replace(" mi", "").replace(",", "")
        my_dict = my_str.split(" ")

        kilometers += float(printMils(float(my_dict[1]), kilometers))
    kilometers = round(kilometers, 2)
    return kilometers

def printCurrencies(myDir):
    pathfile = os.path.join(myDir, "travel.txt")
    with open(pathfile, encoding="utf-8") as f:
        sum_currencies = workWithLineCurrencies(f)
    return sum_currencies

myDir = os.path.dirname(os.path.realpath(__file__))

print(str(printCurrencies(myDir)) + " километров")
