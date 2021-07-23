import random 
def guess(x):
		random_number = random.randint(1,x)
		guess = 0
		while guess != random_number:
			guess = int(input(f"Guess a number between 1 to {x}!"))
			if guess < random_number:
				print("Too low")
			elif guess > random_number:
				print("Too high")
		print(f"yeh,Congrat you have guessed the number {random_number} correctly!")
number = int(input("nhap so "))
guess(number)


# t = "hom nay la ngay dep troi"
# s = "dayasdg adojf ED FG AS"

# table = 'have'
# s= s.title()
# print(s)