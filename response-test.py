import requests
import time

url = 'http://127.0.0.1:5000/view-unread-books'

start_time = time.time()
response = requests.get(url)
end_time = time.time()

response_time = end_time - start_time

print(f"Response Time: {response_time:.3f} seconds")
