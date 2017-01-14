i = 1
myNumber = 0
while myNumber < 1 or myNumber > 10:
  myNumber = int(input('Введите число от 1 до 10: '))
number = randint(1, 10)
while number:
  if myNumber == number:
    print("Вы угадали! ПК загадал число", number)
    break
  else:
      if myNumber < number:
        print('ПК загадал число, больше введенного вами. Количество ошибок сделанное вами:', i)
        myNumber = 0
        while myNumber < 1 or myNumber > 10:
          myNumber = int(input('Постарайтесь угадать вновь: '))
          if myNumber < 1 or myNumber > 10:
            print("Вы можете вводить число от 1 до 10.")
      else:
        print('ПК загадал число, меньше введенного вами. Количество ошибок сделанное вами:', i)
        myNumber = 0
        while myNumber < 1 or myNumber > 10:
          myNumber = int(input('Постарайтесь угадать вновь: '))
          if myNumber < 1 or myNumber > 10:
            print("Вы можете вводить число от 1 до 10.")
      i += 1
