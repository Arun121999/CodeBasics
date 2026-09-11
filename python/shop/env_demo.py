from dotenv import load_dotenv
import os

#pip install python-dotenv 
#for env
load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)