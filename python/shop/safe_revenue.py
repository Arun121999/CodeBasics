import json
import logging

logging.basicConfig(
    filename="shop/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s" #time, log level, log message
),
    
# logging.debug()	detailed info, only useful while developing
# logging.info()	normal, expected events ("started", "finished")
# logging.warning()	something odd but not breaking anything
# logging.error()	something failed
# logging.critical()	the whole program/pipeline is about to fail

with open("shop/orders.json") as file:
    data = json.load(file)
    logging.info("Load orders.json successfully")

    revenue = {}
    for order in data['orders']:
        try:
            order_id = order['order_id']
            customer = order['customer']
            for item in order['items']:
                line_total = item['price'] * item['quantity']
                revenue[customer] = revenue.get(customer,0) + line_total
        except Exception as e:
                logging.warning(f"Skipping order {order.get('order_id')} — missing field: {e}")


    logging.info(f"Finished processing. Total customers: {len(revenue)}")
