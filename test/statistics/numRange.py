import random

numList = []
for i in range(100):
    numList.append(i+1)
    
print(numList)

numList = []
for i in range(100):
    
    numList.append(random.randint(1,10))
numList.sort()    
print(numList)

for i in numList:
    numList.count(i)
    print(f"There are {numList.count(i)} for the number {i}")
