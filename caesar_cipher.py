import string
message=input("enter a message\n")
shift_number=int(input("enter a shift number\n"))

lower_letter=string.ascii_lowercase
upper_letter=string.ascii_uppercase



def shift_message (sentence, number):
	en_message=""
	for letter in sentence :
		if letter in lower_letter:
			position=lower_letter.index(letter)
			new_position=(position + number) % len(lower_letter)
			en_message += lower_letter[new_position]
		elif letter in upper_letter:
			position=upper_letter.index(letter)
			new_position=(position+number) % len(upper_letter)
			en_message += upper_letter[new_position]
		else:
			en_message += letter
	print(en_message)


shift_message(message, shift_number)