def dopolneniye(A):
  dopolneniyeA = []
  for line in A:
    uroven = []
    for needle in line:
      unit = 1 - needle
      unit = float("{0:.2f}".format(unit))
      uroven.append(unit)
    dopolneniyeA.append(uroven)
  return dopolneniyeA

def peresecheniye(A, B):
  peresecheniyeAB = []
  loop = 0
  for line in A:
    uroven = []
    loops = 0
    for needle in line:
      unit = min(needle, B[loop][loops])
      loops += 1
      uroven.append(unit)
    loop += 1
    peresecheniyeAB.append(uroven)
  return peresecheniyeAB

def obyedineniye(A, B):
  obyedineniyeAB = []
  loop = 0
  
  for line in A:
    uroven = []
    loops = 0
    for needle in line:
      unit = max(needle, B[loop][loops])
      loops += 1
      uroven.append(unit)
    loop += 1
    obyedineniyeAB.append(uroven)
  return obyedineniyeAB
  
def  raznost(A, B):
  B = dopolneniye(B)
  raznostAB = []
  loop = 0
  
  for line in A:
    uroven = []
    loops = 0
    for needle in line:
      unit = min(needle, B[loop][loops])
      loops += 1
      uroven.append(unit)
    loop += 1
    raznostAB.append(uroven)
  return raznostAB

def dizyunktivnayaSumma(A, B):
  C = raznost(A, B)
  B = raznost(B, A)
  dSum = []
  loop = 0
  for line in C:
    uroven = []
    loops = 0
    for needle in line:
      unit = max(needle, B[loop][loops])
      loops += 1
      uroven.append(unit)
    loop += 1
    dSum.append(uroven)
  return dSum


i1 = [1, 0.5, 0.7, 1]
i2 = [0.7, 1, 1, 0.6]
i3 = [0.4, 1, 1, 0.9]
i4 = [0.8, 0.5, 1, 1]

j1 = [0.7, 0.5, 0.7, 0.8]
j2 = [0.5, 1, 0, 0.5]
j3 = [0.3, 1, 0, 0.8]
j4 = [0.3, 0.5, 0.9, 0.5]

i = [i1, i2, i3, i4]
j = [j1, j2, j3, j4]

variable = input("Какое действие вы хотите сделать?")   

if variable == "дополнение":
  print(dopolneniye(i)) 
if variable == "пересечение":
  print(peresecheniye(i, j))
if variable == "объединение":
  print(obyedineniye(i, j))
if variable == "разность":
  print(raznost(i, j))
if variable == "дизъюнктивная суммуа":
  print(dizyunktivnayaSumma(i, j))



