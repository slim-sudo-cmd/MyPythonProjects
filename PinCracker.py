
import time
class UserPinCheckOut:

   def __init__(self,FourGuess = None,SixGuess = None,EightGuess = None) -> None:
      self.FourGuess = FourGuess
      self.SixGuess = SixGuess
      self.EightGuess = EightGuess

   @classmethod
   def UserFourPinConditions(cls,UserFourPin) -> bool:
      if UserFourPin.isdigit() and len(UserFourPin) == 4:return True
      else:
         print("Please Try Again issue your Pin")
         return False

   @classmethod
   def UserFourPinCrackingCondition(cls,UserFourPinCracking,UserFourPin,FourHomeInstance):
      if UserFourPinCracking == 1:return UserPinCheckOut.PinCracker(cls,UserFourPin)
      elif UserFourPinCracking == 2:return FourHomeInstance.HomeIntro()
      else:
         print("Please Select from 1-2...Try Again\n")
         return False

   @classmethod
   def FourDigitContinueConditions(cls,CrackContinue,FourHomeInstance) -> bool:
      if CrackContinue == 1:return UserPinCheckOut.UserFourPinIntro()
      elif CrackContinue == 2: 
         FourHomeInstance.HomeIntro()
         return True
      else:
         print("Please select from given Option...Try Again")
         return False

   @staticmethod
   def UserFourPinIntro():
      FourHomeInstance = Home()
      print("\n          4-DIGIT PIN          \n")
      while True:
         UserFourPin = input("Lets have Fun with Cracking\n>>Enter any 4-digit Pin as a Test :")
         if UserPinCheckOut.UserFourPinConditions(UserFourPin):break
         else:continue

      while True:
         UserFourPinCracking = int(input("\nProceed With :\n1:Crack Pin\n2:Main Menu\n>>Your Option :"))
         if UserPinCheckOut.UserFourPinCrackingCondition(UserFourPinCracking,UserFourPin,FourHomeInstance):break
         else:continue

      while True:
         """User input to continue cracking or close software"""
         CrackContinue = int(input("\nNow What do you wanna do next :\n1:Crack Another Pin\n2:Main Menu\n>>Input :"))
         if UserPinCheckOut.FourDigitContinueConditions(CrackContinue,FourHomeInstance):break
         else:continue


   def PinCracker(self,UserFourPin) -> True:
      print("It may take a While\nGrab a Coffee while you wait....")
      for x in range(10000):
         self.FourGuess = str(x).zfill(4)
         print(f"Cracking {self.FourGuess}.........../Failed")
         time.sleep(0.0001)

         if self.FourGuess == UserFourPin:
            print(f"Cracking {self.FourGuess}........../Successfull\nYour Pin is :{self.FourGuess}")
            return True

class SixPin:
   def __init__(self,SixPinGuess = None) ->None:
      self.SixPinGuess = SixPinGuess

   @classmethod
   def SixPinConditions(cls,SixPinInput):
      if SixPinInput.isdigit() and len(SixPinInput) == 6:return True
      else:
         print("\nEnter a valid 6-digit pin...Try Again")
         return False

   @classmethod
   def SixPinCrackCondition(cls,SixPinCrack,SixHomeInstance,SixPinInput):
      if SixPinCrack == 1:return SixPin.SixPinCracker(cls,SixPinInput)
      elif SixPinCrack == 2:return SixHomeInstance.HomeIntro()
      else:
         print("Please Enter a Valid input...Try Again")
         return False

   @classmethod
   def SixPinContinue(cls,SixPinCrackContinue,SixHomeInstance):
      if SixPinCrackContinue == 1:return cls.SixPin.SixPinIntro()
      elif SixPinCrackContinue == 2:return SixHomeInstance.HomeIntro()
      else:return False

   @staticmethod
   def SixPinIntro():
      SixHomeInstance = Home()
      print("\n         6-DIGIT PIN         \n")
      while True:
         SixPinInput = input("Enter Your 6-digit Pin:")
         if SixPin.SixPinConditions(SixPinInput):break
         else:continue

      while True:
         SixPinCrack = int(input("Lets have Fun...\n1:Crack Pin\n2:Main Menu\n>>Your Option :"))
         if SixPin.SixPinCrackCondition(SixPinCrack,SixHomeInstance,SixPinInput):break
         else:continue

      while True:
         SixPinCrackContinue = int(input("\n1: Crack Another Pin\n2: Main Menu\n>>Input :"))
         if SixPin.SixPinContinue(SixPinCrackContinue,SixHomeInstance):return
         else:
            print("\nPlease Select 1-2...Try Again")
            continue

   def SixPinCracker(self,SixPinInput):
      for i in range(1000000):
         self.SixPinGuess = str(i).zfill(6)
         print(f"Cracking {self.SixPinGuess}........../Failed")
         time.sleep(0.00000001)

         if self.SixPinGuess == SixPinInput:
            print(f"Cracking {self.SixPinGuess}........../Successful\nYour Pin is :{self.SixPinGuess}\n")
            return True

class EightPin:
   def __init__(self,EightPinGuess = None) -> None:
      self.EightPinGuess = EightPinGuess

   """ 8-Digit Pin Start Quires"""
   @classmethod
   def EightPinConditions(cls,EightPinInput) -> bool:
      if EightPinInput.isdigit() and len(EightPinInput) == 8:return True
      else:
         print("\nPlease Enter a Valid 8-digit pin... Try Again ")
         return False

   @classmethod
   def EightPinCrackingCondition(cls,EightPinCracking,EightPinInput,EightHomeInstance):
      if EightPinCracking == 1:return EightPin.EightPinCracker(cls,EightPinInput)
      elif EightPinCracking == 2:return EightHomeInstance.HomeIntro()
      else:
         print("Please Select from 1-2...Try Again\n")
         return False

   @classmethod
   def EightContinueConditions(cls,EightCrackContinue,EightHomeInstance) -> bool:
      if EightCrackContinue == 1:return EightPin.EightPinIntro()
      elif EightCrackContinue == 2:return EightHomeInstance.HomeIntro()
      else:
         print("\nPlease select from given Option...Try Again")
         return False

   @staticmethod
   def EightPinIntro():
      EightHomeInstance = Home()
      print("\n          8-DIGIT          \n")
      while True:
         EightPinInput = input("Lets have Fun with Cracking\n>>Enter any 8-digit Pin as a test :")
         if EightPin.EightPinConditions(EightPinInput):break
         else:continue

      while True:
         EightPinCracking = int(input("\nProceed With :\n1:Crack Pin\n2:Main Menu\n>>Input : :"))
         if EightPin.EightPinCrackingCondition(EightPinCracking,EightPinInput,EightHomeInstance):break
         else:continue

      while True:
         EightCrackContinue = int(input("\n1: Crack Another Pin\n2: Main Menu\n>>Input :"))
         if EightPin.EightContinueConditions(EightCrackContinue,EightHomeInstance):break
         else:continue

   def EightPinCracker(self,EightPinInput):
      print("\nThis may Take some while....Please Wait")
      for x in range(100000000):
         self.EightPinGuess = str(x).zfill(8)
         print(f"Cracking {self.EightPinGuess}........../Failed")
         time.sleep(0.00000000001)

         if self.EightPinGuess == EightPinInput:
            print(f"Cracking {self.EightPinGuess}........../Successful\nYour pin is :{self.EightPinGuess}")
            return True

class Home:
   def __init__(self) -> None:
      pass








   @classmethod
   def HomeSelection(cls,HomeInput,FourDigitInstance,SixDigitInstance,EightDigitInstance):
      if HomeInput == 1:return FourDigitInstance.UserFourPinIntro()
      elif HomeInput == 2:return SixDigitInstance.SixPinIntro()
      elif HomeInput == 3:return EightDigitInstance.EightPinIntro()
      elif HomeInput == 4:return True
      else:
         print("\nPlease Select from 1-4...Try Again")
         return False

   @staticmethod
   def HomeIntro():
      FourDigitInstance = UserPinCheckOut()
      SixDigitInstance = SixPin()
      EightDigitInstance = EightPin()
      while True :
         HomeInput = int(input("\nDashBoard :\nSelect Target sample Pin digit;\n1:4-digit Pin\n2:6-digit Pin\n3:8-digit Pin\n4:Close Software\n>>Your Option :"))
         if Home.HomeSelection(HomeInput,FourDigitInstance,SixDigitInstance,EightDigitInstance):break
         else:continue

if __name__ == '__main__':
   print("\n       Slim Cyber Course     \nIs just an illustration on how pin Cracking is done ;")
HomeLink = Home()
HomeLink.HomeIntro()
