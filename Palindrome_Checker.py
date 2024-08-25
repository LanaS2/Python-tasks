original_string = input("Enter a string: ")

cleaned_string = ''.join(char.lower() for char in original_string if char.isalnum())

if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
