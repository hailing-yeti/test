# Infinite loop holding test

def get_formatted_name (first_name, last_name):
    #Return a formatted name
    fullname = f"{first_name}"

while True:
    print("\nPlease tell me your name:")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
