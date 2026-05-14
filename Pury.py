#from rich.prompt import IntPrompt from rich.console import console
import numpy as np
import re,time
AdminInfo = {}
UserDataDetails = {"First Name":"None","Surname":"None","Mobile +254":"None","Email":"None","Bio":"None","Username":"None","Security Questions":"None"}
Array = np.array([[1,2,3],[4,5,6],[7,8,9]])
StockInventory = {}
class RegistrationAndLogin:
   def __init__(self,UserDataDetails,Array,StockInventory):
      self.UserDataDetails = UserDataDetails
      self.StockInventory = StockInventory
      self.Array = Array
      self.HomeInstance = Home(UserDataDetails,Array,StockInventory)
      self.AdminInfo = AdminInfo

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
   def UserAccountRegistration(cls,UserDataDetails,Array,StockInventory,AdminInfo):
      print("\n_______ Account SignUp ______")
      cls.HomeInstance = Home(UserDataDetails,Array,StockInventory)
      cls.FirstName = cls.UserValidInputs("\n>>> First Name :",lambda x: x.isalpha() and len(x) < 8,">>> Name Should Contain letters and max lenth of 8 character",UserDataDetails,"First Name")
      cls.Surname = cls.UserValidInputs("\n>>> Surname :",lambda y:y.isalpha() and len(y) < 8,">>> Name Should Contain letters and max lenth of 8 character",UserDataDetails,"Surname")
      cls.MobileNumber = cls.UserValidInputs("\n>>> Mobile Number\n>>> +254 :",lambda p: len(p) == 9 and p[0] in ['1','7'],">>> Phone number should start with 1 or 7",UserDataDetails,"Mobile +254")
      cls.Email = cls.UserValidInputs("\n>>> Email :",lambda y: re.search(r"^[a-zA-Z0-9_&#]+@[a-zA-Z]+\.[a-zA-Z_#$]",y),">>> Invalid Email...Try Again",UserDataDetails,"Email")
      cls.Password = cls.UserValidInputs("\n>>> Create Password :",lambda x:re.search(r"^(?=.*[a-z])(?=.*\d)(?=.*[@#$/£¢§∆π√®✓%]).{8,}",x),">>> Create a Strong password",UserDataDetails,"Password")
      cls.DateOfBirth = int(cls.UserValidInputs("\n>>> Date Of Birth :",lambda x:x.isdigit() and int(x) <= 31,">>> Enter a valid Birth date eg 1-31 to yours",UserDataDetails,"Date Of Birth"))
      cls.MonthDay = int(cls.UserValidInputs("\n>>> Month Date:",lambda x:x.isdigit() and int(x) <= 12,">>> Enter a valid Month eg 1-12",UserDataDetails,"Month Date"))
      cls.YearOfBirth = int(cls.UserValidInputs("\n>>> Year of Birth :",lambda y:y.isdigit() and int(y) >= 1940 and int(y) <= 2008,">>> Age Not Valid to sign up",UserDataDetails,"Year Of Birth" ))
      return cls.UserAccountLogin(UserDataDetails,cls.HomeInstance,AdminInfo,StockInventory)

   @classmethod
   def UserAccountLogin(cls,UserDataDetails,HomeInstance,AdminInfo,StockInventory):
      print("\n______  Welcome To Login ______")
      cls.AdminPanelInstance = AdminPanel(AdminInfo,StockInventory)
      cls.LoginEmail = cls.GetUserLoginDetails("\n>>> Enter Your Email/Mobile Number :",lambda x:x in [UserDataDetails["Email"],UserDataDetails["Mobile +254"],'Admin@2026'],">>> Account doesn't Exists")
      if cls.LoginEmail == 'Admin@2026':return cls.AdminPanelInstance.AdminAccountSignUp(UserDataDetails,Array,AdminInfo,StockInventory)
      else:
         cls.LoginPassword = cls.GetUserLoginDetails("\n>>> Enter Your Password:",lambda x:x == UserDataDetails["Password"],">>> Wrong Password...Try Again")
         def TimerLag(start=3,stop=0):
            print("\n>>> Please wait...")
            for x in range(start,stop,-1):print(x);time.sleep(1)
         TimerLag()
         return cls.HomeInstance.HomePageIntro(UserDataDetails,Array,StockInventory)

   @classmethod
   def LogInSystemIn(cls,UserDataDetails,Array,AdminInfo,StockInventory):
      cls.HomeInstance = Home(UserDataDetails,Array,StockInventory)
      print("\n______ Purity's Mart ______\n")
      cls.HelpInstance = HelpPage(UserDataDetails,Array)
      cls.LoginPanel = int(cls.GetUserLoginDetails("\n>>> Get all your house equipmets at affodable price.\n>>> Every Commodity you name it we got it.\n\n>>> Continue with ;\n>> 1: Create Account\n>> 2: Login\n>> 3: Help\n>> 4: Close App\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4],">>> Please select a valid input."))
      if cls.LoginPanel == 1:return cls.UserAccountRegistration(UserDataDetails,Array,AdminInfo,StockInventory)
      elif cls.LoginPanel == 2:return cls.UserAccountLogin(UserDataDetails,cls.HomeInstance,AdminInfo,StockInventory)
      elif cls.LoginPanel == 3:return cls.HelpInstance.HelpIntro(UserDataDetails,Array)
      elif cls.LoginPanel == 4:return
      else:return None

   @classmethod
   def LoginBack(cls,UserDataDetails,AdminInfo,Array):
      print("\n______ Purity's Mart ______\n")
      cls.HelpInstance = HelpPage(UserDataDetails,Array)
      cls.LoginBackIntro = int(cls.GetUserLoginDetails("\n>>> Get all your house equipmets at affodable price.\n>>> Every Commodity you name it we got it.\n\n>>> Continue with ;\n>> 1: Create Account\n>> 2: Login\n>> 3: Help\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))
      if cls.LoginBackIntro == 1:return cls.UserAccountRegistration(UserDataDetails,Array)
      elif cls.LoginBackIntro == 2:return cls.AllLoginBack(UserDataDetails,cls.HomeInstance,AdminInfo)
      elif cls.LoginBackIntro == 3:return cls.HelpInstance.HelpIntro(UserDataDetails,Array)

   @classmethod
   def AllLoginBack(cls,UserDataDetails,Array,AdminInfo,StockInventory):
      cls.AdminPanelInstance = AdminPanel(AdminInfo,StockInventory)
      StockAvailableIn = StockInventory
      cls.HomeInstance = Home(UserDataDetails,Array,StockInventory)
      print("\n______ Welcome To Purity Mart ______\n")
      if (Choice := int(cls.GetUserLoginDetails("\n>>> Continue with ;\n>> 1: Create Account\n>> 2: Logim\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Select a valid Input"))) == 1:return cls.UserAccountRegistration(UserDataDetails,Array,StockInventory,AdminInfo)
      elif Choice == 2:
         cls.LoggedBack = cls.GetUserLoginDetails("\n>>> Enter Your Email/Mobile Number:",lambda x:x in [UserDataDetails["Email"],UserDataDetails["Mobile +254"],AdminInfo["Id No"]],">>> Account Doesn't exist.")
         if cls.LoggedBack == UserDataDetails["Email"] and cls.LoggedBack == UserDataDetails["Mobile +254"]:
            cls.GetUserLoginDetails("\n>>> Enter Password :",lambda x:x == UserDataDetails["Password"],">>> Wrong password")
            print(f"\n>>> Welcome back ,{UserDataDetails["First Name"].capitalize()}")
            return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
         elif cls.LoggedBack == AdminInfo["Id No"]:
            cls.GetUserLoginDetails(">>> Enter Password :",lambda x:x == AdminInfo["Admin Password"],">>> Wrong password")
            print(f">>> Welcome back ,{AdminInfo["Admin Name"].capitalize()}")
            return cls.AdminPanelInstance.StockActionIntro(UserDataDetails,Array,AdminInfo,StockAvailableIn)
         else:return None
      else:return None

class AdminPanel:
   StockInventory = {
                 "Bakery":{
                           "brown bread":{"Price":0,"Available Stock":0},
                           "white bread":{"Price":0,"Available Stock":0},
                           "white scones":{"Price":0,"Available Stock":0},
                           "vanila loaf bread":{"Price":0,"Available Stock":0},
                           "queen cakes":{"Price":0,"Available Stock":0},
                           "mandazi":{"Price":0,"Available Stock":0},
                           "fruit cake":{"Price":0,"Available Stock":0},
                           "bread rusk":{"Price":0,"Available Stock":0},
                           "chocolate muffins":{"Price":0,"Available Stock":0},
                              },
                 "Dairy":{
                           "milk 1 ltr":{"Price":0,"Available Stock":0},
                           "cheese 500g":{"Price":0,"Available Stock":0},
                           "cheese 250g":{"Price":0,"Available Stock":0},
                           "yogurt 1 ltr":{"Price":0,"Available Stock":0},
                           "yogurt 500ml":{"Price":0,"Available Stock":0},
                           "mala 1 ltr":{"Price":0,"Available Stock":0},
                           "butter 500g":{"Price":0,"Available Stock":0},
                           "butter 250g":{"Price":0,"Available Stock":0}
                           },
                 "Cooking Essentials":{
                           "spices":{"Price":0,"Available Stock":0},
                           "cooking oil 1 ltr":{"Price":0,"Available Stock":0},
                           "cooking fat 1kg":{"Price":0,"Available Stock":0},
                           "salt 1kg":{"Price":0,"Available Stock":0},
                           "yeast":{"Price":0,"Available Stock":0},
                           "baking powder":{"Price":0,"Available Stock":0},
                           "tomato paste":{"Price":0,"Available Stock":0}
                           },
                 "Personal Care & Hygiene":{
                           "geisha":{"Price":0,"Available Stock":0},
                           "sanitary pad":{"Price":0,"Available Stock":0},
                           "vaseline 250ml":{"Price":0,"Available Stock":0},
                           "tissue 4pck":{"Price":0,"Available Stock":0},
                           "pepsodent toothpaste":{"Price":0,"Available Stock":0},
                           "dental floss":{"Price":0,"Available Stock":0},
                           "shower gel":{"Price":0,"Available Stock":0}
                           },
                 "Home & Laundry":{
                           "pegs":{"Price":0,"Available Stock":0},
                           "detergent powder 1kg":{"Price":0,"Available Stock":0},
                           "liquid soap 1ltr":{"Price":0,"Available Stock":0},
                           "bar soap 1kg":{"Price":0,"Available Stock":0},                            "Fruit Cake":{"Price":0,"Available Stock":0},
                           "downey":{"Price":0,"Available Stock":0},
                           "bleech 500ml":{"Price":0,"Available Stock":0}
                           },
                 "Dry Pantry & Grains":{
                            "pembe 2kg maize":{"Price":0,"Available Stock":0},
                            "soko 2kg maize":{"Price":0,"Available Stock":0},
                            "ajab 2kg maize":{"Price":0,"Available Stock":0},
                            "amaize 2kg maize":{"Price":0,"Available Stock":0},
                            "raha 2kg maize":{"Price":0,"Available Stock":0},
                            "pisha 2kg maize":{"Price":0,"Available Stock":0},
                            "jogoo 2kg maize":{"Price":0,"Available Stock":0},
                            "pembe 1kg maize":{"Price":0,"Available Stock":0},
                            "soko 1kg maize":{"Price":0,"Available Stock":0},
                            "ajab 1kg maize":{"Price":0,"Available Stock":0},
                            "amaize 1kg maize":{"Price":0,"Available Stock":0},
                            "raha 1kg maize":{"Price":0,"Available Stock":0},
                            "pisha 1kg maize":{"Price":0,"Available Stock":0},
                            "jogoo 1kg maize":{"Price":0,"Available Stock":0},
                            "pembe 2kg wheat":{"Price":0,"Available Stock":0},
                            "soko 2kg wheat":{"Price":0,"Available Stock":0},
                            "ajab 2kg wheat":{"Price":0,"Available Stock":0},
                            "raha 2kg wheat":{"Price":0,"Available Stock":0},
                            "pembe 1kg wheat":{"Price":0,"Available Stock":0},
                            "soko 1kg wheat":{"Price":0,"Available Stock":0},
                            "ajab 1kg wheat":{"Price":0,"Available Stock":0},
                            "raha 1kg wheat":{"Price":0,"Available Stock":0},
                            "soko 2kg uji sour":{"Price":0,"Available Stock":0},
                            "familia 2kg uji sour":{"Price":0,"Available Stock":0},
                            "familia 2kg pure":{"Price":0,"Available Stock":0},
                            "soko 2kg pure uji":{"Price":0,"Available Stock":0},
                            "familia 1kg uji sour":{"Price":0,"Available Stock":0},
                            "familia 1kg uji pure":{"Price":0,"Available Stock":0},
                            "soko 1kg uji sour":{"Price":0,"Available Stock":0},
                            "soko 1kg pure uji":{"Price":0,"Available Stock":0},
                            "sugar 2kg ":{"Price":0,"Available Stock":0},
                            "salt 2kg":{"Price":0,"Available Stock":0},
                            "sugar 1kg":{"Price":0,"Available Stock":0},
                            "salt 1kg":{"Price":0,"Available Stock":0},
                            "salt 1/2kg":{"Price":0,"Available Stock":0},
                            "coffee 1kg":{"Price":0,"Available Stock":0},
                            "pishori 5kg":{"Price":0,"Available Stock":0},
                            "sindano 5kg":{"Price":0,"Available Stock":0},
                            "pishori 2kg":{"Price":0,"Available Stock":0},
                            "pishori 1kg":{"Price":0,"Available Stock":0},
                            "sindano 2kg":{"Price":0,"Available Stock":0},
                            "sindano 1kg":{"Price":0,"Available Stock":0},
                            "basmati 5kg":{"Price":0,"Available Stock":0},
                            "basmati 2kg":{"Price":0,"Available Stock":0},
                            "basmati 1kg":{"Price":0,"Available Stock":0},
                            "mwea 5kg":{"Price":0,"Available Stock":0},
                            "mwea 2kg":{"Price":0,"Available Stock":0},
                            "mwea 1kg":{"Price":0,"Available Stock":0},
                            "coffee 500g":{"Price":0,"Available Stock":0},
                            "coffee 250g":{"Price":0,"Available Stock":0},
                            "coffee 125g":{"Price":0,"Available Stock":0},
                            "ketepa tea 1kg":{"Price":0,"Available Stock":0},
                            "ketepa tea 500g":{"Price":0,"Available Stock":0},
                            "ketepa tea 250g":{"Price":0,"Available Stock":0},
                           }
   }

   def __init__(self,AdminInfo,StockInventory):
      self.AdminInfo = AdminInfo
      self.StockInventory = StockInventory

   @staticmethod
   def GetAdminLoginDetails(Prompt,ConditionFunc,ErrMsg,AdminInfo,key):
      while not ConditionFunc(val := input(Prompt)):
         print(f"{val} is not allowed.\n{ErrMsg}")
      AdminInfo[key] = val
      return val

   @staticmethod
   def GetAdminInputs(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(val := input(Prompt)):
         print(f"{val} is not allowed.\n{ErrMsg}.")
      return val

   @classmethod
   def AdminAccountSignUp(cls,UserDataDetails,Array,AdminInfo,StockInventory):
      print("\n________ Admin Panel ________\n")
      cls.AdminName = cls.GetAdminLoginDetails("\n>>> Admin Name :",lambda x:x.isalpha() and len(x) <= 10,">>> Enter a Valid Admin name.",AdminInfo,"Admin Name")
      cls.AdminNo = cls.GetAdminLoginDetails("\n>>> Mobile No\n>>>+254:",lambda x:x.isdigit() and len(x) == 9 and x[0] in ['1','7'],"Invalid Mobile number",AdminInfo,"Mobile No +254")
      cls.AdminPassword = cls.GetAdminLoginDetails("\n>>> Create Admin Password :",lambda x:re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[&$#@*_-¢€¥π×§∆√]).{8,}",x),">>> Create a strong password",AdminInfo,"Admin Password")
      cls.Id_No = cls.GetAdminLoginDetails("\n>>> Id No :",lambda x:x.isdigit() and len(x) <= 10 and len(x) > 5,"Enter a valid id no",AdminInfo,"Id No")
      def Timer(Start=3,Stop=0):
         for i in range(Start,Stop,-1):print(i);time.sleep(1)
      Timer()
      return cls.AdminLogin(UserDataDetails,Array,AdminInfo,StockInventory)

   @classmethod
   def AdminLogin(cls,UserDataDetails,Array,AdminInfo,StockInventory):
      print("\n______ Admin Login ______\n")
      cls.GetAdminInputs("\n>>> Admin Id:",lambda x: x == AdminInfo["Id No"],">>> Wrong User")
      cls.GetAdminInputs("\n>>> Admin Password :",lambda x:x == AdminInfo["Admin Password"],">>> Wrong Password Try Again")
      def Timer(Start =3,Stop =0):
         for x in range(Start,Stop,-1):print(x);time.sleep(1)
      Timer()
      return cls.StockActionIntro(UserDataDetails,Array,AdminInfo,StockInventory)


   @classmethod
   def StockActionIntro(cls,UserDataDetails,Array,AdminInfo,StockInventory):
      cls.RegistrationInstance = RegistrationAndLogin(UserDataDetails,Array,StockInventory)
      cls.StockAction = int(cls.GetAdminInputs("\n______ Admin Page ______\n\n>> 1: Stocks\n>> 2: Finance\n>> 3: Business Stats\n>> 4: Sign Out\n\n>>> Option :",lambda x: x.isdigit() and int(x) in [1,2,3,4],">>> Select a valid input"))
      if cls.StockAction == 1:return cls.StockPerCategory()
      elif cls.StockAction == 2:return cls.FinanceStatus()
      elif cls.StockAction == 3:return cls.BusinessStats()
      elif cls.StockAction == 4:
         def Timer(Start=3,Stop=0):
            for x in range(Start,Stop,-1):print(x);time.sleep(0.75)
         Timer()
         return cls.RegistrationInstance.AllLoginBack(UserDataDetails,Array,AdminInfo,StockInventory)
      else:return None

   """ Handles Category Creation """
   @classmethod
   def CreateStockCategory(cls):
      pass

   @classmethod
   def StockPerCategory(cls):
      print("\n______ Stock Per Category ______\n\n>>> Select any category you wish ;\n")
      for i, category in enumerate(cls.StockInventory.keys(),1):print(f">> {i:<3}: {category.title():<20}")
      if (choice := int(cls.GetAdminInputs("\n>> 00: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,5,6,00],">>> Select a valid input."))) == 1:return cls.BakeryUpdates()
      elif choice == 2:return cls.DairyUpdates()
      elif choice == 3:return cls.CookingEssentialUpdates()
      elif choice == 4:return cls.PersonalCareUpdates()
      elif choice == 5:return cls.HomeAndLaundryUpdates()
      elif choice == 6:return cls.PantryUpdates()
      elif choice == 00:return cls.StockActionIntro(UserDataDetails,Array,AdminInfo,StockInventory)
      else:return None

   """ Bakery All Appending"""
   @classmethod
   def BakeryUpdateAndQuantity(cls,ItemIn,PriceIn,QuantityIn):
      cls.TargetKey = next((k for k in cls.StockInventory["Bakery"] if k.lower() == ItemIn.strip().lower()),None)
      if cls.TargetKey:
         cls.StockInventory["Bakery"][cls.TargetKey]["Available Stock"] += int(QuantityIn)
         cls.StockInventory["Bakery"][cls.TargetKey]["Price"] = float(PriceIn)
      else:
         print(f"\n>>> Note : {ItemIn} not found in Bakery Category.\n>>> Created new Stock Category.")
         cls.StockInventory["Bakery"][ItemIn] = {"Price":float(PriceIn),"Available Stock":int(QuantityIn)}

   @classmethod
   def AddBakeryStock(cls):
      print("\n______ Adding Bakery Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Bakery"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.BakeryItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Bakery Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.BakeryPrice = float(cls.GetAdminInputs("\n>>> Bakery Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.BakeryQuantity = int(cls.GetAdminInputs("\n>>> Bakery Iten Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.BakeryUpdateAndQuantity(cls.BakeryItem,cls.BakeryPrice,cls.BakeryQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Bakery"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Bakery Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Enter a valid input"))) == 1:return cls.AddBakeryStock()
      elif Choice == 2:return cls.BakeryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Bakery Deletion Category"""
   @classmethod
   def BakeryDeletion(cls,Item):
      cls.TargetKey = next((x for x in cls.StockInventory["Bakery"] if x.lower() == Item.strip().lower()),None)
      if cls.TargetKey:
         del cls.StockInventory["Bakery"][cls.TargetKey]
         print(f">>> {cls.TargetKey.title()} was successfully deleted")
      else:print(f"\n>>> Ooops {Item.capitalize()} was Not Found")

   @classmethod
   def DeleteBakeryStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.BakeryDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Bakery"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Bakery Updates\n>> 3: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2,3],">>> Select a valid Input"))) == 1:return cls.BakeryDelStock()
      elif Choice == 2:return cls.BakeryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def BakeryUpdates(cls):
      print("\n______ Bakery Updates ______\n\n>>> Here are the  available Stock of bakery.\n")
      for i, (item, Details) in enumerate(cls.StockInventory["Bakery"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {Details['Price']:<10} | Stock : {Details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Bakery Category\n>> 2: Delete Bakery Category\n>> 3: Stock In Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid Input."))) == 1:return cls.AddBakeryStock()
      elif Choice == 2:return cls.DeleteBakeryStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Updating Dairy Category """
   @classmethod
   def DairyUpdateAndQuantity(cls,ItemIn,PriceIn,QuantityIn):
      cls.TargetKey = next((x for x in cls.StockInventory["Dairy"] if x.lower == ItemIn.strip().lower()),None)
      if cls.TargetKey:
         cls.StockInventory["Dairy"][cls.TargetKey]['Available Stock'] += int(QuantityIn)
         cls.StockInventory["Dairy"][cls.TargetKey]["Price"] = float(PriceIn)
      else:
         print(f"\n>>> Note : {ItemIn} not found in Dairy Category.\n>>> Created new Dairy Category")
         cls.StockInventory["Dairy"][ItemIn] = {"Price":float(PriceIn),"Available Stock":int(QuantityIn)}

   """ Delete Dairy Stock """
   @classmethod
   def DairyDeletion(cls,Item):
      cls.DelKey = next((k for k in cls.StockInventory["Dairy"] if k.lower() == Item.strip().lower()),None)
      if cls.DelKey:
         del cls.StockInventory["Dairy"][cls.DelKey]
         print(">>> {cls.DelKey.title()} was Succefully Deleted.")
      else:print(f"Ooops {Item} wss Not Found.")

   """ Adding Dairy Stock"""
   @classmethod
   def AddDairyStock(cls):
      print("\n______ Adding Dairy Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Dairy"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.DairyItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Bakery Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.DairyPrice = float(cls.GetAdminInputs("\n>>> Bakery Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.DairyQuantity = int(cls.GetAdminInputs("\n>>> Bakery Iten Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.DairyUpdateAndQuantity(cls.DairyItem,cls.DairyPrice,cls.DairyQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Dairy"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Dairy Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Enter a valid input"))) == 1:return cls.AddDairyStock()
      elif Choice == 2:return cls.DairyUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def DairyDelStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.DairyDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Dairy"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Dairy Updates\n>> 3: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2,3],">>> Select a valid input"))) == 1:return cls.DairyDelStock()
      elif Choice == 2:return cls.DairyUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def DairyUpdates(cls):
      print("\n______ Dairy Updates ______\n\n>>> Here are the available Stock of dairy.\n")
      for i, (item,details) in enumerate(cls.StockInventory["Dairy"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {details['Price']:<10} | Available Stock :{details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Dairy Stock\n>> 2: Delete Dairy category item\n>> 3: Stock Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddDairyStock()
      elif Choice == 2:return cls.DairyDelStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Updating Cooking Essential """
   @classmethod
   def CookingUpdateAndQuantity(cls,Item,Price,Quantity):
      cls.TargetKey = next((i for i in cls.StockInventory["Cooking Essentials"] if i.lower() == Item.strip().lower()),None)
      if cls.TargetKey:
         cls.StockInventory["Cooking Essentials"][cls.TargetKey]['Available Stock'] += int(Quantity)
         cls.StockInventory["Cooking Essentials"][cls.TargetKey]["Price"] = float(Price)
      else:
         print(f">>> Note : {Item} not found in Cooking Category.\n>>> Created new Cooking Essential Category.")
         cls.StockInventory["Cooking Essentials"][Item] = {"Price":float(Price),"Available Stock":int(Quantity)}

   """ Delete Cooking Essentials Stock """
   @classmethod
   def CookingDeletion(cls,Item):
      cls.DelKey = next((k for k in cls.StockInventory["Cooking Essentials"] if k.lower() == Item.strip().lower()),None)
      if cls.DelKey:
         del cls.StockInventory["Cooking Essentials"][cls.DelKey]
         print(">>> {cls.DelKey.title()} was Succefully Deleted.")
      else:print(f"Ooops {Item} wss Not Found.")

   @classmethod
   def CookingDelStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.CookingDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Cooking Essentials"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2],">>> Select a valid input"))) == 1:return cls.CookingDelStock()
      elif Choice == 2:return cls.CookingEssentialUpdate()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def AddCookingStock(cls):
      print("\n______ Adding Cooking Essentials Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Cooking Essentials"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.CookingItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Bakery Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.CookingPrice = float(cls.GetAdminInputs("\n>>> Bakery Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.CookingQuantity = int(cls.GetAdminInputs("\n>>> Bakery Iten Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.CookingUpdateAndQuantity(cls.CookingItem,cls.CookingPrice,cls.CookingQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Cooking Essentials"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Cooking Essentials  Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],"Enter a valid input"))) == 1:return cls.AddCookingStock()
      elif Choice == 2:return cls.CookingEssentialUpdates()
      elif Choice == 3:return cls.StockCategory()
      else:return None

   @classmethod
   def CookingEssentialUpdates(cls):
      print("\n______ Cooking Essentials Updates ______\n\n>>> Here are the available Stock for Cooking Essentials.\n")
      for i, (item,details) in enumerate(cls.StockInventory["Cooking Essentials"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {details['Price']:<10} | Available Stock :{details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Cooking  Stock\n>> 2: Delete Cooking Stock\n>> 3: Stock In Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddCookingStock()
      elif Choice == 2:return cls.CookingDelStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Delete Personal Care & Hygiene Stock """
   @classmethod
   def PersonalDeletion(cls,Item):
      cls.DelKey = next((k for k in cls.StockInventory["Personal Care & Hygiene"] if k.lower() == Item.strip().lower()),None)
      if cls.DelKey:
         del cls.StockInventory["Personal Care & Hygiene"][cls.DelKey]
         print(">>> {cls.DelKey.title()} was Succefully Deleted.")
      else:print(f"Ooops {Item} wss Not Found.")

   @classmethod
   def PersonalDelStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.PersonalDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Personal Care & Hygiene"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Personal Care Update\n>> 3: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2],">>> Select a valid input"))) == 1:return cls.PersonalDelStock()
      elif Choice == 2:return cls.PersonalCareUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def AddPersonalStock(cls):
      print("\n______ Adding Personal Care & Hygiene Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Personal Care & Hygiene"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.PersonalItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Bakery Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.PersonalPrice = float(cls.GetAdminInputs("\n>>> Bakery Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.PersonalQuantity = int(cls.GetAdminInputs("\n>>> Bakery Iten Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.PersonalCareUpdateAndQuantity(cls.PersonalItem,cls.PersonalPrice,cls.PersonalQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Personal Care & Hygiene"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Personal Care Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Enter a valid Input"))) == 1:return cls.AddPersonalStock()
      elif Choice == 2:return cls.PersonalCareUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Personal Care & Hygiene Update"""
   @classmethod
   def PersonalCareUpdateAndQuantity(cls,Item,Price,Quantity):
      if Item in cls.StockInventory["Personal Care & Hygiene"]:
         cls.StockInventory["Personal Care & Hygiene"][Item]['Available Stock'] += int(Quantity)
         cls.StockInventory["Personal Care & Hygiene"][Item]["Price"] = float(Price)
      else:
         print(f">>> Note : {Item} not found in Personal Care Category.\n>>> Created new Personal Care Category.")
         cls.StockInventory["Personal Care & Hygiene"][Item] = {"Price":float(Price),"Available Stock":int(Quantity)}

   @classmethod
   def PersonalCareUpdates(cls):
      print("\n______ Personal Care Hygiene Updates ______\n\n>>> Here are the available Stock of dairy.\n")
      for i, (item,details) in enumerate(cls.StockInventory["Personal Care & Hygiene"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {details['Price']:<10} | Available Stock :{details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Personal Care  Stock\n>> 2: Delete Personal Care Category item\n>> 3: Stock In Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddPersonalStock()
      elif Choice == 2:return cls.PersonalDelStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Delete Home Laundry Stock """
   @classmethod
   def HomeLaundryDeletion(cls,Item):
      cls.DelKey = next((k for k in cls.StockInventory["Home & Laundry"] if k.lower() == Item.strip().lower()),None)
      if cls.DelKey:
         del cls.StockInventory["Home & Laundry"][cls.DelKey]
         print(">>> {cls.DelKey.title()} was Succefully Deleted.")
      else:print(f"Ooops {Item} wss Not Found.")

   @classmethod
   def HomeLaundryDelStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.HomeLaundryDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Home & Laundry"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Home & Laundry Update\n>> 3: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2],">>> Select a valid input"))) == 1:return cls.HomeLaundryDelStock()
      elif Choice == 2:return cls.HomeAndLaundryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Home & Laundry Updates """
   @classmethod
   def HomeLaundryUpdateAndQuantity(cls,Item,Price,Quantity):
      cls.TargetKey = next((k for k in cls.StockInventory["Home & Laundry"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey:
         cls.StockInventory["Home & Laundry"][cls.TargetKey]["Available Stock"] += int(Quantity)
         cls.StockInventory["Home & Laundry"][cls.TargetKey]["Price"] = float(Price)
      else:
         print(f">>> Note : {Item.Upper()} not found in Home & Laundry Category.\n>>> Created new Home & Laundry Category.")
         cls.StockInventory["Home & Laundry"][Item]= {"Price":float(Price),"Available Stock":int(Quantity)}

   @classmethod
   def AddHomeLaundryStock(cls):
      print("\n______ Adding Home Laundry Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Home & Laundry"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.HomeLaundryItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Bakery Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.HomeLaundryPrice = float(cls.GetAdminInputs("\n>>> Bakery Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.HomeLaundryQuantity = int(cls.GetAdminInputs("\n>>> Bakery Iten Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.HomeLaundryUpdateAndQuantity(cls.HomeLaundryItem,cls.HomeLaundryPrice,cls.HomeLaundryQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Home & Laundry"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Home & Laundry Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Enter a valid Input"))) == 1:return cls.AddHomeLaundryStock()
      elif Choice == 2:return cls.HomeAndLaundryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def HomeAndLaundryUpdates(cls):
      print("\n______ Home & Laundry Updates ______\n\n>>> Here are the available Stock of Home & Laundry.\n")
      for i, (item,details) in enumerate(cls.StockInventory["Home & Laundry"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {details['Price']:<10} | Available Stock :{details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Home Laundry Stock\n>> 2: Delete Home Laundry Category Item\n>> 3: Stock In Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddHomeLaundryStock()
      elif Choice == 2:return cls.HomeLaundryDelStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   """ Pantry and Grain Updates """
   @classmethod
   def PantryAndGrainsUpdateAndQuantity(cls,Item,Price,Quantity):
      cls.TargetKey = next((x for x in cls.StockInventory["Dry Pantry & Grains"] if x.lower() == Item.strip().isdigit()),None)
      if cls.TargetKey:
         cls.StockInventory["Dry Pantry & Grains"][cls.TargetKey]["Available Stock"] += int(Quantity)
         cls.StockInventory["Dry Pantry & Grains"][cls.TargetKey]["Price"] = float(Price)
      else:
         print(f">>> Note : {Item} not found in Dry Pantry & Grains Category.\n>>> Created new Dry Pantry & Grains Category.")
         cls.StockInventory["Dry Pantry & Grains"][Item] = {"Price":float(Price),"Available Stock":int(Quantity)}

   """ Delete Pantry Category """
   @classmethod
   def PantryDeletion(cls,Item):
      cls.DelKey = next((x for x in cls.StockInventory["Dry Pantry & Grains"] if x.lower() == Item.strip().lower()),None)
      if cls.DelKey:
         del cls.StockInventory["Dry Pantry & Grains"][cls.DelKey]
         print(">>> {cls.DelKey.title()} was Successfully Deleted.")
      else:print(f">>> {Item} was Not Found.")

   @classmethod
   def PantryDelStock(cls):
      cls.DelStock = (cls.GetAdminInputs("\n______ Delete Category ______\n\n>>> Stock Name :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Stock name")).strip().lower()
      cls.PantryDeletion(cls.DelStock)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Dry Pantry & Grains"].items(),1):print(f">> {i:<3}:{bake.title():<20} | Price @ ksh:{bakeOut["Price"]:<10} | Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Delete Another Category\n>> 2: Dry Pantry Update\n>> 3: Stock Category\n>>> Option :",lambda y: y.isdigit() and int(y) in [1,2,3],">>> Select a valid input"))) == 1:return cls.PantryDelStock()
      elif Choice == 2:return cls.PantryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def AddPantryStock(cls):
      print("\n______ Adding Dry Pantry & Grains Category ______\n")
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Dry Pantry & Grains"].items(),1):print(f">> {i:<3}:{bake.title():<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      cls.PantryItem = (cls.GetAdminInputs("\n>>> Continue with Item Appending ;\n>>> Dry Pantry Item Name :",lambda x:x.replace(' ','').isalnum() and len(x) < 15,">>> Enter a valid Stock name.")).strip().lower()
      cls.PantryPrice = float(cls.GetAdminInputs("\n>>> Dry Pantry Item Price @ Ksh:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid Stock Price."))
      cls.PantryQuantity = int(cls.GetAdminInputs("\n>>> Dry Pantry Item Quantity :",lambda x:x.isdigit(),">>> Enter a valid Stock Quantity"))
      cls.PantryAndGrainsUpdateAndQuantity(cls.PantryItem,cls.PantryPrice,cls.PantryQuantity)
      for i, (bake, bakeOut) in enumerate(cls.StockInventory["Bakery"].items(),1):print(f">> {i:<3}:{bake:<20}| Price @ Ksh:{bakeOut["Price"]:<10}| Available Stock :{bakeOut["Available Stock"]:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Another Item\n>> 2: Dry Pantry Updates\n>> 3: Stock Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddPantryStock()
      elif Choice == 2:return cls.PantryUpdates()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def PantryUpdates(cls):
      print("\n______ Pantry Updates ______\n\n>>> Here are the available Stock of Pantry.\n")
      for i, (item,details) in enumerate(cls.StockInventory["Dry Pantry & Grains"].items(),1):print(f">> {i:<3} : {item.title():<20} | Price :Ksh {details['Price']:<10} | Available Stock :{details['Available Stock']:<10}")
      if (Choice := int(cls.GetAdminInputs("\n>>> Continue with ;\n>> 1: Add Dry Pantry & Grain  Stock\n>> 2: Delete  Pantry Category\n>> 3: Stock In Menu\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3],">>> Select a valid input"))) == 1:return cls.AddPantryStock()
      elif Choice == 2:return cls.PantryDelStock()
      elif Choice == 3:return cls.StockPerCategory()
      else:return None

   @classmethod
   def StockItemsIn(cls):
      return cls.StockInventory



   @classmethod
   def BusinessStats(cls):pass


class Home:
   def __init__(self,UserDataDetails,Array,StockInventory):
      self.UserDataDetails = UserDataDetails
      self.Array = Array
      self.StockInventory = StockInventory
      self.ShoppingCart = {}

   @staticmethod
   def GetHomeDetails(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(HomeDetVal := input(Prompt)):
         print(f">>> {HomeDetVal} is Not allowed.\n{ErrMsg}")
      return HomeDetVal

   @classmethod
   def HomePageIntro(cls,UserDataDetails,Array,StockInventory):
      cls.HelpPageInstance = HelpPage(UserDataDetails,Array)
      cls.StockSaleInstance = StockSale()
      cls.LoginInstance = RegistrationAndLogin(UserDataDetails,Array,StockInventory)
      cls.AccountSettingInstance = AccountSettings(UserDataDetails,Array)
      print(f"\n________ Home Page ________\n\n>>> Welcome {UserDataDetails["First Name"].capitalize()}.")
      if (HomeIn := int(cls.GetHomeDetails("\n>>> Continue with ;\n>> 1: Shop with Us\n>> 2: Account Setting\n>> 3: Chart\n>> 4: Help Page\n>> 5: Log Out\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,5],">>> Please Enter a valid Input"))) == 1:return cls.ShopIntro(UserDataDetails,StockInventory)
      elif HomeIn == 2:return cls.AccountSettingInstance.AccountSettingIntro(UserDataDetails,Array)
      elif HomeIn == 3:return cls.StockSaleInstance.ChartItemsIntro()
      elif HomeIn == 4:return cls.HelpPageInstance.HelpIntro(UserDataDetails,Array)
      elif HomeIn == 5:return cls.LoginInstance.AllLoginBack(UserDataDetails,Array,AdminInfo,StockInventory)
      else :return None

   @classmethod
   def ShopIntro(cls,UserDataDetails,StockInventory):
      cls.AdminInstance = AdminPanel(AdminInfo,StockInventory)
      cls.StockLocal = cls.AdminInstance.StockItemsIn()
      cls.StockSellInstance = StockSale()
      print("\n______ Shop Page ______\n\n>>> Item Are displayed in Category.")
      for x, Shop in enumerate(cls.StockLocal.keys(),1):print(f">> {x:<2} : {Shop:<10}")
      if (ShopChoice := int(cls.GetHomeDetails("\n>> 0 : Chart\n>>> Select Any Category\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2,3,4,5,6,0],">>> Select a valid Input"))) == 1:return cls.StockSellInstance.BakerySaleIntro()
      elif ShopChoice == 2:return cls.StockSellInstance.DairySaleIntro()
      elif ShopChoice == 3:return cls.StockSellInstance.CookingSaleIntro()
      elif ShopChoice == 4:return cls.StockSellInstance.PersonalCareSaleIntro()
      elif ShopChoice == 5:return cls.StockSellInstance.HomeAndLaundrySaleIntro()
      elif ShopChoice == 6:return cls.StockSellInstance.DryPantrySaleIntro()
      elif ShopChoice == 0:return cls.StockSellInstance.ChartItemsIntro()
      else:return None

class StockSale:
   Shopping_Chart = {}
   StockHome = Home(UserDataDetails,Array,StockInventory)
   AdminInstance = AdminPanel(AdminInfo,StockInventory)
   Stock_For_Sale = AdminInstance.StockItemsIn()

   def __init__(self):pass

   """ Handles All Stock Quantity"""
   @staticmethod
   def GetSaleInput(Prompt,ConditionFunc,ErrMsg):
      while not ConditionFunc(Val := input(Prompt)):
         print(f">>> {Val} is not Allowed.\n{ErrMsg}")
      return Val

   """Handles Bakery Sales"""
   @classmethod
   def BakerySales(cls,Item,Quantity):
      cls.picked_Val = 0
      cls.TargetKey = next((b for b in cls.Stock_For_Sale["Bakery"] if b.lower() == Item.strip().lower()),None)
      if cls.TargetKey:
         cls.unit_sale = cls.Stock_For_Sale["Bakery"][cls.TargetKey]["Price"]
         cls.Total_Amount = cls.unit_sale * int(Quantity)
         if "Bakery" not in cls.Shopping_Chart: cls.Shopping_Chart["Bakery"] = {}
         cls.product_Name = cls.TargetKey.lower()
         if cls.product_Name in cls.Shopping_Chart["Bakery"]:
            cls.Shopping_Chart["Bakery"][cls.product_Name]["Picked"] = cls.picked_Val
            cls.Shopping_Chart["Bakery"][cls.product_Name]["Picked"] += int(Quantity)
            cls.Shopping_Chart["Bakery"][cls.product_Name]["Total"] = cls.Total_Amount
         else:
            cls.Shopping_Chart["Bakery"][cls.product_Name] = {"Picked":int(Quantity),"Total":cls.Total_Amount}

      cls.Stock_For_Sale["Bakery"][cls.TargetKey]["Available Stock"] -= int(Quantity)
      return True

   @classmethod
   def BakerySaleIntro(cls):
      print("\n__________ Bakery Sales __________\n")
      for x,(cls.Bake,cls.BakeSell) in enumerate(cls.Stock_For_Sale["Bakery"].items(),1):print(f">>> {x:<2} :{cls.Bake.title():<20} | Price @Ksh :{cls.BakeSell["Price"]:<10}")
      cls.BakerySellItem = cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum(),">>> Enter a valid product name")
      cls.BakerySellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity"))
      if (Choice := int(cls.GetSaleInput("\n>>> Continue with;\n>> 0: Chart\n>> 1: Edit Bought Goods\n>> 2: Add Bakery Produco1ts\n>> 3: Proceed To Other Products\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Select a valid Input"))) == 1:return cls.BakerySaleIntro()
      elif Choice == 0:
         cls.BakerySales(cls.BakerySellItem,cls.BakerySellQuantity)
         return cls.ChartItemsIntro()
      elif Choice == 2:
         cls.BakerySales(cls.BakerySellItem,cls.BakerySellQuantity)
         return cls.BakerySaleIntro()
      elif Choice == 3:
         cls.BakerySales(cls.BakerySellItem,cls.BakerySellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None

   """ Dairy Sale """
   @classmethod
   def DairySales(cls,Item,Quantity):
      cls.TargetKey = next((k for k in cls.Stock_For_Sale["Dairy"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey and cls.Stock_For_Sale["Dairy"][cls.TargetKey]["Available Stock"] > 0:
         cls.Stock_For_Sale["Dairy"][cls.TargetKey]["Available Stock"] -= int(Quantity)
         cls.TotalDairyPrice = cls.Stock_For_Sale["Dairy"][cls.TargetKey]["Price"] * int(Quantity)
         cls.Shopping_Chart["Dairy Items"] = cls.TotalDairyPrice
         print(f"\n>>> Sold :{Quantity} {cls.TargetKey.title()} @ Ksh :{cls.Stock_For_Sale["Dairy"][cls.TargetKey]["Price"]} & remaining Item:{cls.Stock_For_Sale["Dairy"][cls.TargetKey]["Available Stock"]}")
         return cls.Shopping_Chart
      else:
         print(f">>> Ooops !! {Item.title()} Is Unavailable/Out Of Stock!!.")
         return False

   @classmethod
   def DairySaleIntro(cls):
      print("\n__________ Dairy Sale __________\n")
      for x, (dairyIn,DairyInPrice) in enumerate(cls.Stock_For_Sale["Dairy"].items(),1):print(f">> {x:<2}: {dairyIn.title():<20} | Price @ Ksh :{DairyInPrice["Price"]:<10}")
      cls.DairySellItem = (cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Product Name")).strip().lower()
      cls.DairySellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity Value"))
      if (SellChoice := int(cls.GetSaleInput("\n>>> Continue With;\n>> 0: Chart\n>> 1 : Edit Bought Product\n>> 2: Add Dairy Products\n>> 3: Proceed To Other Products\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Enter a valid Input"))):return cls.DairySaleIntro()
      elif SellChoice == 0:
         cls.DairySales(cls.DairySellItem,cls.DairySellQuantity)
         return cls.ChartItemsIntro()
      elif SellChoice == 2:
         cls.DairySales(cls.DairySellItem,cls.DairySellQuantity)
         return cls.DairySaleIntro()
      elif cls.SellChoice == 3:
         cls.DairySales(cls.DairySellItem,cls.DairySellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None

   """ Cooking Essentials  Sale """
   @classmethod
   def CookingSales(cls,Item,Quantity):
      cls.TargetKey = next((k for k in cls.Stock_For_Sale["Cooking Essentials"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey and cls.Stock_For_Sale["Cooking Essentials"]["Available Stock"] > 0:
         cls.Stock_For_Sale["Cooking Essentials"][cls.TargetKey]["Available Stock"] -= int(Quantity)
         cls.TotalDairyPrice = cls.Stock_For_Sale["Cooking Essentials"][cls.TargetKey]["Price"] * int(Quantity)
         cls.Shopping_Chart["Cooking Essentials Items"] = cls.TotalDairyPrice
         print(f">>> Sold :{Quantity} {cls.TargetKey.title()} @ Ksh :{cls.Stock_For_Sale["Cooking Essentials"][cls.TargetKkey]["Price"]}")
         return cls.Shopping_Chart
      else:
         print(f">>> Ooops !! {Item.title()} Is Unavailabld/Out Of Stock!!.")
         return False

   @classmethod
   def CookingSaleIntro(cls):
      print("\n__________ Cooking Essentials  Sale __________\n")
      for x, (cls.CookingIn,cls.CookingInPrice) in enumerate(cls.Stock_For_Sale["Cooking Essentials"].items(),1):print(f">> {x:<2}: {cls.CookingIn.title():<20} | Price @ Ksh :{cls.CookingInPrice["Price"]:<10}")
      cls.CookingSellItem = (cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Product Name")).strip().lower()
      cls.CookingSellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity Value"))
      if (SellChoice := int(cls.GetSaleInput("\n>>> Continue With;\n>> 0: Chart\n>> 1 : Edit Bought Product\n>> 2: Add Cooking Product\n>> 3: Proceed To Other Products\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Enter a valid input !!"))) == 1:return cls.CookingSaleIntro()
      elif SellChoice == 0:
         cls.CookingSales(cls.CookingSellItem,cls.CookingSellQuantity)
         return cls.ChartItemsIntro()
      elif SellChoice == 2:
         cls.CookingSales(cls.CookingSellItem,cls.CookingSellQuantity)
         return cls.CookingSaleIntro()
      elif SellChoice == 3:
         cls.CookingSales(cls.CookingSellItem,cls.CookingSellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None

   """ Personal Care & Hygiene Sale """
   @classmethod
   def PersonalCareSales(cls,Item,Quantity):
      cls.TargetKey = next((k for k in cls.Stock_For_Sale["Personal Care & Hygiene"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey and cls.Stock_For_Sale["Personal Care & Hygiene"][cls.TargetKey]["Available Stock"] > 0:
         cls.Stock_For_Sale["Personal Care & Hygiene"][cls.TargetKey]["Available Stock"] -= int(Quantity)
         cls.TotalDairyPrice = cls.Stock_For_Sale["Personal Care & Hygiene"][cls.TargetKey]["Price"] * int(Quantity)
         cls.Shopping_Chart["Personal Care & Hygiene Items"] = cls.TotalDairyPrice
         print(f">>> Sold :{Quantity} {cls.TargetKey} @ Ksh:{cls.Stock_For_Sale["Personal Care & Hygiene"][cls.TargetKey]["Price"]}")
         return cls.Shopping_Chart
      else:
         print(f">>> Ooops !! {Item.title()} Is Unavailable/Out Of Stock.")
         return False

   @classmethod
   def PersonalCareSaleIntro(cls):
      print("\n__________ Personal Care & Hygiene Sale __________\n")
      for x, (cls.PersonalCareIn,cls.PersonalCareInPrice) in enumerate(cls.Stock_For_Sale["Personal Care & Hygiene"].items(),1):print(f">> {x:<2}: {cls.PersonalCareIn.title():<20} | Price @ Ksh :{cls.PersonalCareInPrice["Price"]:<10}")
      cls.PersonalCareSellItem = (cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Product Name")).strip().lower()
      cls.PersonalCareSellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity Value"))
      if (SellChoice := int(cls.GetSaleInput("\n>>> Continue With;\n>> 0: Chart\n>> 1 : Edit Bought Product\n>> 2: Add Personal Care Products\n>> 3: Proceed To Other Products\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Enter a valid input"))) == 1:return cls.PersonalCareSaleIntro()
      elif SellChoice == 0:
         cls.PersonalCareSales(cls.PersonalCareSellItem,cls.PersonalCareSellQuantity)
         return cls.ChartItemsIntro()
      elif SellChoice == 2:
         cls.PersonalCareSales(cls.PersonalCareSellItem,cls.PersonalCareSellQuantity)
         return cls.PersonalCareSaleIntro()
      elif SellChoice == 3:
         cls.PersonalCareSales(cls.PersonalCareSellItem,cls.PersonalCareSellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None

   """ Home and Laundry  Sale """
   @classmethod
   def HomeAndLaundrySales(cls,Item,Quantity):
      cls.TargetKey = next((k for k in cls.Stock_For_Sale["Home & Laundry"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey and cls.Stock_For_Sale["Home & Laundry"][cls.TargetKey]["Available Stock"] > 0:
         cls.Stock_For_Sale["Home & Laundry"][cls.TargetKey]["Available Stock"] -= int(Quantity)
         cls.TotalDairyPrice = cls.Stock_For_Sale["Home & Laundry"][cls.TargetKey]["Price"] * int(Quantity)
         cls.Shopping_Chart["Home & Laundry Items"] = cls.TotalDairyPrice
         print(f">>> Sold :{Quantity} {cls.TargetKey} @ Ksh: {cls.Stock_For_Sale["Home & Laundry"][cls.TargetKey]["Price"]}")
         return cls.Shopping_Chart
      else:
         print(f">>> Ooops !! {Item.title()} Is Unavailable/Out Of Stock.")
         return False

   @classmethod
   def HomeAndLaundrySaleIntro(cls):
      print("\n__________ Home & Laundry Sale  __________\n")
      for x, (cls.HomeAndLaundryIn,cls.HomeAndLaundryInPrice) in enumerate(cls.Stock_For_Sale["Home & Laundry"].items(),1):print(f">> {x:<2}: {cls.HomeAndLaundryIn.title():<20} | Price @ Ksh :{cls.HomeAndLaundryInPrice["Price"]:<10}")
      cls.HomeAndLaundrySellItem = (cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Product Name")).strip().lower()
      cls.HomeAndLaundrySellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity Value"))
      if (SellChoice := int(cls.GetSaleInput("\n>>> Continue With;\n>> 0: Chart\n>> 1 : Edit Bought Product\n>> 2: Add Home & Laundry Products\n>> 3: Proceed To Other Products\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Enter a valid input"))) == 1:return cls.HomeAndLaundrySaleIntro()
      elif SellChoice == 0:
         cls.HomeAndLaundrySales(cls.HomeAndLaundrySellItem,cls.HomeAndLaundrySellQuantity)
         return cls.ChartItemsIntro()
      elif SellChoice == 2:
         cls.HomeAndLaundrySales(cls.HomeAndLaundrySellItem,cls.HomeAndLaundrySellQuantity)
         return cls.HomeAndLaundrySaleIntro()
      elif SellChoice == 3:
         cls.HomeAndLaundrySales(cls.HomeAndLaundrySellItem,cls.HomeAndLaundrySellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None

   """ Dry Pantry & Grains Sale """
   @classmethod
   def DryPantrySales(cls,Item,Quantity):
      cls.TargetKey = next((k for k in cls.Stock_For_Sale["Dry Pantry & Grains"] if k.lower() == Item.strip().lower()),None)
      if cls.TargetKey and cls.Stock_For_Sale["Dry Pantry & Grains"][cls.TargetKey]["Available Stock"] > 0:
         cls.Stock_For_Sale["Dry Pantry & Grains"][cls.TargetKey]["Available Stock"] -= int(Quantity)
         cls.TotalDairyPrice = cls.Stock_For_Sale["Dry Pantry & Grains"][cls.TargetKey]["Price"] * int(Quantity)
         cls.Shopping_Chart["Dry Pantry & Grains Items"] = cls.TotalDairyPrice
         print(f">>> Sold :{Quantity} {cls.TargetKey} @ Ksh:{cls.Stock_For_Sale["Dry Pantry & Grains"][cls.TargetKey]["Price"]}")
         return cls.Shopping_Chart
      else:
         print(f">>> Ooops !! {Item.title()} Is Unavailable/Out Of Stock.")
         return False

   @classmethod
   def DryPantrySaleIntro(cls):
      print("\n__________ Dry Pantry & Grains Sale __________\n")
      for x, (cls.DryPantryIn,cls.DryPantryInPrice) in enumerate(cls.Stock_For_Sale["Dry Pantry & Grains"].items(),1):print(f">> {x:<2}: {cls.DryPantryIn.title():<20} | Price @ Ksh :{cls.DryPantryInPrice["Price"]:<10}")
      cls.DryPantrySellItem = (cls.GetSaleInput("\n>>> Product :",lambda x:x.replace(' ','').isalnum() and len(x) <= 15,">>> Enter a valid Product Name")).strip().lower()
      cls.DryPantrySellQuantity = int(cls.GetSaleInput("\n>>> Quantity :",lambda x:x.isdigit(),">>> Enter a valid Quantity Value"))
      if (SellChoice := int(cls.GetSaleInput("\n>>> Continue With;\n>> 0: Chart\n>> 1 : Edit Bought Product\n>> 2: Add Dry Pantry & Grains\n>> 3: Proceed To Other Products\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [0,1,2,3],">>> Enter a valid input"))) == 1:return cls.DryPantrySaleIntro()
      elif SellChoice == 0:
         cls.DryPantrySales(cls.DryPantrySellItem,cls.DryPantrySellQuantity)
         return cls.ChartItemsIntro()
      elif SellChoice == 2:
         cls.DryPantrySales(cls.DryPantrySellItem,cls.DryPantrySellQuantity)
         return cls.DryPantrySaleIntro()
      elif SellChoice == 3:
         cls.DryPantrySales(cls.DryPantrySellItem,cls.DryPantrySellQuantity)
         return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
      else:return None


   """Chart Settings And Handling"""
   @classmethod
   def ChartItemsIntro(cls):
      print("\n__________ Shopping Cart __________\n")
      cls.ChartTotal = sum(cls.item["Total"] for item in cls.Shopping_Chart.values() if "Total" in item)
      cls.PaymentInstance = Payments()
      if not cls.Shopping_Chart:
         print("\n>>> No Items Available on Chart")
         def timer(Start = 3,Stop = 0):
            for x in range(Start,Stop,-1):print(x);time.sleep(1)
         return cls.StockHome.HomePageIntro(UserDataDetails,StockInventory)
      else:
         print("\n__________ Shopping Chart ___________\n")
         for x, (cls.ChartKeys,cls.ChartVal) in enumerate(cls.Shopping_Chart.items(),1):print(f">> {x:<2} :{cls.ChartKeys.title():<20} | Quantity :{cls.Shopping_Chart["Picked"]:<10} | Total Ksh:{cls.ChartVal["Total"]:<10}")
         print(f"\n>>> Total Payout >>> @ Ksh:{cls.ChartTotal:.2f}\n")
         if (ChartChoice := int(cls.GetSaleInput(">>> Proceed;\n>> 1: Place Order\n>> 2: Expand Chart\n>> 0: Home\n>>> Option:",lambda x:x.isdigit() and int(x) in [1,2,0],">>> Enter a valid Input"))) == 1:return cls.PaymentInstance.PaymentIntro()
         elif ChartChoice == 2:return cls.Chart_Expand()
         elif ChartChoice == 0:return cls.StockHome.ShopIntro(UserDataDetails,StockInventory)
         else:return None

   @classmethod
   def Chart_Expand(cls):
      cls.BillOverdue = sum(cls.Shopping_Chart.values())
      return cls.BillOverdue

   @classmethod
   def ChartEdits(cls):pass



#class Payments:
 #  class Mpesa(Payments):

  #    @staticmethod
   #   def mpesa_Inputs_Continue(prompt,conditionFunc,errMsg):
    #     while not conditionFunc(val := input(prompt)):
     #       print(f"\n{errMsg}")
      #   return val

      #@classmethod
     # def mpesa_Intro(cls):
       #  print("\n___________ Mpesa __________\n")
      #   int(cls.mpesa_Inputs_Continue("\n>>> Enter your M-pesa No;\nNo +254 :",lambda x:x.isdigit() and len(x) == 9 and x[0] in [1,7],">>> Check your Phone Number !!"))
         #for x in range(1,4):
            #int(cls.mpesa_Inputs_Continue("\n>>> Enter your M-pesa Pin :",lambda x:x == UserDataDetails["Pin"],">>> Wrong Pin !!"))
       #  return cls.mpesa_Menu()

      #@classmethod
      #def mpesa_Menu(cls):
        # print("\n__________ Mpesa Menu __________\n")
         #if (mpesa_menu_Opt = int(cls.mpesa_Inputs_Continue("\n>>> Continue with;\n>> 1:Proceed to Pay\n>> 2:Check My Pury Points\n>> 3:Redeem Pury Points\n>> 0:Go Back\n>>> Que Option :",lambda y:y.isdigit() and int(y) in [1,2,3,0],">>> Enter a valid Input !!"))) == 1:return cls.mpesa_payment()
        # elif mpesa_menu_Opt == 2:return cls.pury_points_Check()
         #elif mpesa _menu_Opt == 3:return cls.pury_points_Redeem()
         #elif mpesa_menu_Opt == 0:return cls.home()
         #else:return None



      #@classmethod
      #def mpesa_transaction(cls,balance,):

#      @classmethod
#      def mpesa_payment(cls):
 #        print("\n__________ Mpesa Payment __________\n")


  #    @classmethod
   #   def pury_points_Check(cls):pass
    #  @classmethod
     # def pury_points_Redeem(cls):pass




#   class Airtel(Payments):pass
 #  class Crypto_Options(Payments):pass








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
      cls.NewUserBioContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit bio\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
      if cls.NewUserBioContinue == 1:return cls.UserBioEdits(UserDataDetails)
      elif cls.NewUserBioContinue == 2:return cls.ProfileEdits(UserDataDetails)
      else:return None

   @classmethod
   def UserProfilePicEdit(cls,UserDataDetails):
      print("\n>>> Oooops This section under Development >>>\n")
      cls.UserProfilePicContinue = int(cls.GetAccountInputs(">>> Continue with ;\n>> 1: Edit Profile picture\n>> 2: Go Back\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2"))
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

   """ Privacy Setting """
   @classmethod
   def PrivacyEdits(cls,UserDataDetails):
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

   class account_Deactivation_And_Retrival(AccountSettings):
      """ Account Deactivation & Deletion Genesis"""
      @staticmethod
      def account_delete_Man_Inputs(prompt,conditionFunc,errMsg):
         while not conditionFunc(val := input(prompt)):
            print(f">>> {val} is Not Allowed !!\n{errMsg}")
         return val

      @classmethod
      def account_delete_Man_Intro(cls):
         print("\n___________ ACCOUNT DELETE & DEACTIVATION __________\n")
         if (account_Man := int(cls.account_delete_Man_Intro("\n>>> Continue with ;\n>> 1: Deactivate Account\n>> 2: Delete Account\n>> 3: Retrieve Account\n>> 0: Go Back\n\n>>> Que Option :",lambda y:y.isdigit() and int(y) in [1,2,3,0],">>> Enter a valid Input !!"))) == 1:return 
   class account_Retrival(AccountSettings):
      @staticmethod
      def code_Generator():
         code_ref = "GPA420"
         code_gen = list("" + string.digits + string.Ascii_letters + string.panctuation)
         code_gen_In = code_gen.copy()
         random.shuffle(code_gen_In)
         for x in range(code_ref):
            index = code_gen(x)
            code_Out += code_gen_In[index]

      @staticmethod
      def account_retrival_Inputs(prompt,conditionFunc,errMsg):
         while not conditionFunc(val := input(prompt)):
            print(f">>> {val} is Not Allowed !!\n{errMsg}")
         return val

      @classmethod
      def account_retrival_Intro(cls):
         print("\n___________ ACCOUNT RETRIVAL __________\n")
         if (account_Select := int(cls.account_del_Inputs("\n>>> Retrieve with ;\n>> 1: E-mail\n>> 2: Phone Number\n>> 0: Go Back\n\n>>> Que Option :",lambda x:x.isdigit() and int(x) in [1,2,0],">>> Enter a valid Input !!"))) == 1:return cls.retrive_Email()
         elif account_Select == 2:return cls.retrive_Phone()
         elif account_Select == 0:return cls.account_Setting_Home()
         else:return None

      @classmethod
      def retrive_Email(cls):
         print("\n__________ VIA EMAil __________\n")
         cls.account_retrival_Inputs("\n>>> Enter Your E-mail :",lambda x:x == UserDataDetails["Email"],">>> E-mail Not Registered !!")
         
      @classmethod
      def retrive_Phone(cls):
         print("\n___________ VIA PHONE NO ___________\n")
         cls.via_Phone = int(cls.account_retrival_Intro("\n>>> Enter your Phone No \n>> +254 :",lambda u:u == UserDataDetails["Phone Number +254"],">>> Check your Phone Number !!"))
         if not cls.via_Phone:
            if (via_Phone_Select := int(cls.account_retrival_Intro("\n>>> Continue with ;\n>> 1.Try Another way\n>> 2: Help\n>> 0: Go Back\n\n>>> Que Option :",lambda y:y.isdigit() and int(y) in [1,2,0],">>> Enter a valid Input !!"))):return cls.another_Way()
            elif via_Phone_Select == 2:return None
            elif via_Phone_Select == 0:return cls.home_Page()
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
      print("\n>>> Ooops this Area is Under Development\n")
      cls.HelpPageIntro = int(cls.GetHelpInputs(">>> Continue with ;\n>> 1: Help page\n>> 2: Main Menu\n\n>>> Option :",lambda x:x.isdigit() and int(x) in [1,2],">>> Please select 1-2...Try Again"))
      if cls.HelpPageIntro == 1:return cls.HelpIntro(UserDataDetails,Array)
      elif cls.HelpPageIntro == 2:return cls.HomeInstance.HomePageIntro(UserDataDetails,Array)
      else:return None


class Close:pass

if __name__ == '__main__':
   RegistrationAndLogin.LogInSystemIn(UserDataDetails,Array,AdminInfo,StockInventory)
