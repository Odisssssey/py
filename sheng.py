
def orderMin(a, b):
  if a < b:
    return a 
  else:
    return b

def orderMax(a, b):
  if a > b:
    return a 
  else:
    return b 

def addition(zanDni, minimum, maximum):
  n = minimum
  while n < (maximum + 1):
    if not(n in zanDni):
      zanDni.append(n)
    n += 1
  return zanDni

def orderOll(i):
  zanDni = []
  
  for line in i:
    maximum = orderMax(line[0], line[1])
    minimum = orderMin(line[0], line[1])
    
    addition(zanDni, minimum, maximum)
    
  return zanDni
  
def arrangement(zanDni):
  stop = 0
  while stop == 0:
    stop = 1
    i = 0
    k = 1
    
    for unit in zanDni:
      try: 
        if zanDni[k] in zanDni:
          if unit > zanDni[k]:
            zanDni[i] = zanDni[k]
            zanDni[k] = unit
        
            stop = 0
      except IndexError: 
        break
      
      i += 1 
      k += 1
  return zanDni

def addVizit(zanDni):
  openNewVizit = int(input("Введите начало нового визита:"))
  closeNewVizit = int(input("Введите конец нового визита:"))
  addition(zanDni, orderMin(openNewVizit, closeNewVizit), orderMax(openNewVizit, closeNewVizit))
  return zanDni
  
def myDay(dni):
  ostatok = 90 - dni
  return ostatok
  
def removeVizit(zanDni):
  removeOpenVizit = int(input("Введите начало удаления визитов:"))
  removeCloseVizit = 0 
  while removeCloseVizit < removeOpenVizit:
    removeCloseVizit = int(input("Введите конец удаления визитов:"))
  k = 0
  while zanDni:
    try: 
      if removeOpenVizit <= zanDni[k] and zanDni[k] <= removeCloseVizit:
        
        zanDni.remove(zanDni[k])
      else:
        k += 1
    except IndexError: 
      break
  return zanDni

def maximumDayVisit(zanDni):
  maxDay = 0
  n = 1
  for k in zanDni:
    try: 
      version = orderMax(zanDni[n], k)
      if version > maxDay:
        maxDay = version
      n += 1
      
    except IndexError: 
      break
  return maxDay  
  
def plannedVizit(zanDni):
  maxVizit = maximumDayVisit(zanDni)
  ostatok = -1
  while ostatok < 0:
    ostatok = 0
    j = []
    fstPlan = 0
    scndPlan = 0
  
    while fstPlan < maxVizit:
      print('Последний день вашей прошлой поездки был:', maxVizit)
      fstPlan = int(input('Введите начало планируемого визита:'))
    
    while scndPlan < fstPlan:
      scndPlan = int(input('Введите конец планируемого визита:'))
    j.append(fstPlan)
    j.append(scndPlan)
    
    dni = 0

    firstDay = orderMin(j[0], j[1]) - 180
    for unit in zanDni:
      if unit >= firstDay:
        dni += 1
    ostatok = myDay(dni)
    
    print("Количество дней, которое вы пробыли в шенгене к началу нового визита:", dni)

    print("Количество дней, которое осталось:", ostatok) 

    lastDay = orderMax(j[0], j[1]) - 180
    
    newDays = lastDay - firstDay + 1
    print("Количество дней, которое вы будете в шенгене:", newDays)
    
    maximum = orderMax(j[0], j[1])
    minimum = orderMin(j[0], j[1])
    
    addition(zanDni, minimum, maximum)
    saveDay = 0
    usedDays = 0
    for unit in zanDni:
      if unit >= lastDay:
        usedDays += 1
    
    saveDay = 90 - usedDays
    print("Количество дней, которое после указанной даты отьезда у вас останется:", saveDay)
    
    pay = input('На сколько евро в день вы собираетесь жить?')
    
    paymentPlan = int(pay) * newDays
    
    print("Вам потребуется", paymentPlan, "евро на поездку.")
    
    k = 0
    while zanDni:
      try: 
        if fstPlan <= zanDni[k] and zanDni[k] <= scndPlan:
          
          zanDni.remove(zanDni[k])
        else:
          k += 1
      except IndexError: 
          break
  

#прошлые поездки 
i = [[2, 14], [16, 20], [40, 34], [51, 70], [50, 50], [30, 40], [200, 140]]

start = ""

while start != 'e':
  start = input("""
  Для продолжения работы выберите одно из действий:
  o - для вывода всех дней визитов
  v - для добавления визита в историю 
  p - для ввода запланированного визита
  r - для удаления визита из истории
  e - для выхода
  """)
  
  try:
    len(zanDni)
  except NameError: 
    zanDni = orderOll(i)
  
  zanDni = arrangement(zanDni)
  
  if start == 'e':
    break
  
  if start == 'o':
    print(zanDni)
    
  if start == 'v':
    zanDni = addVizit(zanDni)
    
  if start == 'p':
    plannedVizit(zanDni)
  
  if start == 'r':
    zanDni = removeVizit(zanDni)
  
