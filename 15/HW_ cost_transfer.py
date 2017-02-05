import osa
import os.path

def printPrice(currency, price, sum_currencies):
    url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client1 = osa.Client(url)

    response = client1.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB', amount=price, rounding=True)
    sum_currencies += (int(round(response, 0)))
    return sum_currencies

def workWithLineCurrencies(f):
    sum_currencies = 0
    for line in f:
        #print(line)

        my_str = line.replace("\n", "")

        my_dict = my_str.split(" ")
        sum_currencies = printPrice(str(my_dict[2]), int(my_dict[1]), sum_currencies)
    return sum_currencies

def printCurrencies(myDir):
    pathfile = os.path.join(myDir, "currencies.txt")
    with open(pathfile, encoding="utf-8") as f:
        sum_currencies = workWithLineCurrencies(f)
    return sum_currencies


myDir = os.path.dirname(os.path.realpath(__file__))

print(str(printCurrencies(myDir)) + " рублей")
