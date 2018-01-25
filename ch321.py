#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
#talking clock

#assuming that the arguments = time given

import sys
from num2words import num2words
script, filename = sys.argv

#store each line from the text file into an array
fp = open(filename, 'r')


#each line is given the format xx:xx
#so just split the things on the left and right of the colon
for line in fp:

	#useful function SPLIT to split on a certain character
	hour = int(line.split(':')[0])
	minute = int(line.split(':')[1])

	day = 1

	#Case 1: hour is above 12
	if hour > 12:
		hour = hour - 12
		day = 0 #pm prefix after

	#Case 2: house is 01 - 12
	elif hour == 0:
		hour = 12

	#Case 4 : hour is 24
	elif hour == 24:
		hour = 12
		day = 0


	hour = num2words(hour)


	#making sure it's NOT ZERO
	#TODO: consider single digit minutes eg. 12 oh one and 12 oh three
	if (minute):
		if (minute < 10 and minute > 0):
			minute = "oh " + num2words(minute)
		else:
			minute = num2words(minute)
	else:
		minute = ""

	#consider case when minute is nothing, then you don't have to state minutes
	if (day):
		day = "am"
	else:
		day = "pm"

	#dealing with night or day

	print(f"It's {hour} {minute} {day} ")

fp.close()