class Node:
	def __init__(self,dataval = None):
		self.dataval = dataval
		self.nextval = None

class SLinkList:
	def __init__(self):
		self.headval = None
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval
	def InsertB(self,newdata):
		newNode = Node(newdata)
		newNode.nextval = self.headval
		self.headval = newNode
	def InsertE(self,newdata):
		newNode = Node(newdata)
		if self.headval is None:
			self.headval = newNode
			return
		laste = self.headval
		while laste.nextval :
			laste = laste.nextval
		laste.nextval = newNode
	def InsertBetween(self,midNode,newdata):
		if midNode is None:
			print("The Node is absent")
			return
		newNode = Node(newdata)
		newNode.nextval = midNode.nextval
		midNode.nextval = newNode
	def RemoveNode(self, Removekey):
		HeadVal = self.headval
         
		if (HeadVal is not None):
			if (HeadVal.dataval == Removekey):
				self.headval = HeadVal.nextval
				HeadVal = None
				return
		while (HeadVal is not None):
			if HeadVal.dataval == Removekey:
				break
			prev = HeadVal
			HeadVal = HeadVal.nextval
			if (HeadVal == None):
				return
		prev.nextval = HeadVal.nextval
		HeadVal = None
my_list = SLinkList()
my_list.headval = Node("monday")
d2 = Node("tues")
d3 = Node("wed")
d4 = Node("thus")
#link list
my_list.headval.nextval = d2
d2.nextval = d3
d3.nextval = d4
#Insert element to linklist
my_list.InsertB("sun")
my_list.InsertE("fri")

my_list.InsertBetween(d4,d2)
#remove Node
my_list.RemoveNode("fri")


#print list
my_list.listprint()

