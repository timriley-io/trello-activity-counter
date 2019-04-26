import json
from pprint import pprint    

with open(input("Enter JSON file path: ")) as f:
    data = json.load(f)
    counter = {}
    actions = data["actions"]
    
    for action in actions:
        name = action["memberCreator"]["fullName"]
        t = action["type"]
        
        if (name not in counter):
            counter[name] = {}

        if (t not in counter[name]):
            counter[name][t] = 0

        counter[name][t] += 1


print("\n")
for user in counter:
    print(user)
    pprint(counter[user])
    print("\n")

                    
