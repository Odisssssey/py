from random import randint

i = 1
myNumber = 0
while myNumber < 1 or myNumber > 10:
  myNumber = int(input('Введите число от 1 до 10: '))
number = randint(1, 10)
stop = 1
while stop == 1:
  if myNumber == number:
    print("Вы угадали! ПК загадал число", number)
    stop = 0
  else:
      if myNumber < number:
        print('ПК загадал число, больше введенного вами. Количество ошибок сделанное вами:', i)
        myNumber = int(input('Постарайтесь угадать вновь: '))
      else:
        print('ПК загадал число, меньше введенного вами. Количество ошибок сделанное вами:', i)
        myNumber = int(input('Постарайтесь угадать вновь: '))
      i += 1
