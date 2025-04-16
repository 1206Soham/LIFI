# Input from user
num_str = input("Enter an integer: ")

# Convert each character to an integer and store in a list
digit_list = [int(digit) for digit in num_str]

# Display the result
print("List of digits:", digit_list)
