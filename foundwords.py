import random
words = ('питон', 'слово', 'задание', 'загадка', 'буква', 'название', 'дублер')
word = random.choice(words)

nabor = {'питон': 'Язык, который вы изучаете.',
         'слово': 'Оно было вначале.',
         'задание': 'Задача, вам задана.',
         'буква' : 'Они всюду.',
         'загадка': 'Задача, на которую уже есть ответ.',
         'название': 'Есть у книги.',
         'дублер': 'Есть у дорог.'}

resource = word
jumble =''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(jumble)
print('Pасставьте буквы в нужном порядке.')

newWord = jumble
presWord = ""
stop = 1

while presWord != resource:
  presWord = ""
  while len(presWord) < len(resource):
    letter = input('Введите букву:')
    loop = 1
    if letter in jumble:
      simple = ''
      for symbol in newWord:
        if symbol == letter and loop == 1:
          loop = 0
        else:
          simple += symbol
      newWord = simple
      presWord += letter    
    
    print('Оставшиеся буквы:', newWord)
    print("Вы ввели", presWord)
  
  if presWord != resource and stop == 1:
    hint = input('Хотите подсказку?')
    if hint != '':
      print(nabor[resource])
      stop = 0

print("Вы угадали слово!")
