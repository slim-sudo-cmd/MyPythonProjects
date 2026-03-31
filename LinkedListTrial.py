

import time
#implementing Linked List

class Node:
   def __init__(self,Data = None) ->None:
      self.Data = Data
      self.next = None

class LinkedList:

   def __init__(self):
      self.Head = Node()

   def Append(self,Data):
      self.NewNode = Node(Data)
      self.CurrentNode = self.Head
      while self.CurrentNode.next != None:
         self.CurrentNode = self.CurrentNode.next
      self.CurrentNode.next = self.NewNode

   def Length(self):
      self.Total = 0
      self.CurrentNode = self.Head
      while self.CurrentNode.next != None:
         self.CurrentNode = self.CurrentNode.next
         self.Total += 1
      return Total

   def Display(self):
      self.Element = []
      self.CurrentNode = self.Head
      while self.CurrentNode.next != None:
         self.CurrentNode = self.CurrentNode.next
         self.Element.append(self.CurrentNode.Data)
      return self.Element

   def Get(self,index):
      if index > self.Length:
         print("Oops Out of range")
         return None
      self.CurrentNode = self.Head
      self.CurrentIndex = 0
      while True:
         self.CurrentNode = self.CurrentNode.next
         if self.CurrentIndex == index:return self.CurrentNode.Data
         self.CurrentIndex += 1

StartTime = time.perf_counter()
my = LinkedList()
print(f"My list before Appending :{my.Display()}")
my.Append(1)
my.Append(4)
my.Append(7)
print(f"My List After Appending :{my.Display()}")
StopTime = time.perf_counter()
Duration = StopTime - StartTime
print(f">>>Program Start Time:{StartTime:.4f}seconds\n>>>Program Stop Time :{StopTime:4f}seconds\n>>>Program Total Time Taken :{Duration:.4f}seconds")
