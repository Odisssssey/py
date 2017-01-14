import json

with open('tet.json') as f:    
    data = json.load(f)
def searchType(myType, data):
    j = []
    for scop in data:
        for key, rows in scop.items():
            for iformation in rows:
                if myType == iformation['type']:
                    j.append(iformation['name'])
                    #print(iformation['name'])
    return j

def Ollgoods(myDishs, data, peoples):
    bag = []
    for myDish in myDishs:
        for scop in data:
            for key, rows in scop.items():
                for iformation in rows:
                    if myDish == iformation['name']:
                        for ingridient in iformation['ingridients']:
                            structure = {}
                            mastHave = ingridient["quantity"] * peoples
                            structure[ingridient["product"]] = [ingridient["product"], mastHave ,ingridient["unit"]]
                            IDontKnow = ''
                            for lol in bag:
                                for k, i in lol.items():
                                    try:
                                        if k == ingridient["product"]:
                                            IDontKnow = ingridient["product"]
                                            i[1] += mastHave
                                    except KeyError: 
                                        continue
                            if IDontKnow == '':
                                bag.append(structure)          
    return bag


def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))                    
        
                    
myDishs = []
while True:
    myType = 0
    while myType > 3 or myType < 1:
        if len(myDishs) > 0:
            print("Вот все бдлюа, которые вы хотите приготовить", myDishs)
        myType = int(input("""
Какое блюдо вы хотите готовить? 1 - горячее, 2 - второе, 3 - десерт
        """))
        if myType > 3 or myType < 1:
            stopOll = input("Если хотите выйти введите e:")
            if stopOll == "e":
                break
    ollDishs = searchType(myType, data)
    myDish = ""
    while myDish not in ollDishs:
        print("Вот все блюда этой категории:", ollDishs)
        myDish = input("Введите название желаемого блюда:")
        if myDish not in ollDishs:
            stop = input("Для выбора категории нажмите e:")
            if stop == "e":
                break
    if myDish in ollDishs:
        myDishs.append(myDish)
    question = input("Хотите еще что-то готовить? если нет - пропустите.")
    if question == "":
        break
print("Вот все бдлюа, которые вы хотите приготовить", myDishs)
people = int(input("На сколько человек будете готовить?"))
myBag = Ollgoods(myDishs, data, people)
print(myBag)
