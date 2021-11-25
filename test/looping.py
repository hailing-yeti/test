# Test dictionary looping

import random

things = {
    "Thanksgiving",
    "Christmas",
    "New Year",
    "St. Valentine's Day",
    "St. Patrick's Day",
    "April Fool's Day",
    "Mother's Day",
    "Father's Day",
    "Independence Day",
    "Perseid Meteor Shower",
    "Labor Day",
    "Halloween"
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October"
    }

for i in things:
    stack1 = list.pop(random.choice(things))
    stack2 = list.pop(random.choice(things))

print(stack1)