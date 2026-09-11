import csv

with open("shop/orders.csv", "r") as file:
    # reader = csv.reader(file)
    # for row in reader:
    #     print(row)
    #Note: Here we access the values using index

    # reader = csv.DictReader(file)
    # for row in reader:
    #     print(row)
    # #Note: Here, We access the value using key

    reader = csv.DictReader(file)
    revenue = {}
    for row in reader:
        customer = row["customer"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity #Here we are calculating the pricing of each product against the quantity
        

        # if(customer in revenue):
        #     revenue[customer] += line_total #If customer exist then we add the amount in the existing one.
        # else:
        #     revenue[customer] = line_total #If customer not exist then we assign the value to the customer

        revenue[customer] = revenue.get(customer, 0) + line_total #alternate of if statement

    print(revenue) 


with open("shop/revenue_by_customer.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["customer", "total_revenue"])   # header row
    for customer, total in revenue.items():
        writer.writerow([customer, total])

    print("Revenue file written successfully")