#https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/
#Challenge 348 (Easy)

import sys
script_name, init_male_rabbits, init_female_rabbits, rabbits_needed = sys.argv


init_male_rabbits = int(init_male_rabbits)
init_female_rabbits = int(init_female_rabbits)
rabbits_needed = int(rabbits_needed)


month_count = 0
rabbit_count = init_male_rabbits + init_female_rabbits



males = []
females = []



for index in range(init_male_rabbits):
	males.append(2)

for index in range(init_female_rabbits):
	females.append(2)


total_rabbit_count = init_male_rabbits + init_female_rabbits



while (total_rabbit_count < rabbits_needed):

	month_count = month_count + 1
	#go through each male	
	for index, item in enumerate(males):
		males[index] = item + 1

	for index, item in enumerate(females):
		females[index] = item + 1	



	for item in females:
		#reproduce
		if item >=4 and item < 96:
			#add 5 male (0 months old)	
			for index in range(5):
				males.append(0)
			#add 9 female (0 months old)
			for index in range(9):
				females.append(0)



	#go through the whole list and count rabbits less than 96
	total_rabbit_count = 0
	for item in males:
		if item < 96:
			total_rabbit_count = total_rabbit_count + 1

	for item in females:
		if item < 96:
			total_rabbit_count = total_rabbit_count + 1

	print(males)
	print(females)
	print(total_rabbit_count)

print(month_count)

		







	#month_count = month_count + 1
 









