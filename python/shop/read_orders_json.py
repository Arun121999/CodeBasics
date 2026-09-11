import json

with open("shop/orders.json", "r") as file:
    data = json.load(file)

#     print(data["store"])
#     print(data["city"])
#     print(data["orders"])

# for order in data['orders']:
#     print(order['order_id'], order['customer'], order['city'])

# for order in data['orders']:
#     for item in order['items']:
#         print(item['name'], item['price'], item['quantity'])

revenue = {}
for order in data['orders']:
    customer = order['customer']
    for item in order['items']:
        line_total = item['price'] * item['quantity']
        if(customer in revenue):
            revenue[customer] += line_total
        else:
            revenue[customer] = line_total

print(revenue)