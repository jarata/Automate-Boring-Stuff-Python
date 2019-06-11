spam = 0
while spam < 5:
	print('Hello world!')
	spam = spam + 1

print('\n')

name = ''
while name != 'your name':
	print('Please type your name.')
	name = input()
print('Thank you!')

print('\n')

spam = 0
while spam < 5:
	spam = spam + 1
	if spam == 3:
		continue
	print('spam is ' + str(spam))