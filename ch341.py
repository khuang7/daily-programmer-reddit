#https://www.reddit.com/r/dailyprogrammer/comments/7eh6k8/20171121_challenge_341_easy_repeating_numbers/


#Enter a number from user input
print(f"Please enter a number")
number = input()

total_length = len(number)
#can't have a repeating sequence with more than half the digits
max_length = len(number)//2 #// means INTEGER DIVISION (no remainder)

#convert to a string (to make slicing easier)
number = str(number)

#number -> repetitions
d = dict()

#minimum is 2 number length
while (max_length > 1):
	#lets consider the 3 digits
	range_left = 0
	range_right = max_length

	while (range_right <= total_length):
		
		key = number[range_left:range_right]

		if key in d:
   			d[key] += 1
		else:
			d[key] = 1

		range_left = range_left + 1
		range_right = range_right + 1

	max_length = max_length - 1

for key,value in d.items():
	if(value != 1):
		print(f"{key}:{value}")
#put each digit into an array
#remember that length must be one less than half of the list

