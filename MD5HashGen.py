import requests
import re
import hashlib

url = "<your-URL"

# Session for Cookie
session = requests.Session()

#get needed Stuff
response = session.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the website: {response.status_code}")
    exit()

#Regex to find needed string after h3
pattern = r'<h3 align=\'center\'>(.*?)</h3>'
match = re.search(pattern, response.text)
if not match:
    print("String not found in the source code.")
    exit()

# Match the right group
specific_string = match.group(1)

# generate hash
md5_hash = hashlib.md5(specific_string.encode()).hexdigest()

# Post data
post_data = {
    "hash": md5_hash  
} 
 
# Cookie with session for post 
response = session.post(url, data=post_data)

if response.status_code == 200:
    print(f"POST request successful. Response: {response.text}")
else:
    print(f"Failed to send the POST request: {response.status_code}")
