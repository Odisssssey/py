import random
words = ('питон', 'слово', 'задание', 'загадка', 'буква', 'название', 'дублер')
resource = random.choice(words)

nabor = {'питон': 'Язык, который вы изучаете.',
         'слово': 'Оно было вначале.',
         'задание': 'Задача, вам задана.',
         'буква' : 'Они всюду.',
         'загадка': 'Задача, на которую уже есть ответ.',
         'название': 'Есть у книги.',
         'дублер': 'Есть у дорог.'}

presWord = ""
stop = 0
print("Угадайте, что скрывает следующая анаграмма:") 

while resource != presWord:
  word = resource
  jumble =''
  while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
  if stop == 1:
    print("Ваша новая анаграмма:")    
  print(jumble)
  print('Pасставьте буквы в нужном порядке.')
  presWord = input("Ваше предположение:")
  if resource != presWord and stop == 0:
    print("ПОДСКАЗКА:")
    print(nabor[resource])
    stop = 1
  
print("Вы угадали!", "Слово, которое было загадано - ", resource)
