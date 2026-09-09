# List Slicing
# numbers = [1,2,3,4,5,6]
# print(numbers[0]) # 1
# print(numbers[1:3]) # [2,3]
# print(numbers[:3]) # [1, 2, 3]
# print(numbers[0:]) # [1, 2, 3, 4, 5, 6]
# print(numbers[-2:]) #[5, 6]

#Sorting 
# scores = [80, 90, 20, 93, 55]
# scores.sort() #Sorting in ascending order [20, 55, 80, 90, 93]
# print(scores)
# scores.sort(reverse=True) #Sorting in descending order [93, 90, 80, 55, 20]
# print(scores)



#Sorting (Here the original array will not be disturbed)
# scores = [80, 90, 20, 93, 55]

# # 1. Sorting in ascending order
# updatedscoreasc = sorted(scores) 
# print(updatedscoreasc)   # Output: [20, 55, 80, 90, 93]

# # 2. Sorting in descending order
# updatedscoredesc = sorted(scores, reverse=True) 
# print(updatedscoredesc)  # Output: [93, 90, 80, 55, 20]

# # 3. Original list remains unchanged
# print(scores)            # Output: [80, 90, 20, 93, 55]


#Sorting of array on specific key based
# orders = [
#     {"item": "Laptop", "price": 50000},
#     {"item": "Mouse", "price": 1500},
#     {"item": "Keyboard", "price": 2000}
# ]

# sorted_orders = sorted(orders, key=lambda order: order["item"])
# for o in sorted_orders:
#     print(o["item"], o["price"])

# tuples (we use () for tuples and it does not support assignment operation)
# point = (10, 20)
# print(point[0])     # 10
# print(point[1])     # 20

# point[0] = 99        # this will throw an error!


# A list - can change, good for a shopping cart that grows
# cart = ["apple", "banana"]
# cart.append("mango")
# print(cart)

# # A tuple - fixed, good for something that should never change
# coordinates = (28.7041, 77.1025)   # latitude, longitude of Delhi

# function defining and aggregate function
# def get_min_sum_max_len(numbers):
#     return min(numbers), sum(numbers), max(numbers), len(numbers)

# min, sum, max, len = get_min_sum_max_len([2,4,6])
# print(min, sum, max, len)

# scores = [2, 5, 20, 90, 60, 76]
# scores.sort() #here sorting will disturb the actural resource (asc)
# print(scores)
# scores.sort(reverse=True) #here sorting will disturb the actural resource (desc)
# print(scores)
# scores.sort(reverse=True) #here sorting will disturb the actural resource (desc)
# print(scores[3]) 
#Note : Here notice one thing if the value inside the square is without : then it show the value which lies on that index other wise
#the values inside the square acts as range [start, end]

# sortedscores = sorted(scores, reverse=True)[:3]
# print(sortedscores)