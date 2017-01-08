
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
  
def saveDay(dni):
  ostatok = 90 - dni
  return ostatok

#прошлые поездки 
i = [[2, 14], [16, 20], [40, 34], [51, 70], [50, 50], [30, 40], [200, 140]]
#планируемые
j = [250, 263]


dni = 0
zanDni = []

for line in i:
  maximum = orderMax(line[0], line[1])
  minimum = orderMin(line[0], line[1])
  
  addition(zanDni, minimum, maximum)
    
print(zanDni)

firstDay = orderMin(j[0], j[1]) - 180
for unit in zanDni:
  if unit >= firstDay:
    dni += 1
    
print("Количество дней, которое вы пробыли в шенгене:", dni)

ostatok = saveDay(dni)
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
