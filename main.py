

while True:
	user_input = input("Enter something: ").lower()

	if user_input == 'hi':
		print('Hello!')
	elif user_input ==  'good':
		print('Good to hear!')
	elif user_input == 'bad':
		print('WHY!?!?')
	elif user_input == 'tae':
		print('Delicious yum yum!')
	elif user_input == 'hello':
		print('Hi!')
	elif user_input == 'bye':
		print('bye')
		break
	else:
		print('I do not understand')