from datetime import datetime, timedelta

# Simulate order data with dates (as strings, exactly how you'd get them from an API/CSV)
orders = [
    {"order_id": 101, "customer": "Arun", "order_date": "2026-09-01"},
    {"order_id": 102, "customer": "Priya", "order_date": "2026-09-08"},
    {"order_id": 103, "customer": "Rohit", "order_date": "2026-08-20"},
    {"order_id": 104, "customer": "Sahil", "order_date": "2026-09-10"},
]


# Step 1: Convert each order_date string into a real datetime object
for order in orders:
    order["order_date"] = datetime.strptime(order["order_date"], "%Y-%m-%d") #string to datetime
    # print(order["order_date"])

# Step 2: Get today's date
today = datetime.now()
print("Today is:", datetime.strftime(today, "%Y-%m-%d"))

# Step 3: Calculate how many days ago each order was placed
for order in orders:
    days_ago = (today - order["order_date"]).days
    print(f"Order {order['order_id']} ({order['customer']}) was placed {days_ago} days ago")

# Step 4: Filter orders from the last 7 days only
print("\n--- Orders in the last 7 days ---")
seven_days_ago = today - timedelta(days=7)
recent_orders = [o for o in orders if o["order_date"] >= seven_days_ago]


for order in recent_orders:
    print(order["order_id"], order["customer"], order["order_date"].strftime("%Y-%m-%d"))