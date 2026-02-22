import requests
try:
    r = requests.get('http://127.0.0.1:5001/api/search')
    print("Status:", r.status_code)
    print("JSON:", r.json())
except Exception as e:
    print("Error:", e)
