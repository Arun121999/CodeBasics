import random
import time

def call_payment_api():
    random_num = random.random()
    if random_num > 0.5:
        raise ConnectionError("Payment server not responding")
    
    return "Payment Successful!"

max_attempts = 5
attempt = 1


while attempt <= max_attempts:
    try:
        result = call_payment_api()
        print(result)
        break
    except Exception as e:
        print(f"Attempt {attempt} failed: {e}")
        attempt += 1
        time.sleep(5)
else:
    print("All atempts failed!")