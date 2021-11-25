import random
import math

int1 = random.randint(1,10)
int2 = random.randint(1,10)

print(f"I'm multiplying {int1} and {int2} to get {int1*int2}")

print("Let's try something fancy.")
print(f'{max(int1,int2)} is the max of the two values')
print(f'{pow(int1,int2)} is {int1} to the power of {int2}')
print(f'{math.sqrt(int1 * int2)} is the Square Root of {int1} and {int2}')