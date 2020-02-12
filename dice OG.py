import random
howManyRolls = int(input("How many rolls?"))
roll = random.randint(1,6)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
i=0

while(i<howManyRolls):
    roll = random.randint(1,6)
    print(roll)
    if(roll == 1):
        count1 += 1
    if(roll == 2):
        count2 += 1
    if(roll == 3):
        count3 += 1
    if(roll == 4):
        count4 += 1
    if(roll == 5):
        count5 += 1
    if(roll == 6):
        count6 += 1
    
    i += 1
    
print("Number of 1s: " + str(count1))
print("Percent of 1s: " + str(count1/howManyRolls))
print("Number of 2s: " + str(count2))
print("Percent of 2s: " + str(count2/howManyRolls))
print("Number of 3s: " + str(count3))
print("Percent of 3s: " + str(count3/howManyRolls))
print("Number of 4s: " + str(count4))
print("Percent of 4s: " + str(count4/howManyRolls))
print("Number of 5s: " + str(count5))
print("Percent of 5s: " + str(count5/howManyRolls))
print("Number of 6s: " + str(count6))
print("Percent of 6s: " + str(count6/howManyRolls))

    
print ("next")
