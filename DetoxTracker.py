
import time,re

StartTime = time.perf_counter()
StopTime = time.perf_counter()
Duration = StopTime - StartTime

UserDataDetails = {"First Name":"None","Surname":"None","Mobile Number +254":"None","Email":"None","Password":"None"}
class UserRegistrationAndLogin:
   @staticmethod
   def GetUserDetails(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
      while not(ConditionFunc(Val := input(Prompt))):
         print(f"[!]Error {Val} is not allowed.\n{ErrMsg}")
      UserDataDetails[key] = Val
      return Val

   @staticmethod
   def GetUserLoginDetails(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(Val:= input(Prompt)):
         print("!! Error {Val} is Invalid.{ErrMsg}")
      return Val

   @classmethod
   def UserDetailsCollect(cls,UserDataDetails):
      print("\n>>> Account SignUp >>>\n")
      cls.HomeInstance = Home(UserDataDetails)
      cls.FirstName = cls.GetUserDetails("\n>>> First Name :",lambda x: x.isalpha() and len(x) < 8,f">>> Should Contain 8 characters...Invalid Try Again",UserDataDetails,"First Name")
      cls.Surname = cls.GetUserDetails("\n>>> Surname :",lambda x: x.isalpha() and len(x) < 8,"Should Contain 8 characters...Invalid Try Again",UserDataDetails,"Surname")
      cls.PhoneNumber = cls.GetUserDetails("\n>>> Phone Number\n>>> +254:",lambda x: x.isdigit() and len(x) == 9 and x[0] in '17',"Number should start 7 or 1...Invalid Try Again",UserDataDetails,"Mobile Number +254")
      cls.Email = cls.GetUserDetails("\n>>> Email :",lambda x: re.search(r"^[a-zA-Z0-9_.$]+@[a-zA-Z0-9_y]+\.[a-zA-Z@$-]",x),"Invalid Email...Try Again",UserDataDetails,"Email")
      cls.Password = cls.GetUserDetails("\n>>> Create Login Password :",lambda x: re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$&+/£¢€¥∆]).{8,}",x),">>> Create a strong Password...Try Again",UserDataDetails,"Password")
      return cls.LoginPage(UserDataDetails,cls.HomeInstance)

   @classmethod
   def LoginPage(cls,UserDataDetails,HomeInstance):
      print("\n>>>    Account Login    >>>\n")
      cls.LoginEmail = cls.GetUserLoginDetails(">>> Enter your Email/Mobile Number +254:",lambda x:x in [UserDataDetails["Email"],UserDataDetails["Mobile Number +254"]],">>> Account doesn't EXIST")
      cls.LoginPassword = cls.GetUserLoginDetails(">>> Enter Your Password:",lambda y: y == UserDataDetails["Password"],">>> Wrong Password...Try Again")
      return HomeInstance.HomeIntro(UserDataDetails)

class Home:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails

   @staticmethod
   def GetHomeInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(HomeVal = input(Prompt)):
         print(f">>> {HomeVal} is not allowed.\n{ErrMsg}")
      return HomeVal


   @classmethod
   def HomeIntro(cls,UserDataDetails):
      cls.AccountEditsInstance = AccountEdit(UserDataDetails)
      cls.HomeIntroOption = cls.GetHomeInputs(">>> Home\n 1:account:",lambda x:x in ['1','2','3','4','5'],">>> Please select 1-5...Try Again")
      if cls.HomeIntroOption == '1':return cls.AccountEditsInstance.AccountEditsIntro(UserDataDetails)


class AccountEdit:
   def __init__(self,UserDataDetails):
      self.UserDataDetails = UserDataDetails

   @staticmethod
   def GetUserEdits(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(UsrEditsVal = input(Prompt)):
         print(f">>> {UsrEditsVal} is not allowed.\n{ErrMsg}")
      return UsrEditsVal

   @staticmethod
   def UserEditsControl(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
      while not ConditionFunc(EditVal := input(Prompt)):
         print(f">>> {EditVal} is not allowed.\n{ErrMsg}")
      UserDataDetails[key] = EditVal
      return EditVal

   @classmethod
   def AccountEditsIntro(cls,UserDataDetails):
      cls.AccountEditOption = cls.GetUserEdits(">>>    Account Section    >>>\n>> 1: Edit Profile\n>> 2: Personal Credetials\n>> 3: Change Password\n>> 4: Change Language\n>> 5: Disable/Delete Account\n>> 6: Main Menu\n>>> Option :",lambda x:x in ['1','2','3','4','5'],">>> Please Select 1-5...Try Again")
      if cls.AccountEditOption == '1':return  cls.UserProfileEdits(UserDataDetails)
      elif cls.AccountEditOption == '2':pass







   @classmethod
   def UserProfileEdits(cls,UserDataDetails):
      """ Profile Edits """
      cls.UserProfile = cls.GetUserEdits(">>>    Profile    >>>\n> 1: First Name\n> 2: Last Name\n> 3: Username\n> 4: Bio\n> 5: Go Back\n>>> OPTION :",lambda x: x in ['1','2','3','4'],">>> Please select 1-4...Try Again")
      if cls.UserProfileEdiits == '1':return cls.FirstNameEdits(UserDataDetails)
      elif cls.UserProfileEdits == '2':return cls.LastNameEdits(UserDataDetails)
      elif cls.UserProfileEdits == '3':return cls.UsernameEdits(UserDataDetails)
      elif cls.UserProfileEdits == '4':return cls.UserBioEdits(UserDataDetails)
      else:return cls.AccountEditsIntro(UserDataDetails)

   def FirstNameEdits(self,UserDataDetails):
      self.NewFirstName = self.UserEditsControl(f">>>   First Name Section   >>>\n>> Current Name :{UserDataDetails["FirstName"]}\n\n>>> New First Name :",lambda x:x.isalpha() and len(x) < 8,">>> Name should contain 8 char and no digits",UserDataDetails,"FirstName")
      self.FirstNameContinue = self.GetUserEdits(">>> Continue with ;\n>> 1: Edit First name\n2:Go Back\n>>> Option :",lambda x: x in ['1','2'],">>> Please select 1 or 2...Try Again")
      if self.FirstNameContinue == '1':return self.FirstNameEdits(UserDataDetails)
      else :return self.AccountEditsIntro(UserDataDetails)


   def SurnameEdits(self,UserDataDetails):
      self.Surname = self.UserEditsControl(f">>>   Surname  Section   >>>\n>> Current Name :{UserDataDetails["Surname"]}\n\n>>> New Surname :",lambda x:x.isalpha() and len(x) < 8,">>> Name should be of Max 8 char and no digits",UserDataDetails,"Surname")
      self.SurnameContinue = self.GetUserEdits(">>> Continue with ;\n>> 1: Edit Surname\n2:Go Back\n>>> Option :",lambda x: x in ['1','2'],">>> Please select 1 or 2...Try Again")
      if self.SurnameNameContinue == '1':return self.SurnameNameEdits(UserDataDetails)
      else :return self.AccountEditsIntro(UserDataDetails)

   def UsernameEdits(self,UserDataDetails):
      self.UsernameChanged = self.UserEditControl(f">>>   Username   >>>\n>> Current Username :{UserDataDetails["Username"]}\n\n>>> New Username :",lambda x:re.search(r"^(?=.*\d)(?=.*[a-z])(?=.*[@_.©®™])",x),UserDataDetails,"Username")
      self.UsernameContinue = self.GetUserEdits(">>> Continue with ;\n> 1: Edit Username\n> 2: Main Menu",lambda x:x in ['1','2'],">>> Select 1-2...Try Again")
      if self.UsernameContinue == '1':return self.UsernameEdits(UserDataDetails)
      else:return self.AccountEditsIntro(UserDataDetails)

   def UserBioEdits(self,UserDataDetails):
      self.UserBioChanged = self.UserEditsControl(f">>>   User Bio   >>>\n>> Current Bio :{UserDataDetails["Bio"]}\n\n>>> Your New Bio :",lambda y:y.isalpha() and len(y) < 25,">>> Invalid Bio",UserDataDetails,"Bio")
      self.UserBioContinue = self.GetUserEdits(">>> Continue with;\n> 1: Edit Bio\n> 2: Main Menu\n>>> OPTION :",lambda x:x in ['1','2'],">>> Please Select 1-2")
      if self.UserBioContinue == '1':return self.UserBioEdits(UserDataDetails)
      else:return self.AccountEditsIntro(UserDataDetails)




if __name__ == '__main__':
   StartTime
   UserRegistrationAndLogin.UserDetailsCollect(UserDataDetails)
   #Home.UserDataCheck(UserDataDetails)
   StopTime
   print(f">>>Time Taken To Run the program :{Duration}seconds")
