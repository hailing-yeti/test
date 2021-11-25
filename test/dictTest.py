import random

alpha = ""
count = random.randint(5, 10)
dcit = {}

for i in range(count):
    dcit.update({i:i+3})

# print(count)

print(dcit)
print(dcit[1])