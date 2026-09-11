from shop.order import Order
from shop.pricing import calculate_gst

o = Order(101, "Arun")
o.add_item("Laptop", 50000)
o.add_item("Keyboard", 20000)

print(o.items)
print(o.total())
print(o.avg())

gst = calculate_gst(o.total())
print(gst)