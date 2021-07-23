import numpy.random as rd 
import time 

print("--"*8)
print("Welcome you to my game!")
print("Rule is :1 is punch ,2 is leaves,3 is sciscors ")
print("You have 3 turn ")
print("--"*8)
turn = 3
while turn !=0:
	print(f"Now you have {turn} turn")
	you = int(input("Your turn ,please enter your choice: "))
	computer = rd.choice([1,2,3])
	print("computer chose :",computer)

	def main():
		if(you == 1 and computer == 2) or (you == 2 and computer == 3) or (you == 3 and computer ==1):
			print("You lose !")
		elif (you == 1 and computer == 3 ) or (you ==2 and computer == 1) or (you ==3 and computer == 2):
			print("You win !")
		else:
			print("Draw :))")

	main()
	turn = turn -1
	print("*"*20)

	time.sleep(2)


