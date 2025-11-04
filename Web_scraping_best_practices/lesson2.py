# Analyse and find the bug.
"""
The target is to put a timeout of 2 seconds for a request

"""

import requests

url = "https://postman-echo.com/delay/10"

try:
    response = requests.get(url, timeout=2)
    print(response.text)
except requests.Timeout:
    print("The request timed out")