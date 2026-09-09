# Nested Dictionaries and access the values & Iteration of the nested dictionary
# employee = {
#     "name": "Arun Sharma",
#     "job": {
#         "profile": "Data Engineer",
#         "Skill": "Python"
#     }
# }

# print(employee)
# print(employee["name"])
# print(employee["job"])
# print(employee["job"]["profile"])
# print(employee["job"]["Skill"])

# for item in employee.items():
#     print(item)


#Safely access the value from the dictionary with the default values
# person = {"name":"Arun", "Age": 25}

# print(person.get("name"))
# print(person.get("email","Not Available"))


# .keys(), .values(), .items() and sorting on specific keys
# prices = {"Apple":100, "Banana": 30, "Guava": 60}

# print(prices.items())
# print(prices.values())
# print(prices.keys())

# sortedarray = sorted(prices.items(), key=lambda price: price[0]) #here if we use 0 index then the value will be sorted using key and if 1 then value
# for fruit in sortedarray:
#     print(fruit[0],":",fruit[1])


# Checking if a key exists
# prices = {"apple":50, "Guava":40}

# if("mangoes" in prices):
#     print("found")
# else:
#     print("Not found")

#Updating and adding to a dictionary
# prices = {"apple": 50, "banana": 20}
# prices["apple"] = 55        # update existing key
# prices["mango"] = 80        # add new key
# print(prices)