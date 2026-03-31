
import numpy as np
import re,time

UserDataDetails = {"First Name":"None","Surname":"None","Mobile +254":"None","Email":"None","Bio":"None","Username":"None","Security Questions":"None"}
Array = np.array([[1,2,3],[4,5,6],[7,8,9]])
class RegistrationAndLogin:
   def __init__(self,UserDataDetails,Array):
      self.UserDataDetails = UserDataDetails
      self.Array = Array

   @staticmethod
   def UserValidInputs(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
      while not ConditionFunc(Val:= input(Prompt)):
         print(f">>> {Val} is Invalid.\n{ErrMsg}")
      UserDataDetails[key] = Val
      return Val

   @staticmethod
   def GetUserLoginDetails(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(Val:= input(Prompt)):
         print(f">>> {Val} is Invalid.\n{ErrMsg}")
      return Val

   @classmethod
   def UserAccountRegistration(cls,UserDataDetails,Array):
      print("\n>>>   Account SignUp   >>>")
      cls.HomeInstance = Home(UserDataDetails,Array)
      cls.FirstName = cls.UserValidInputs("\n>>> First Name :",lambda x: x.isalpha() and len(x) < 8,">>> Name Should Contain letters and max lenth of 8 character",UserDataDetails,"First Name")
      cls.Surname = cls.UserValidInputs("\n>>> Surname :",lambda y:y.isalpha() and len(y) < 8,">>> Name Should Contain letters and max lenth of 8 character",UserDataDetails,"Surname")
      cls.MobileNumber = cls.UserValidInputs("\n>>> Mobile Number\n>>> +254 :",lambda p: len(p) == 9 and p[0] in ['1','7'],">>> Phone number should start with 1 or 7",UserDataDetails,"Mobile +254")
      cls.Email = cls.UserValidInputs("\n>>> Email :",lambda y: re.search(r"^[a-zA-Z0-9_&#]+@[a-zA-Z]+\.[a-zA-Z_#$]",y),">>> Invalid Email...Try Again",UserDataDetails,"Email")
      cls.Password = cls.UserValidInputs("\n>>> Create Password :",lambda x:re.search(r"^(?=.*[a-z])(?=.*\d)(?=.*[@#$/£¢§∆π√®✓%]).{8,}",x),">>> Create a Strong password",UserDataDetails,"Password")
      cls.DateOfBirth = int(cls.UserValidInputs("\n>>> Date Of Birth :",lambda x:x.isdigit() and int(x) <= 31,">>> Enter a valid Birth date eg 1-31 to yours",UserDataDetails,"Date Of Birth"))
      cls.MonthDay = int(cls.UserValidInputs("\n>>> Month Date:",lambda x:x.isdigit() and int(x) <= 12,">>> Enter a valid Month eg 1-12",UserDataDetails,"Month Date"))
      cls.YearOfBirth = int(cls.UserValidInputs("\n>>> Year of Birth :",lambda y:y.isdigit() and int(y) >= 1940 and int(y) <= 2008,">>> Age Not Valid to sign up",UserDataDetails,"Year Of Birth" ))
      return cls.UserAccountLogin(UserDataDetails,cls.HomeInstance)

   @classmethod
   def UserAccountLogin(cls,UserDataDetails,HomeInstance):
      print("\n>>>   Welcome To Login   >>> ")
      cls.LoginEmail = cls.GetUserLoginDetails("\n>>> Enter Your Email/Mobile Number :",lambda x:x in [UserDataDetails["Email"],UserDataDetails["Mobile +254"]],">>> Account doesn't Exists")
      cls.LoginPassword = cls.GetUserLoginDetails("\n>>> Enter Your Password:",lambda x:x == UserDataDetails["Password"],">>> Wrong Password...Try Again")
      def TimerLag(start=3,stop=0):
         print("\n>>> Please wait...")
         for x in range(start,stop,-1):
            print(x)
            time.sleep(1)
      TimerLag()
      return HomeInstance.HomePageIntro(UserDataDetails,Array)

class Home:
   def __init__(self,UserDataDetails,Array):
      self.UserDataDetails = UserDataDetails
      self.Array = Array

   @staticmethod
   def GetHomeDetails(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(HomeDetVal := input(Prompt)):
         print(f">>> {HomeDetVal} is Not allowed.\n{ErrMsg}")
      return HomeDetVal

   @classmethod
   def HomePageIntro(cls,UserDataDetails,Array):
      cls.NumpyInstance = ArrayActivity(UserDataDetails,Array)
      cls.TrialInstance = TrialExplore(UserDataDetails,Array)
      cls.HelpPageInstance = HelpPage(UserDataDetails,Array)
      cls.AccountSettingInstance = AccountSettings(UserDataDetails,Array)
      print(">>>   Home Page   >>>")
      cls.HomeIn = int(cls.GetHomeDetails("\n>> 1: Numpy Operations\n>> 2: Trials Explore\n>> 3: Account Setting\n>> 4: Help Page\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4],">>> Please select 1-4."))
      if cls.HomeIn == 1:return cls.NumpyInstance.ArrayInputsIntro(UserDataDetails,Array)
      elif cls.HomeIn == 2:return cls.TrialInstance.TrialExploreIntro(UserDataDetails,Array)
      elif cls.HomeIn == 3:return cls.AccountSettingInstance.AccountSettingIntro(UserDataDetails,Array)
      elif cls.HomeIn == 4 :return cls.HelpPageInstance.HelpIntro(UserDataDetails,Array)
      else :return None

class AccountSettings:
   def __init__(self,UserDataDetails,Array):
      self.UserDataDetails = UserDataDetails
      self.Array = Array

   @staticmethod
   def GetAccountInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(AccountVal := input(Prompt)):
         print(f">>> {AccountVal} is Invalid.\n{ErrMsg}")
      return AccountVal

   @staticmethod
   def GetAccountEdits(Prompt,ConditionFunc,ErrMsg,UserDataDetails,key):
      while not ConditionFunc(AccountEdits := input(Prompt)):
         print(f"{AccountEdits} is invalid.\n{ErrMsg}")
      UserDataDetails[key] = AccountEdits
      return AccountEdits

   @classmethod
   def AccountSettingIntro(cls,UserDataDetails,Array):
      """ Account Activities """
      print("\n>>>    Account Setting    >>>\n")
      cls.HomeInstance = Home(UserDataDetails,Array)
      cls.AccountMenu = int(cls.GetAccountInputs("\n>>> 1:Edit Profile information\n>>> 2:Security & Credentials\n>>> 3:Privacy Setting\n>>> 4:Notifications Preference\n>>> 5:Account Deletion/Activation\n>>> 6:Subscription & biling\n>>> 7: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,5,6,7],">>> Please Select 1-7"))
      if cls.AccountMenu == 1:return cls.ProfileEdits(UserDataDetails)
      elif cls.AccountMenu == 2:return cls.SecurityEdits(UserDataDetails)
      elif cls.AccountMenu == 3:return cls.PrivacyEdits(UserDataDetails)
      elif cls.AccountMenu == 4:return cls.NotificationsEdits(UserDataDetails)
      elif cls.AccountMenu == 5:return cls.AccountDeletion(UserDataDetails)
      elif cls.AccountMenu == 6:return cls.SubscriptionEdits(UserDataDetails)
      elif cls.AccountMenu == 7:return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
      else : return None

   """ Profile Edits genesis"""
   @classmethod
   def ProfileEdits(cls,UserDataDetails):
      """ Profile Setting """
      cls.ProfileData = {"First name": UserDataDetails["First Name"],"Surname":UserDataDetails["Surname"],"Bio": UserDataDetails["Bio"],"Username":UserDataDetails["Username"]}
      print("\n>>> Current Profile Details :")
      print(*(f"-{key}:{value}" for key,value in cls.ProfileData.items()),sep="\n")
      cls.ProfileEditOption = int(cls.GetAccountInputs("\n>>> Edit any Profile info;\n>> 1: First Name\n>> 2: Surname\n>> 3: UserName\n>> 4: Bio\n>> 5: Profile Picture\n>> 6: Go Back\n>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,5,6],">>> Please select 1-6"))
      if cls.ProfileEditOption == 1:return cls.FirstNameEdits(UserDataDetails)
      elif cls.ProfileEditOption == 2:return cls.SurnameEdits(UserDataDetails)
      elif cls.ProfileEditOption == 3:return cls.UsernameEdits(UserDataDetails)
      elif cls.ProfileEditOption == 4:return cls.UserBioEdits(UserDataDetails)
      elif cls.ProfileEditOption == 5:return cls.ProfilePic(UserDataDetails)
      elif cls.ProfileEditOption == 6:return cls.AccountSettingIntro(UserDataDetails,Array)
      else:return None

   @classmethod
   def FirstNameEdits(cls,UserDataDetails):
      cls.NewFirstName = cls.GetAccountEdits(f"\n>>> Current First name :{UserDataDetails["First Name"].capitalize()}\n\n>>> New First Name :",lambda y: len(y) <= 8 and y.isalpha(),">>> Name should have Max Char 8 and all alphabets",UserDataDetails,"First Name")
      cls.NewFirstNameContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit new name\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.NewFirstNameContinue == 1:return cls.FirstNameEdits(UserDataDetails)
      elif cls.NewFirstNameContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def SurnameEdits(cls,UserDataDetails):
      cls.Surname = cls.GetAccountEdits(f"\n>>> Current Surname :{UserDataDetails["Surname"].capitalize()}\n\n>>> New Surname :",lambda x: len(x) <= 8 and x.isalpha(),">>> Name should have Max 8 Char",UserDataDetails,"Surname")
      cls.SurnameContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit new name\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and x in ['1','2'],">>> Please select 1-2"))
      if cls.SurnameContinue == 1:return cls.SurnameEdits(UserDataDetails)
      elif cls.SurnameContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def UsernameEdits(cls,UserDataDetails):
      cls.NewUsername = cls.GetAccountEdits(f"\n>>> Current Username :{UserDataDetails["Username"]}\n\n>>> New Username :",lambda x:re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_.©®™])",x),">>> Username should contain (eg... _.@)",UserDataDetails,"Username")
      cls.NewUsernameContinue = cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Username\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and x in ['1','2'],">>> Please select 1-2")
      if cls.NewUsernameContinue == 1:return cls.UsernameEdits(UserDataDetails)
      elif cls.NewUsernameContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def UserBioEdits(cls,UserDataDetails):
      cls.NewUserBio = cls.GetAccountEdits(f"\n>>> Current Bio :{UserDataDetails["Bio"]}\n\n>>> New Bio :",lambda x:x.isalnum() and len(x) < 25,">>> Bio should not exceed 25 characters",UserDataDetails,"Bio")
      cls.NewUserBioContinue = int(self.GetAccountInputs(">>> Continue with ;\n>> 1: Edit bio\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.NewUserBioContinue == 1:return cls.UserBioEdits(UserDataDetails)
      elif cls.NewUserBioContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def UserProfilePicEdit(cls,UserDataDetails):
      print("\n>>> Oooops This section under Development >>>\n")
      cls.UserProfilePicContinue = int(self.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Profile picture\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.UserProfilePicContinue == 1:return cls.UserProfilePicEdit(UserDataDetails)
      elif cls.UserProfilePicContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   """ Security  Setting Genesis """
   @classmethod
   def SecurityEdits(cls,UserDataDetails):
      print("\n>>>    Security Edits    >>>\n")
      cls.SecurityEditsIntro = int(cls.GetAccountInputs(">>> Security Implements;\n>> 1: Change Password\n>> 2: 2-way Authentification\n>> 3: Security Questions\n>> 4: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4],">>> Please select 1-4"))
      if cls.SecurityEditsIntro == 1:return cls.PasswordEdits(UserDataDetails)
      elif cls.SecurityEditsIntro == 2:return cls.TwoWayAuntificationEdits(UserDataDetails)
      elif cls.SecurityEditsIntro == 3:return cls.SecurityQuestionsEdits(UserDataDetails)
      else:return None


   @classmethod
   def PasswordEdits(cls,UserDataDetails):
      cls.NewPassword = cls.GetAccountInputs("\n>>> New Login Password :",lambda x:re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$&_£¢∆¥π]).{8,}",x) and x != UserDataDetails["Password"],">>> Create a Strong Password and should be same as Old")
      cls.NewPasswordConfirm = cls.GetAccountEdits("\n>>> Confirm Password :",lambda x: x == cls.NewPassword,">>> Password Mismatched...Try Again",UserDataDetails,"Password")
      cls.PasswordContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Password\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.PasswordContinue == 1:return cls.PasswordEdits(UserDataDetails)
      elif cls.PasswordContinue == 2:return cls.AccountSettingIntro(UserDataDetails)
      else:return None

   @classmethod
   def TwoWayAuthentificationEdits(cls,UserDataDetails):
      cls.TwoAuthContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit 2-way Authentication\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.TwoAuthContinue == 1:return cls.TwoWayAuthentificationEdits(UserDataDetails)
      elif cls.TwoAuthContinue == 2:return cls.AccountSettingIntro(UserDataDetails)
      else:return None

   @classmethod
   def SecurityQuestionsEdits(cls,UserDataDetails):
      print("\n>>>   Security Questions   >>>\n-> Question are categorized into 3 that is;\n• Personal\n• Favorites\n• Unique & Obscure\n>>> Each category 3 questions are needed.")
      while True:
         if int(cls.GetAccountInputs("\n>>> Continue with;\n>> 1: Set Questions\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2")) == 1:break
         else:return cls.SecurityEdits(UserDataDetails)
      cls.SchoolName = cls.GetAccountEdits("\n>>> Your First School Name:",lambda y:y.isalpha() and len(y) <= 8,">>> Enter a valid school name.",UserDataDetails,"School Name")
      cls.StreetName = cls.GetAccountEdits("\n>>> Street name you lived while on 3rd Grade :",lambda x:x.isalnum() and len(x) <= 8,">>> Street name too long.",UserDataDetails,"Street Name")
      cls.CousinName = cls.GetAccountEdits("\n>>> Your oldest cousing Middle name :",lambda x:x.isalpha() and len(x) <= 8,">>> Invalid name",UserDataDetails,"Cousin's Name")
      cls.BookOrMovie = cls.GetAccountEdits("\n>>> Whats your favorite Book/Movie :",lambda y:y.isalnum() and len(y) <= 8,">>> Enter a valid Book/Movie name.",UserDataDetails,"Movie/Book")
      cls.ToyName = cls.GetAccountEdits("\n>>> Whats your childhood favorite Toy:",lambda x:x.isalpha() and len(x) <= 8,">>> Enter a valid Toy name.",UserDataDetails,"Toy Name")
      cls.DishMeal = cls.GetAccountEdits("\n>>> Whats your favorite Dish to cook :",lambda x:x.isalpha() and len(x) <= 8,">>> Invalid Dish name",UserDataDetails,"Favorite Dish")
      cls.ToyNickName = cls.GetAccountEdits("\n>>> What's the Name you gave your Toy:",lambda y:y.isalnum() and len(y) <= 8,">>> Enter a valid Toy Nick name given.",UserDataDetails,"Toy Nickname")
      cls.HighSchoolTeacher = cls.GetAccountEdits("\n>>> Favorite High school teacher name :",lambda x:x.isalpha() and len(x) <= 8,">>> Teachers name too long.",UserDataDetails,"High School Teacher")
      cls.HospitalName = cls.GetAccountEdits("\n>>> Hospital name Once admitted to :",lambda x:x.isalpha() and len(x) <= 8,">>> Invalid Hospital name",UserDataDetails,"Hospital Name")
      print(">>> Hold Up ;\n")
      for key,value in UserDataDetails.items():print(f"{key}:{value}")
      cls.SecurityQuestionsContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Security Questions\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.SecurityQuestionsContinue == 1:return cls.SecurityQuestionsEdits(UserDataDetails)
      elif cls.SecurityQuestionContinue == 2:return cls.AccountSettingIntro(UserDataDetails)
      else:return None

   """ Privacy Setting Genesis """
   @classmethod
   def PrivacyEdits(cls,UserDataDetails):
      if int(cls.GetAccountInputs("\n>>>     Privacy Setting     >>>\n\n>>> You can edit the Following ;\n>> 1: Id Number\n>> 2: Location\n>> 3: Cookies\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Please select 1-3")) == 1:cls.GetAccountEdits("\n>>> Enter Id Number :",lambda x: x.isdigit() and len(x) <=10,">>> please Enter a valid Id number",UserDataDetails,"Id No")
      elif int(cls.GetAccountInputs("\n>>>     Privacy Setting     >>>\n\n>>> You can edit the Following ;\n>> 1: Id Number\n>> 2: Location\n>> 3: Cookies\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Please select 1-3")) == 2:cls.GetAccountEdits("\n>>> Enter your Current Location :",lambda x: x.isalpha() and len(x) <=10,">>> please Enter a location",UserDataDetails,"Location")
#      elif == 3:return cls.cls.GetAccountEdits("\n>>> Enter Id Number :",lambda x: x.isdigit() and len(x) <=10,">>> please Enter a valid Id number",UserDataDetails,""
      else:return None
      cls.PrivacyEditsContinue = int(cls.GetAccountInputs("\n>>> Ooops Sorry this section Is Unavailable\n>>> Continue with ;\n>> 1: Edit Privacy\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1 or 2"))
      if cls.PrivacyEditsContinue == 1:return cls.PrivacyEdits(UserDataDetails)
      elif cls.PrivacyEditsContinue == 2:return cls.AccountSettingIntro(UserDataDetails,Array)
      else:return None

   """ Notification Settings Genesis"""
   @classmethod
   def NotificationsEdits(cls,UserDataDetails):
      cls.NotificationsEditsContinue = int(cls.GetAccountInputs("\n>>> Ooops this section is Unavailable\n>>> Continue with ;\n>> 1: Edit Notifications\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.NotificationsEditsContinue == 1:return cls.NotificationsEdits(UserDataDetails)
      elif cls.NotificationsEditsContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def SubscriptionBiling(cls,UserDataDetails):
      pass


   """ Account Deactivation & Deletion Genesis"""
   @classmethod
   def AccountDeletion(cls,UserDataDetails):
      cls.AccountDeletionContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Profile picture\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.AccountDeletionContinue == 1:return cls.AccountDeletion(UserDataDetails)
      elif cls.AccountDeletionContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

class ArrayActivity:
   def __init__(self,Array,UserDataDetails):
      self.Array = Array
      self.UserDataDetails = UserDataDetails


   @staticmethod
   def GetArrayInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(ArrIntroVal := input(Prompt)):
         print(f">>> {ArrIntroVal} is not Allowed.\n{ErrMsg}")
      return ArrIntroVal

   @classmethod
   def ArrayInputsIntro(cls,UserDataDetails,Array):
      print(f"\nHey {UserDataDetails["First Name"].capitalize()} You suck at programming\n>>> Section Is currently Unavailable >>>...")
      """AS USER FOR DATA INPUT"""
      cls.HomeInstance = Home(UserDataDetails,Array)
      cls.ArrayIntro = int(cls.GetArrayInputs(">>> Continue with ;\n>> 1: Numpy Activity\n>> 2: Main Menu\n\n>>> Option :",lambda x:x.isdigit() and x in ['1','2'],">>> Please select 1-2...Try Again"))
      if cls.ArrayIntro == 1:return cls.ArrayInputsIntro(UserDataDetails,Array)
      elif cls.ArrayIntro == 2:return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
      else:return None

class TrialExplore:
   def __init__(self,UserDataDetails,Array):
      self.UserDataDetails = UserDataDetails
      self.Array = Array


   @staticmethod
   def GetTrialExploreInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(TrialExploreVal := input(Prompt)):
         print(f">>> {TrialExploreVal} is not allowed.\n{ErrMsg}")
      return TrialExploreVal

   @classmethod
   def TrialExploreIntro(cls,UserDataDetails,Array):
      cls.HomeInstance = Home(UserDataDetails,Array)
      print("\n>>> Ooops This section is currently Unavailable >>>\n")
      for key,value in UserDataDetails.items():print(f">> {key.capitalize()}:{value}")
      cls.TrialHome = int(cls.GetTrialExploreInputs(">>> Continue with ;\n>> 1: Trial Explore\n>> 2: Main Menu\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2...Try Again"))
      if cls.TrialHome == 1:return cls.TrialExploreIntro(UserDataDetails,Array)
      elif cls.TrialHome == 2:return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
      else:return None

class HelpPage:
   def __init__(self,UserDataDetails,Array):
      self.UserDataDetails = UserDataDetails
      self.Array = Array

   @staticmethod
   def GetHelpInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(HelpVal := input(Prompt)):
         print(f">>> {HelpVal} is Not allowed.\n{ErrMsg}")
      return HelpVal


   @classmethod
   def HelpIntro(cls,UserDataDetails,Array):
      cls.HomeInstance = Home(UserDataDetails,Array)
      print(f"\n>>> Ooops this Area is Under Development\n")
      cls.HelpPageIntro = int(cls.GetHelpInputs(">>> Continue with ;\n>> 1: Help page\n>> 2: Main Menu\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2...Try Again"))
      if cls.HelpPageIntro == 1:return cls.HelpIntro(UserDataDetails,Array)
      elif cls.HelpPageIntro == 2:return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
      else:return None


class Close:pass

if __name__ == '__main__':
   #Home.AccountSetting(UserDataDetails)
   RegistrationAndLogin.UserAccountRegistration(UserDataDetails,Array)
