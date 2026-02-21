

class Node:
   def __init__(self,Data = None) -> None:
      self.Data = Data
      self.next = None

class LinkedList:
   def __init__(self):
      self.Head = Node()

   def Append(self,Data):
      self.NewNode = Node(Data)
      self.CurrentNode = self.Head
      while self.CurrentNode != None:
         self.CurrentNode = self.CurrentNode.next
      self.CurrentNode.next = self.NewNode

   def Length(self):
      self.Total = 0
      self.CurrentNode = self.Head
      while self.CurrentNode != None:
         self.CurrentNode = self.CurrentNode.next
         self.Total += 1
      return self.Total

   def Display(self):
      self.CurrentNode = self.Head
      self.Elements = []
      while self.CurrentNode != None:
         self.CurrentNode = self.CurrentNode.next
         self.Elements.append(self.CurrentNode.Data)
      return self.Elements

   def Get(self,index):
      if index > self.Length():return None
      self.CurrentNode = self.Head
      self.CurrentIndex = 0
      while True:
         self.CurrentNode = self.CurrentNode.next
         if self.CurrentIndex == index:return self.CurrentNode.Data
         self.CurrentIndex += 1


list = LinkedList()
print(f"List Before Appending :{list.Display()}")
list.append(5)
list.append(3)
list.append(7)
list.append(1)
print(f"List After Appending :{list.Display()}")
