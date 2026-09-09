# name = "Arun"
# age = 25
# print("My name is", name)
# print("My age is", age)

# a = 5
# b = 6
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)   # normal division, gives decimal
# print(a // b)  # floor division, gives whole number
# print(a % b)   # remainder

# marks = 93
# if(marks >= 90):
#     print("GRADE A+")
# elif(marks >= 80):
#     print("GRADE A")
# else:
#     print("PASS")

#range upto the given number
# for i in range(10):
#     print(i)

# fruits = ["A", "B", "C"]
# for i in fruits:
#  print(i)

# here we are defining the range(start point, end point, step count)
# for i in range(1, 10, 2):
#  print(i)

# here we are defining the range(start point, end point, step count) combined with the even-odd logic
# for i in range(11, 20, 1):
#     if(i % 2) == 0:
#         print(i,"EVEN")
#     else:
#         print(i,"ODD")

#here we are iterating the value from the array along with the index value
# vegetables = ["Lady Finger", "Cabbage", "Potato", "Tomato"]

# for index,vegetable in enumerate(vegetables):
#     print(index, vegetable)


#here we extract the dara from the dictionary(Curly braces wrapped data)
# FruitList = {"Apple":100, "Banana":60, "Guava":80}
# for fruit, cost in FruitList.items():
#     print(fruit, "Cost: ", cost)

#Nested Loop
# for i in range(2):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

# Break & Continue
# for num in range(1, 50):
#     if(num == 2):
#         print("2 is skipped")
#         continue
#     elif(num % 5 == 0):
#         print("Number divisible 5 are skipped")
#         continue
#     else:
#         print(num)

#here we are iterating the values from the array put inside the another array after performing some modification to the values
# list_a = [1, 2, 3, 4, 5]
# list_b = []
# for num in list_a:
#     print(num)
#     list_b.append(num ** 3)

# print(list_b)