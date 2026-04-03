# External Modules

import requests # ModuleNotFoundError: No module named 'requests'
print(requests.status_codes)
r = requests.get('https://www.python.org/')
print("HTTP Status Code: ", r.status_code)

r = requests.get('https://www.python.org/ravi')
print("HTTP Status Code: ", r.status_code)

r = requests.get('https://www.python.org/')
print("HTTP Status Code: ", r.status_code)

if r.status_code != 200:
    print("API Not Functional")
else:
    print("API Functional")
    print("Fetching Data From API")
    

