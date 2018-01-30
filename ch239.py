#https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

number = input("Enter Integer: ")
#num = int(input("Enter Number") 

#string to int
number = int(number)


while number != 1:

	#divisible by 3
	if number % 3 == 0:
		number = number // 3

		if number != 1:
			print(f"{number} 0")

	#number is closer to 
	elif number % 3 == 1:
		print (f"{number} - 1")
		number = number - 1

	elif number % 3 == 2:
		print (f"{number} + 1")
		number = number + 1

print("1")


#Good sample solution to go through
'''
num = int(input())

while num != 1:
    print("%d %d" % (num, (0, -1, 1)[int(num % 3)]))
    num = (num + (0, -1, 1)[int(num % 3)]) / 3

print(1)


'''