
import time,re

UserDataDetails = {"First Name":"None","Surname":"None","Mobile Number +254":"None","Email":"None","Password":"None"}
class UserRegistrationAndLogin:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails
      self.HomeInstance = Home(UserDataDetails)

   @staticmethod
   def GetUserDetails(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
      while not ConditionFunc(Val:=input(Prompt)):
         print(f">>> !!! Error {Val} is not Allowed.\n{ErrMsg}")
      UserDataDetails[key] = Val
      return Val

   @staticmethod
   def GetUserLoginDetails(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(Val:=input(Prompt)):
         print(f">>> !!! Error {Val} is Invalid.\n{ErrMsg}")
      return Val

   @classmethod
   def UserRegistration(cls,UserDataDetails):
      HomeInstance = Home(UserDataDetails)
      print("\n>>> Account Creation >>>\n")
      cls.FirstName = cls.GetUserDetails("\n>>> First Name :",lambda x: x.isalpha() and len(x) < 8,">>> Enter a valid name...Try Again",UserDataDetails,"First Name")
      cls.Surname = cls.GetUserDetails("\n>>> Surname :",lambda x: x.isalpha() and len(x) < 8,">>> Enter a valid Name...Try Again",UserDataDetails,"Surname")
      cls.PhoneNumber = cls.GetUserDetails("\n>>> Mobile Number\n+254:",lambda x:x.isdigit() and len(x) == 9 and x[0] in '17',">>> Mobile Number should start 1 or 7...Try Again",UserDataDetails,"Mobile Number +254")
      cls.Email = cls.GetUserDetails("\n>>> Email :",lambda x: re.search(r"^[a-zA-Z0-9-_+]+@[a-zA-Z#$_]+\.[a-zA-Z+$]",x),">>> Enter a valid Email",UserDataDetails,"Email")
      cls.Password = cls.GetUserDetails("\n>>> Create Login Password :",lambda x:re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$&+£¢¥¥])",x),">>> Create a strong password",UserDataDetails,"Password")
      return cls.UserAccountLogin(UserDataDetails,HomeInstance)

   @classmethod
   def UserAccountLogin(cls,UserDataDetails,HomeInstance):
      cls.LoginEmail = cls.GetUserLoginDetails("\n>>>   Welcome to Login Page   >>>\n>>> Enter Email/Mobile Number +254:",lambda x:x in [UserDataDetails["Email"],UserDataDetails["Mobile Number +254"]],">>> Account Doesn't exists")
      cls.LoginPassword = cls.GetUserLoginDetails("\n>>> Enter Your Password :",lambda x:x == UserDataDetails["Password"]," >>>Wrong Password")
      return HomeInstance.HomeDirectory(UserDataDetails)

class Home:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails
#   @staticmethod
 #  def UserDetailsCheck(UserDataDetails):
  #    for key,value in UserDataDetails.items():
   #      print(f">>> {key}:{value}")

   @staticmethod
   def HomeDashBoard(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(Val:= input(Prompt)):
         print(f">>> {Val} is invalid.\n{ErrMsg}")
      return Val


   @classmethod
   def HomeDirectory(cls,UserDataDetails):
      print(">>>   Home Directory   >>>\n")
      cls.routeAvailable = {"1":"Nairobi","2":"Naivasha","3":"Nakuru","4":"Kericho","5":"Owasi","6":"Ahero","7":"Kisumu","8":"Maseno","9":"Luanda","10":"Bumala","11":"Busia","12":"Kisii","13":"Nyamira","14":"Turgen","15":"Bomet","16":"Mombasa"}
      for key,value in cls.routeAvailable.items():
         print(f"{key}:{value}")
      cls.HomeFrom = cls.HomeDashBoard("\n>>> From :",lambda x:x in cls.routeAvailable or x.capitalize() in cls.routeAvailable.values(),">>> Currently route is unavailable...Try another routes")
      cls.HomeTo = cls.HomeDashBoard("\n>>> To",lambda y: y in cls.routeAvailable or x.capitalize() in cls.routeAvailable.values(),">>> Currently route is unavailable...Try Other route")
      cls.destinationEdits = cls.HomeDashBoard("\n>>> $1:Search\n>>> $2:Edit routes\n>>> Your Option : ",lambda x:x in ['1','2'],">>> Select 1 or 2 to Edit or Continue.")
      if cls.destinationEdits == '1':pass
      elif cls.destinationEdits == '2':return cls.HomeDirectory(UserDataDetails)
      pass




class Routes:
   def __init__(self,data = None):
      self.data = data
      self.next = None

class routeList:
   def __init__(self):
      self.head = Routes()

   def appendSeat(self,data):
      self.newSeat = Routes(data)
      self.currentSeat = self.head
      while self.currentSeat.next != None:
         self.currentSeat = self.currentSeat.next
      self.currentSeat.next = self.newSeat

   def seatLength(self):
      self.total = 0
      self.currentSeat = self.head
      while self.currentSeat.next != None:
         self.currentSeat = self.currentSeat.next
         self.total +=1
      return self.total

   def seatDisplay(self):
      self.Element = []
      self.currentSeat = self.head
      while self.currentSeat.next != None:
         self.currentSeat = self.currentSeat.next
         self.Element.append(self.currentSeat.data)
      return self.Element

   def getSeat(self,index):
      if index > self.seatLength():
         print(">>> Oops Out of range")
         return None
      self.currentSeat = self.head
      self.currentIndex = 0
      while True:
         self.currentSeat = self.currentSeat.next
         if self.currentIndex == index:return self.currentSeat.data
         self.currentIndex += 1


class AccountManagement:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails

   @classmethod
   def AccountSetting(cls):pass








if __name__ == '__main__':
   print(">>> SLIM COACHES >>>")
   UserRegistrationAndLogin.UserRegistration(UserDataDetails)
   Home.HomeDirectory()
   #home = routeList()
  # home.seatDisplay()
   #print(f">>> list before append :{home.seatDisplay()}")
   #home.appendSeat(2)
  # home.appendSeat(5)
 #  home.appendSeat(6)
#   print(f">>> list after append :{home.seatDisplay()}")

