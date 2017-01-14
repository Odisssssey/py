cook_book = {}
with open("cook.txt") as f:
    for line in f:
        dish = line.split("\n")[0]
        print(dish)
        
        dishType = f.readline().split("\n")[0]
        #print(dishType)
        
        namber = int(f.readline())
        
        ing = []
        
        for ingridient in range(namber):
            prod = {}
            ingridient = f.readline().split("\n")[0]
            prod["product"] = ingridient.split(" | ")[0]
            prod["quantity"] = int(ingridient.split(" | ")[1])
            prod["unit"] = ingridient.split(" | ")[2]
            ing.append(prod)
            #print(ingridient)
        #input("sd")

        dishInf = {}
        dishInf['name'] = dish
        dishInf['type'] = dishType
        dishInf['ingridients'] = ing
        
        cook_book[dish] = dishInf
        
def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, first_dish, second_dish, third_dish):
    # получить блюда из кулинарной книги
    dish1 = cook_book[first_dish]
    dish2 = cook_book[second_dish]
    dish3 = cook_book[third_dish]
    dishes = [dish1, dish2, dish3]
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    # Вывести список покупок
    print_shop_list(shop_list)

print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())

print('Список покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)
