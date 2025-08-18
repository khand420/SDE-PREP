def convert_digits(input_string, start_position, end_position):
	# Adjust for 0-based indexing
	start_position -= 1
	end_position -= 1

	# Check for invalid conditions
	if start_position > end_position:
		return "INVALID"
	if start_position < 0:
		return "INVALID"
	if end_position >= len(input_string):
		return "INVALID"

	new_string = ""
	digit_mapping = {
		'0': 'ZERO',
		'1': 'ONE',
		'2': 'TWO',
		'3': 'THREE',
		'4': 'FOUR',
		'5': 'FIVE',
		'6': 'SIX',
		'7': 'SEVEN',
		'8': 'EIGHT',
		'9': 'NINE'
	}

	# Build the new string with digit conversions
	for index in range(len(input_string)):
		if start_position <= index <= end_position and input_string[index].isdigit():
			new_string += digit_mapping[input_string[index]]
		else:
			new_string += input_string[index]

	return new_string



print(convert_digits("Call my office 888-123-4567.", 16, 18))  # "Call my office EIGHTEIGHTEIGHT-123-4567."
print(convert_digits("Hello 123", 0, 5))  # "INVALID"











# def convert_digits( input_string, start_position, end_position ) :
# 	new_string = input_string[:start_position]
# 	digit_mapping = {
# 		'0': 'ZERO',
# 		'1': 'ONE',
# 		'2': 'TWO',
# 		'3': 'THREE',
# 		'4': 'FOUR',
# 		'5': 'FIVE',	
# 		'6': 'SIX',
# 		'7': 'SEVEN',
# 		'8': 'EIGHT',
# 		'9': 'NINE'
# 	}
	
# 	for index in range(start_position, end_position):
# 		if input_string[index].isdigit():
# 			mapped = digit_mapping[input_string[index]]
# 			new_string = mapped
		
# 	new_string += input_string[end_position + 1:]
# 	return new_string