import random

numRolls = int(input("Hoy many rolls? "))

rolls = [0,0,0,0,0,0]

i = 0
while (i < numRolls):
    roll = random.randint(1,6)
    rolls[roll-1] += 1
    i += 1
    
for i in range(len(rolls)):
    print(f"{i+1}: {rolls[i]}/{numRolls} = {rolls[i]/numRolls*100}%")
