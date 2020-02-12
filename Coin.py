import random

numFlips = int(input("How many flips? "))

countH = 0
countT = 0
i = 0
while(i<numFlips):
    flip = random.randint(1,2)
    if(flip == 1):
        countH += 1
    if(flip == 2):
        countT += 1
    i += 1

print(f"Tails: {countT}/{numFlips} = {countT/numFlips*100}%")
print(f"Tails: {countH}/{numFlips} = {countH/numFlips*100}%")
