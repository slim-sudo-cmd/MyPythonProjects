
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
      else:return None




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

class Vacation:
   class hire_Servicss(Vacation):

      @staticmethod
      def hireServices_Continue(prompt,conditionFunc,errMsg):
         while not conditionFunc(val := input(prompt)):
            print(f">>> {val} is Not Allowed !!.\n{errMsg}")
         return val

      @classmethod
      def hire_service_Intro(cls):
         print("\n__________ Hire Service Intro __________\n")
         if (hireSearvice_Opt := int(cls.hireService_Continue("\n>> 1: ",lambda y:y.isdigit() and int(y) in [1,2,3,0],">>> Enter a valid Input !!"))) == 1:return cls.
   class vacation_Services(Vacation):pass


class AccountManagement:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails

   @classmethod
   def AccountSetting(cls):pass

   class Profile(AccountManagement):
      @staticmethod
      def ProfileInput_Continue(Prompt,ConditionFunc,ErrMsg):
         while not ConditionFunc(val:=input(Prompt)):
            print(f">>> {val} is not allowed.\n{ErrMsg}")
         return val

      @staticmethod
      def ProfileInput_Edit(Prompt,ConditionFunc,ErrMsg,UserDataDetails,Key):
         while not ConditionFunc(val:= input(Prompt)):
            print(f">>> {val} is not Allowed.\n{ErrMsg}")
         UserDataDetails[val] = key
         return val

      """ Profile intro """
      @classmethod
      def Profile_Intro(cls):
         print("\n__________ Profile __________\n")
         if (profile_Choice := int(ProfileInput_Continue("\n>> 1: Username\n>> 2: Name\n>> 3: Bio\n>> 4: Website\n>> 0: Go Back\n\n>>> Que Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,0],">>> Enter a valid Input !!"))) == 1:return cls.profile_Username()
         elif profile_Choice == 2:return cls.profile_Name()
         elif Profile_Choice == 3:return cls.profile_Bio()
         elif profile_Choice == 4:return cls.profile_Website()
         elif profile_Choice == 0:return home()
         else:return None

      @classmethod
      def profile_Username(cls):
         print("\n___________ Profile Username __________\n")
         if not cls.UserDataDetails["Username"]:print("You Don't have a Username Currently...")
         if (username_Choice := int(cls.ProfileInput_Continue(">> 1: Create/Edit Username\n>> 0: Go Back\n\n>>> Que Option :",lambda f:f.isdigit() and int() in [1,0],">>> Enter a valid Input !!"))) == 1:
            cls.ProfileInput_Edit(f"\n>>> Current Username :{UserDataDetails["Username"]}\n\n>>> Whats Your Username :",lambda y:y.isalnum() and len(y) <= 20,UserDataDetails,"Username")
            return cls.profile_Intro()
         elif username_Choice == 0:return cls.profile_Intro()
         else:return None


      @classmethod
      def profile_Name(cls):
         cls.usernames = [cls.UserDataDetails["First Name"],cls.UserDataDetails["Surname"]]
         print(f"\n__________ Profile Name __________\n\n>>> Current Name Info ;\n>> First name :{cls.usernames[0].capitalize}\n>> Surname :{cls.username[1].capitalize()}")
         if (profile_Edit_In := int(cls.ProfileInput_Continue("\n>> 1: First name\n>> 2: Surname\n>> 0: Go Back",lambda x:x.isdigit() and int(x) in [1,2,0],">>> Enter valid Input !!"))) == 1:
            cls.ProfileInput_Edit(">>> First Name :",lambda s:s.isalpha() and len(s) <= 15,">>> Enter valid Name !!",UserDataDetails,"First Name")
            return cls.profile_Intro()
         elif profile_Edit_In == 2:
            cls.ProfileInput_Edit("\n>>> Surname :",lambda f:f.isalpha() and len(f) <= 15,">>> Enter a valid Name !!",UserDataDetails,"Surname")
            return cls.profile_Intro()
         elif profile_Edit_In == 0:return cls.profile_Intro()
         else:return None

      @classmethod
      def profile_Bio(cls):
         print(f"\n___________ Profile Bio __________\n")
         if not cls.UserDataDetails["Bio"]:print(">>> Your Dont Have a Bio Yet!!")
         if (bio_Choice := int(cls.ProfileInput_Continue(f"\n>>> Current Bio :{cls.UserDataDetails["Bio"].title()}\n >> 1: Create/Edit Bio\n>> 0: Go Back\n\n>>> Que Option :",lambda f: f.isdigit() and int(f) in [1,0],">>> Enter a valid Input !!"))) == 1:
            cls.ProfileInput_Edit("\n>>> Whats Your Bio :",lambda x:x.isalnum() and len(x) <= 30,">>> Enter a valid Bio !!",UserDataDetails,"Bio")
            return cls.Profile_Intro()
         elif bio_Choice == 2:return cls.Profile_Intro()
         else:return None

   class Security(AccountManagement):
      @staticmethod
      def securityInput_Edit(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
         while not ConditionFunc(val := input(Prompt)):
            print(f"\n>>> {val} is not allowed.\n{ErrMsg}")
         UserDataDetails[key] = val
         return val

      @staticmethod
      def securityInput_Continue(Prompt,ConditionFunc,ErrMsg):
         while not ConditionFunc(val := input(Prompt)):
            print(f">>> {val} is not allowed !!.\n{ErrMsg}")
         return val

      @classmethod
      def Security_Intro(cls):
         print("\n__________ Security Intro __________\n")
         if (security_Choice := int(cls.securityInput_Continue("\n>>> Continue with ;\n>> 1: Change Password\n>> 2: Security Questions\n>> 3: 2 - way Authentication\n>> 0: Go Back\n\n>>> Que Option :",lambda x:x.isdigit() and int(x) in [1,2,3,0],">>> Enter a valid Input !!"))) == 1:
            print("\n__________ Change Of Password __________\n")
            cls.securityInput_Continue("\n>>> Old Password :",lambda x:x == UserDataDetails["Password"],">>> Wrong Password !!")
            cls.securityInput_Edit("\n>>> New Password :",lambda x:(r"^(?=.*[a-z])(?=.*[A-Z_@$])(?=.*\d)(?=.*[@#$&_-*?!/£¥π]){8,}",x) and x != cls.UserDataDetails["Password"],">>> Create a Strong Password & Should Be same as last !!",UserDataDetails,"Password")
            return cls.Profile_Intro()
         elif security_Choice == 2:return cls.securyQuestion_Intro()
         elif secury_Choices == 3:return cls.twoWay_Authentification()
         elif security_Choice == 0:return cls.Profile_Info()
         else:return None

      @classmethod
      def securityQuestion_Intro(cls):
         print("\n__________ Security Questions __________\n")
         if (secQuestion := int(cls.securityInput_Continue("\n>> 1: Create Question\n>> 2: Edit Questions\n>> 0: Go Back\n\n>>> Que Option :",lambda x:x.isdigit() and int(x) in [1,2,3,0],">>> Enter valid Input"))) == 1:
            cls.schoolName = cls.securityInput_Edit(">>> Your Primary School Name :",lambda x:x.isalpha() and len(x) <= 20,">>> Enter a valid School Name",UserDataDetails,"Primary Name")
            cls.favoriteColor = cls.securityInput_Edit(">>> Your Favorite color :",lambda x:x.isalpha() and len(x) <=10,">>> Enter a valid Color !!",UserDataDetails,"Color")
            cls.favoriteFood = cls.securityInput_Edit(">>> Your Favorite Food :",lambda x:x.isalpha() and len(x) <= 10,">>> Enter a valid Food !!",UserDataDetails,"Food")
            cls.shoeSize = cls.securityInput_Edit(">>> Your Shoe size :",lambda x:x.isdigit() and 30 <= int(x) <= 48,">>> Enter a valid School Name",UserDataDetails,"Shoe Size")
         elif secQuestion == 2:return cls.securityQuestion_Intro()
         else:return None
   class Finance(AccountManagement):
      Account = {}
      @staticmethod
      def financeInput_Continue(cls,prompt,ConditionFunc,errMsg):
         while not ConditionFunc(val := input(prompt)):
            print(f">>> {val} is not allowed !!.\n{errMsg}")
         return val

      @staticmethod
      def financeInput_User(cls,prompt,conditionFunc,errMsg,Account,key):
         while not ConditionFunc(val := input(prompt)):
            print(f">>> {val} is invalid !!.\n{errMsg}")
         Account[key] = val
         return val

      @classmethod
      def finacial_Intro(cls):
         print("\n__________ Account Intro __________\n\n>> 1: Reciepts\n>> 2: statement\n>> 3: Invest\n")
         if (accountChoice := int(cls.financeInput("\n>> 0: Go Back\n>>> Que Option :",lambda a:a.isdigit() and int(a) in [1,2,3,4,5,6,0],">>> Enter a valid Input !!"))) == 1:return cls.proofPayment()
         elif accountChoice == 2:return cls.statementInfo()
         elif accountChoice == 3:return cls.investInfo()
         elif accountChoice == 0:returns cls.account_Home()
         else:return None

      @classmethod
      def proofPayment(cls):
         print("\n__________ Reciepts __________\n\n>> 1: Today\n>> 2: Three day\n>> 3: Last Week\n>> 4: Last Month\n>> 5: All")
         if not Account[""][][]:print("\n>>> You Haven't made Any Transaction Yet")
         if (proofSelect := int(cls.financeInput_Continue("\n>> 0: Go Back\n>>> Que Option :",lambda r:r.isdigit() and int(r) in [1,2,3,4,0],">>> Enter a valid Input !!"))) == 1:

   class Account_Deletion(AccountManagement):
      @staticmethod
      def deleteInput_Continue(cls,prompt,conditionFunc,errMsg):
         while not ConditionFunc(val := input(prompt)):
            print(f">>> {val} is not allowed !!.\n{errMsg}")
         return val

      @classmethod
      def delete_Intro(cls):
         print("\n__________ Account Deletion __________\n")
         if (delAccount_Intro := int(cls.deleteInput_Continue("\n>>> What's Your wish ;\n>> 1: Temporary Disable\n>> 2: Permanent Deletion\n>> 0: Go Back\n>>> Que Option :",lambda y:y.isdigit() and int(y) in [1,2,0],">>> Enter a valid Input !!"))) == 1:return cls.temporaryDel()
         elif delAccount_Intro == 2:return cls.permanentDel()
         elif delAccount_Intro == 0:return cls.account_Home()
         else:return None

      @classmethod
      def temporaryDel(cls):
         cls.options = [1,2,3,4,0]
         print("\n__________ Temporary Disable Account __________\n\n>>> Fill to aid in Our experience;")
         cls.temp_Quiz = cls.deleteInput_Continue("\n>> 1: Personal Reason\n>> 2: Just a Break\n>> 3: Some Time Off\n>> 4: I'll be Back\n>> 0: Go Back\n\n>>> Que Option :",lambda y:y.isdigit() and int(y) in cls.options,">>> Enter a valid Input !!")
         if cls.temp_Quiz in cls.options:
            for x in range(5):
               cls.deleteInput_Continue("\n>>> Enter your Password :",lambda y: y == UserDataDetails["Password"],">>> Wrong Password !!")
               if x == 3:return cls.forget_Password()

      @classmethod
      def permanentDel(cls):
         print("\n__________ Permanent Deletion _________\n")
         if (deleteInput := int(cls.deleteInput_Continue("\n>> 1: Delete Account\n>> 0: Go Back\n\n>>> Que Option :",lambda x:x.isdigit() and int(x) in [0,1],">>> Enter a valid Input !!"))) == 1:
            cls.del_Option = cls.deleteInput_Continue("\n>>>  Enter Your Password :",lambda y:y == UserDataDetails["Password"],"\n>>> Wrong Password !!")
            if cls.del_Option != UserDataDetails["Password"]:
               if (permanent := int(cls.deleteInput_Continue("\n>>> Continue with ;\n>> 1:Forgot Password\n>> 0:Go Back\n\n>>> Que Option :",lambda y:y.isdigit() and int() in [1,0],">>> Enter a valid input !!"))) == 1:return cls.del_passwordRetrival()
               elif permanent == 2:return cls.account_Home()
               else:return None
            else:
               del UserDataDetails
               def timer(start=3,stop=0):
                  for x in range(start,stop,-1):print(x);time.sleep(1)
                  print(f"\n>>> Account Was Successfully Deleted")
               timer()
         elif deleteInput == 2:return cls.account_Home()
         else:return None

   class account_Retrival(AccountManagement):

      @staticmethod
      def accountInput_Continue(prompt,conditionFunc,errMsg):
         while not conditionFunc(val := input(prompt)):
            print(f">>> {val} is not Allowed !!.\n{errMsg}")
         return val

      @staticmethod
      def cod

      @classmethod
      def account_Retrival_Intro(cls):
         print("\n___________ Account Retrival __________\n")
         if (pass_Retrive := int(cls.accountInput_Continue("\n>> 1: Retrieve Account\n>> 2: Forgot Password\n>> 3: Check Login Details\n>> 0: Go Back\n\n>>> Que Option :",lambda c:c.isdigit() and int(c) in [0,1,2,3],">>> Enter a valid Input !!"))) == 1:return cls.retrieve_Account()
         elif pass_Retrive == 2:return cls.forgot_Password()
         elif pass_Retrive == 3:return cls.login_Details()
         else:return None

      @classmethod
      def retrieve_Account(cls):pass

      @classmethod
      def forgot_Password(cls):
         print("\n__________ Forgot Password __________\n")
         if (forgot_Pass := int(cls.accountInput_Continue("\n>> 1: Email\n>> 2: Mobile Number\n>> 0: Go Back\n\n>>> Que Option :",lambda b:b.isdigit() and int(b) in [0,1,2,3],">>> Enter a valid Input !!"))) == 1:return cls.email_Password()
         elif forgot_Pass == 2:return cls.phone_Pass()
         elif forgot_Pass == 0:return cls.account_Home()
         else:return None

      @classmethod
      def email_Pass():

      @classmethod
      def phone_Pass(cls):
         print("\n__________ Via Mobile Number __________\n")
         cls.accountInput_Continue(">>> Enter Mobile Number\n>>> +254 :",lambda v:v == UserDataDetails["Phone Number"],">>> Mobile Number Not Registered")

      @classmethod
      def login_Details(cls):pass







if __name__ == '__main__':
   UserRegistrationAndLogin.UserRegistration(UserDataDetails)
   Home.HomeDirectory()
