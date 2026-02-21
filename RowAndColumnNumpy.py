

import numpy as np



class RowEvents:
   def __init__(self,RowValue = None) -> None :
      self.RowValue = RowValue

   def RowSelectoConditions(RowSelecto,Array,HomeRowInstance):
      if self.RowSelecto == 1: return cls.RowOne(Array,HomeRowInstance)
      elif Self.RowSelecto == 2:return cls.RowTwo(Array,HomeRowInstance)
      elif self.RowSelecto == 3:return cls.RowThree(Array,HomeRowInstance)
      elif self.RowSelecto == 4:return True
      elif self.RowSelecto == 5:return HomeRowInstance.HomeIntro()
      else:return False

   @staticmethod
   def RowRangeSelection(Array,HomeRowInstance):
      for x in Array:print(x)
      while True:
         RowSelecto = input("\n>>Welcome To Row range\n>>Single Row Selection\n1:Row 1\n2:Row 2\n3:Row 3\n4:Combo Selection\n5:Main Menu\n>>>Your Input :")
         if RowSelecto.isdigit():
            RowSelectoVal = int(RowSelecto)
            if RowEvents.RowSelectoCoditions(RowSelectoVal,Array,HomeRowInstance):break
         else:
            print(">>>Please Enter a valid input...Try Again")

   @classmethod
   def RowInputConditions(cls,RowInput,Array,HomeRowInstance) -> bool:
      if RowInput == 1 :return cls.RowRangeSelection(Array,HomeRowInstance)
      elif RowInput == 2:return  cls.RowValueSelection(Array,HomeRowInstance)
      elif RowInput == 3:return True
      else:return False

   @staticmethod
   def RowSelection():
      HomeRowInstance = Home()
      print("\n>>>      ROW SECTION      <<<\n")
      Array = np.array([[1,5,9],
                        [3,2,6],
                        [8,5,3]])

      while True:
         for x in Array:print(x)
         RowInput = input("\n>>>Row Directory;\n1:Row Selection & Range\n2:Value on Row\n3:Go Back\n>>Your input :")
         if RowInput.isdigit():
            RowInputVal = int(RowInput)
            if RowEvents.RowInputConditions(RowInputVal,Array,HomeRowInstance):break
         else:
            print(">>>Select a valid input...Try Again")
            continue

   @staticmethod
   def RowOneSelection(Array,HomeInstance):pass









class ColumnEvents:
   def __init__(self) -> None:
      self.HomeInstance = Home()

   @classmethod
   def ColumnInputCondition(cls,ColumnInput,HomeInstance,Array) -> bool:
      Instance = cls()
      if ColumnInput == 1 :
         Instance.ColumnPickingIntro(HomeInstance,Array)
         return True
      elif ColumnInput == 2:return None
      elif ColumnInput == 3:return True
      else:return False
   @staticmethod
   def ColumnSelection(HomeInstance):
      print("\n      COLUMN SECTION      \n")
      Array = np.array([[1,5,9],
                       [3 ,2,6],
                       [8,5,3]])
      while True:
         for x in Array:print(x)
         ColumnInput = input("\n>>>COLUMN Directory;\n1:Column Selecting\n2:Column Value Selecting\n3:Main Menu\n>>Your Input :")
         if ColumnInput.isdigit():
            ColumnVal = int(ColumnInput)
            if ColumnEvents.ColumnInputCondition(ColumnVal,HomeInstance,Array):break
         else:
            print(">>>Please Select a valid input...Try Again")
            continue

   @classmethod
   def ColumnPickingConditions(cls,ColumnPicking,HomeInstance,Array):
      if ColumnPicking == 1:
         cls.ColumnOne(Array,HomeInstance)
         return True
      elif ColumnPicking == 2:
         cls.ColumnTwo(Array,HomeInstance)
         return True
      elif ColumnPicking == 3:
         cls.ColumnThree(Array,HomeInstance)
         return True
      elif ColumnPicking == 4:
         HomeInstance.HomeIntro()
         return True
      elif ColumnPicking == 5:return True
      else:return False

   @staticmethod
   def ColumnPickingIntro(HomeInstance,Array):
      for x in Array:print(x)
      while True:
         ColumnPicking = input("\n>>>What's Your Selection;\n1:Column 1\n2:Column 2\n3:Column 3\n4:Main Menu\n5:Go Back\n>>>Your Pick :")
         if ColumnPicking.isdigit():
            ColumnPickingVal = int(ColumnPicking)
            if ColumnEvents.ColumnPickingConditions(ColumnPickingVal,HomeInstance,Array):break
         else:
            print(">>>Please Enter a valid Input...Try Again")
            continue

   @classmethod
   def ColumnOneConditions(cls,ColumnOneContinue,HomeInstance):
      if ColumnOneContinue == 1:return True
      elif ColumnOneContinue == 2:return None
      elif ColumnOneContinue == 3:
         HomeInstance.HomeIntro()
         return True
      else:return False

   @classmethod
   def ColumnOneOperationConditions(cls,ColumnOneOperations,Array,HomeInstance):
      if ColumnOneOperations == 1:return f"\n>>>Your Sum is :{Array[:,0].sum()}"
      elif ColumnOneOperations == 2:return f"\n>>>Your Product is :{Array[:,0].prod()}"
      elif ColumnOneOperations == 3:return f"\n>>>Your Standard Deviation is :{Array[:,0].std()}"
      elif ColumnOneOperations == 4:return f"\n>>>Your Mean is :{Array[:,0].mean()}"
      elif ColumnOneOperations == 5:
         HomeInstance.HomeIntro()
         return True
      elif ColumnOneOperations == 6:return True
      else:return False

   @classmethod
   def ColumnOneEndCondition(cls,ColumnOneEnd,HomeInstance):
      if ColumnOneEnd == 1:
         cls.ColumnOne(Array,HomeInstance)
         return True
      elif ColumnOneEnd == 2:
         HomeInstance.HomeIntro()
         return True
      else:return False

   @staticmethod
   def ColumnOne(Array,HomeInstance):
      print(Array[:,0])
      while True:
         ColumnOneContinue = input("\n>>>Column Intrest;\n1:Column Content Arithmetics\n2:Select Another Column\n3:Main Menu\n>>>Your Option :")
         if ColumnOneContinue.isdigit():
            ColumnOneContinueVal = int(ColumnOneContinue)
            if ColumnEvents.ColumnOneConditions(ColumnOneContinueVal,HomeInstance):break
         else:
            print(">>>Please Enter a valid Input...Try Again")
            continue

      while True:
         ColumnOneOperations = input("\n>>>What Do you wanna Do ?\n1:Sum Up\n2:Product\n3:Standard Deviation\n4:Mean\n5:Main Menu\n6:Go Back\n>>>Your Option :")
         if ColumnOneOperations.isdigit():
            ColumnOneOperationsVal = int(ColumnOneOperations)
            ColumnOneResults = (ColumnEvents.ColumnOneOperationConditions(ColumnOneOperationsVal,Array,HomeInstance))
            if ColumnOneResults:
               print(ColumnOneResults)
               break
         else:
            print("\n>>>Select A valid Input...Try Again")
            continue

      while True:
         ColumnOneEnd = input("\n>>>Column One End Session;\n1:Arithmetic operation\n2:Main Menu\n>>>Your Input :")
         if ColumnOneEnd.isdigit():
            ColumnOneEndVal = int(ColumnOneEnd)
            if ColumnEvents.ColumnOneEndCondition(ColumnOneEndVal,HomeInstance):break
         else:
            print(">>>Please Enter A valid Input...Try Again")
            continue

#column 2 operations
   @classmethod
   def ColumnTwoOperationConditions(cls,ColumnTwoOperations,Array,HomeInstance):
      if ColumnTwoOperations == 1:return f"\n>>>Your Sum is :{Array[:,1].sum()}"
      elif ColumnTwoOperations == 2:return f"\n>>>Your Product is :{Array[:,1].prod()}"
      elif ColumnTwoOperations == 3:return f"\n>>>Your Standard Deviation is :{Array[:,1].std()}"
      elif ColumnTwoOperations == 4:return f"\n>>>Your Mean is :{Array[:,1].mean()}"
      elif ColumnTwoOperations == 5:
         HomeInstance.HomeIntro()
         return True
      elif ColumnTwoOperations == 6:return True
      else:return False

   @classmethod
   def ColumnTwoConditions(cls,ColumnTwoContinue,HomeInstance,Array):
      if ColumnTwoContinue == 1:return True
      elif ColumnTwoContinue == 2:
         cls.ColumnPickingIntro(HomeInstance,Array)
         return True
      elif ColumnTwoContinue == 3:
         HomeInstance.HomeIntro()
         return True
      else:return False

   @classmethod
   def ColumnTwoEndCondition(cls,ColumnTwoEnd,HomeInstance):
      if ColumnTwoEnd == 1:
         cls.ColumnTwo(Array,HomeInstance)
         return True
      elif ColumnTwoEnd == 2:
         HomeInstance.HomeIntro()
         return True
      else:return False

   @staticmethod
   def ColumnTwo(Array,HomeInstance):
      print(Array[:,1])
      while True:
         ColumnTwoContinue = input("\n>>>Column Intrest;\n1:Column Content Arithmetic\n2:Select Another Column\n3:Main Menu\n4:Go Back\n>>>Your Pick :")
         if ColumnTwoContinue.isdigit():
            ColumnTwoContinueVal = int(ColumnTwoContinue)
            if ColumnEvents.ColumnTwoConditions(ColumnTwoContinueVal,Array,HomeInstance):break
         else:
            print(">>>Select A valid Input...Try Again")
            continue

      while True:
         ColumnTwoOperations = input("\n>>>What Do you wanna Do ?\n1:Sum Up\n2:Product\n3:Standard Deviation\n4:Mean\n5:Main Menu\n6:Go Back\n>>>Your Pick :")
         if ColumnTwoOperations.isdigit():
            ColumnTwoOperationsVal = int(ColumnTwoOperations)
            ColumnTwoResults = ColumnEvents.ColumnTwoOperationConditions(ColumnTwoOperationsVal,Array,HomeInstance)
            if ColumnTwoResults:
               print(ColumnTwoResults)
               break
         else:
            print(">>>Enter a Valid Input...Try Again")
            continue

      while True:
         ColumnTwoEnd = input("\n>>>Column Two End Session;\n1:Arithmetic/Select Another Column\n2:Main Menu\n>>>Your Option :")
         if ColumnTwoEnd.isdigit():
            ColumnTwoEndVal = int(ColumnTwoEnd)
            if ColumnEvents.ColumnTwoEndCondition(ColumnTwoEndVal,HomeInstance):break
         else:
            print(">>>Please Enter A valid Input...Try Again")
            continue

   #Column Three
   @classmethod
   def ColumnThreeOperationConditions(cls,ColumnThreeOperations,Array,HomeInstance):
      """ Column Three Operations"""
      if ColumnThreeOperations == 1:return f"\n>>>Your Sum is :{Array[:,2].sum()}"
      elif ColumnThreeOperations == 2:return f"\n>>>Your Product is :{Array[:,2].prod()}"
      elif ColumnThreeOperations == 3:return f"\n>>>Your Standard Deviation is :{Array[:,2].std()}"
      elif ColumnThreeOperations == 4:return f"\n>>>Your Mean is :{Array[:,2].mean()}"
      elif ColumnThreeOperations == 5:
         HomeInstance.HomeIntro()
         return True
      elif ColumnThreeOperations == 6:return True
      else:return False

   @classmethod
   def ColumnThreeConditions(cls,ColumnThreeContinue,HomeInstance):
      if ColumnThreeContinue == 1:return True
      elif ColumnThreeContinue == 2:return None
      elif ColumnThreeContinue == 3:
         HomeInstance.HomeIntro()
         return True
      elif ColumnThreeContinue == 4:return None
      else:return False

   @classmethod
   def ColumnThreeEndCondition(cls,ColumnThreeEnd,HomeInstance):
      if ColumnThreeEnd == 1:
         cls.ColumnThree(Array,HomeInstance)
         return True
      elif ColumnThreeEnd == 2:
         HomeInstance.HomeIntro()
         return True
      else:return False

   @staticmethod
   def ColumnThree(Array,HomeInstance):
      print(Array[:,2])
      while True:
         ColumnThreeContinue = input("\n>>>Column Intrest;\n1:Column Content Arithmetic\n2:Select Another Column\n3:Main Menu\n4:Go Back\n>>>Your Pick :")
         if ColumnThreeContinue.isdigit():
            ColumnThreeContinueVal = int(ColumnThreeContinue)
            if ColumnEvents.ColumnThreeConditions(ColumnThreeContinueVal,HomeInstance):break
         else:
            print(">>>Please Enter a valid Input...Try Again")
            continue

      while True:
         ColumnThreeOperations = input("\n>>>What Do you wanna Do ?\n1:Sum Up\n2:Product\n3:Standard Deviation\n4:Mean\n5:Main Menu\n6:Go Back\n>>>Your Input :")
         if ColumnThreeOperations.isdigit():
            ColumnThreeOperationsVal = int(ColumnThreeOperations)
            ColumnThreeResults = ColumnEvents.ColumnThreeOperationConditions(ColumnThreeOperationsVal,Array,HomeInstance)
            if ColumnThreeResults:
               print(ColumnThreeResults)
               break
         else:
            print(">>>Please Enter a Valid Input...Try Again")
            continue

      while True:
         ColumnThreeEnd = input("\n>>>Column Three End Session;\n1:Arithmetic/Select Another Column\n2:Main Menu\n>>>Your Option :")
         if ColumnThreeEnd.isdigit():
            ColumnThreeEndVal = int(ColumnThreeEndVal)
            if ColumnEvents.ColumnThreeEndCondition(ColumnThreeEndVal,HomeInstance):break
         else:
            print(">>>Please Enter A valid Input...Try Again")
            continue

class Home:
   def __init__(self) -> None:pass

   @classmethod
   def HomeIntroConditions(cls,HomeInput,RowInstance,ColumnInstance,HomeInstance):
      if HomeInput == 1:
         RowInstance.RowSelection()
         return True
      elif HomeInput == 2:
         ColumnInstance.ColumnSelection(HomeInstance)
         return True
      elif HomeInput == 3:return True
      else:return False


   @staticmethod
   def HomeIntro():
      RowInstance = RowEvents()
      ColumnInstance = ColumnEvents()
      HomeInstance = Home()
      while True:
         HomeInput = input("\n>>>Home Directory;\n1:Row Section\n2:Column Section\n3:Close Application\n>>Your Input :")
         if HomeInput.isdigit():
            Val = int(HomeInput)
            if Home.HomeIntroConditions(Val,RowInstance,ColumnInstance,HomeInstance):break
         else:
            print(">>>Invalid Input...Try Again")
            continue



if __name__ == '__main__':
   print("\n>>>      Slim Numpy Work      >>>\n")
   Home.HomeIntro()



