import os

file_path = os.path.realpath(__file__)
base_path = os.path.dirname(file_path)

with open(f"{base_path}/math.py") as maThing:
    print(base_path)
with open('math.py') as maTest:
    print(maTest)