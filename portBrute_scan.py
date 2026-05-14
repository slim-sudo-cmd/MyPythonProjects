import subprocess,sys,re
class ipInput:
   @staticmethod
   def ip_validation(prompt,conditionFunc,errMsg):
      try:
         while not (val := input(prompt).strip()) or not conditionFunc(val):
            if val.lower() in ['exit','q']:
               print ("\n>>> [*] Bye have Nice Hunting Time ")
               sys.exit(0)
               return None
            print (f">>> [*]{errMsg}")
         return val
      except:
         print ("\n\n>>> [!] Interupt by the User...Cleaning Up")
         sys.exit(1)

   @classmethod
   def ipGet(cls,sys):
      cls.wordlists = "/usr/share/wordlists/dirb/common.txt"
      cls.ip_target = cls.ip_validation("\n>>> Target Ip :",lambda x:re.match(r"^\d{1,3}(\.\d{1,3}){3}$",x),"Enter a valid Ip Target eg...192.168.1.1")
      print (f"\n>>> [+] Checking {cls.ip_target} for port 80/53 if they are open....")
      cls.nmap_cmd = ["sudo","nmap","-p","80,53,","-Pn","--open",cls.ip_target]
      cls.results = subprocess.run(cls.nmap_cmd,capture_output=True,text=True)
      if "80/tcp open" in cls.results.stdout:
         print (f"\n>>> [+] Port 80 Open on {cls.ip_target}.\n>>> [+] Starting Gobuster....")
         cls.goBuster = ["gobuster","dir","-u",f"http://{cls.ip_target}","-w",cls.wordlists,"-z","500ms"]
         subprocess.run(cls.goBuster)
      elif "53/tcp open" in cls.results.stdout:
         cls.telTry = ["telnet",f"{cls.ip_target}","53"]
         subprocess.run(cls.telTry)
      else:print (f">>> [-] None of the Ports are Open (80,53) on {cls.ip_target}.")

if __name__ == '__main__':
   ipInput.ipGet(sys)
