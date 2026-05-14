import requests

target = "http://192.168.1.1/goform/"
# Common Tenda backend form names
wordlist = ["login", "LoginAuth", "checkpassword", "setSysPassword", "getSysStatus", "adv_remotemanage", "SafeLoginCheck"]

for word in wordlist:
    url = target + word
    try:
        r = requests.get(url, timeout=2)
        # We are looking for anything that ISN'T "Form not defined"
        if "not defined" not in r.text:
            print(f"[!] FOUND ACTIVE ENDPOINT: {url} | Status: {r.status_code}")
    except:
        pass

