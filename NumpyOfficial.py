

import numpy as np

ListOne = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                    [['J','K','L'],['M','N','O'],['P','Q','R']],
                    [['S','T','U'],['V','W','X'],['Y','Z','_']]])

Bitch = ListOne[0,0,1] + ListOne[0,2,2] + ListOne[2,0,1] + ListOne[0,0,2] + ListOne[0,2,1] + ListOne[2,2,2] + ListOne[0,0,0] + ListOne[2,0,0] + ListOne[2,0,0] + ListOne[2,2,2] + ListOne[1,1,1] + ListOne[0,2,2] + ListOne[0,2,0] + ListOne[0,2,0] + ListOne[0,0,0]

print(f"___________________\n\n>>> Number of Dimensions :{ListOne.ndim}\n>>> Array Shape :{ListOne.shape}\n\n___________________")

list = np.array([[['1','a','5','7'],['a','c','f','k']],
                 [['a','x','y','f'],['@','&','f','g']]])
print(f">>> Number of Dimension :{list.ndim}\n>>> Order :{list.shape}\n\n_______________\n>>> Our native insults :{Bitch.title()}")

""" Group One & Two deals with cylinders"""

class CylinderArea:
   def __init__(self,Area,Perimeter,Volume):
      self.Area = Area
      self.Perimeter = Perimeter
      self.Volume = Volume
      self.CylinderGrp =[[]]
      self.CuboidGrp = [[]]

   def GetUserInput(self,Prompt,ConditionFunc,ErrMsg):
      while not self.ConditionFunc(Val := input(self.Prompt)):
         print(f">>> {Val} is not Allowed\n{self.ErrMsg}")
      self.CylGrps = self.CylinderGrp[-1]
      if len(self.CylGrps) == 3:
         self.CylinderGrp.append([Val])
      else:
         self.CylGrps.append(Val)
      return Val

   @staticmethod
   def GetUser(Prompt,ConditionFunc,ErrMsg):
      while not (ConditionFunc(Val := input(Prompt))):
         print(f">>> {Val} is not Allowed.\n{ErrMsg}.")
      return Val

   """Collections of Cylinder Radius"""
   def CylinderInputs(self):
      print("\n__________ All Group One Cylinder __________\n")
      while True:
         float(self.GetUserInput("\n>>> Radius Of the Cylinder in Metres:",lambda x:x.replace('.','').isdigit(),">>> Enter a valid radius"))
         float(self.GetUserInput("\n>>> Height of the Cylinder in Metres:",lambda x:x.replace('.','').isdigit(),">>> Enter valid radius"))
         int(self.GetUserInput("\n>>> How many Cylinders are There :",lambda x:x.isdigit(),">>> Enter a valid Number."))
         if self.GetUser(">>> Press 'Q or q' if you want to Quit :",lambda x:x.isalpha() and len(x) == 1,">>> Enter a valid Input").lower() == 'q':
            for x in self.CylinderGrp:print(*x)
            return self.Area()

   def Area (self):
      self.CylinderVal = np.array(self.CylinderGrp)
      print(f">>> The Grouos are in Order of :{self.CylinderVal.shape}.\n>> Where self.CylinderVal[0] is Number of Group Items\n>> {self.CylinderVal[1]} is Number of Rows in Each Group\n>> {self.CylinderVal[2]} is Number of Columns in Each Row.")

if __name__ == '__main__':
   test = CylinderArea()
   test.CylinderInputs()
