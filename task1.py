list = []
all_inputs = []
inputs_number = 1

while inputs_number <= 5:
    user_input = input(f"Enter value {inputs_number}: ")
    all_inputs.append(user_input)

    try:
        number = int(user_input)
        list.append(number)
    except ValueError:
        print(f"'{user_input}' is not a valid integer. It won't be added to the list.")

    inputs_number += 1

print("List of valid values:", list)

def find_sum():
    summation = sum(list)
    print("Summation of the values:", summation)

def find_max():
    if list:
        maximum_value = max(list)
        print("Maximum value in the list:", maximum_value)
    else:
        print("No valid values to find the maximum.")

def find_mini():
    if list:
        minimum_value = min(list)
        print("Minimum value in the list:", minimum_value)
    else:
        print("No valid values to find the minimum.")

def find_average():
    if list:
        average = sum(list) / len(list)
        print("Average value in the list:", average)
    else:
        print("No valid values to calculate the average.")

def print_positive_values():
    if list:
        positive_values = [value for value in list if value >= 0]
        if positive_values:
            print("Positive values in the list:", positive_values)
        else:
            print("There are no positive values in the list.")
    else:
        print("The list is empty. No values to check.")

def print_negative_values():
    if list:
        negative_values = [value for value in list if value < 0]
        if negative_values:
            print("Negative values in the list:", negative_values)
        else:
            print("There are no negative values in the list.")
    else:
        print("The list is empty. No values to check.")

def find_multiple():
    if list:
        product = 1
        for value in list:
            product *= value
        print("Product of the values:", product)
    else:
        print("The list is empty. No values to compute the product.")

def count_repetitions():
    repetitions = {}
    for input_value in all_inputs:
        if input_value in repetitions:
            repetitions[input_value] += 1
        else:
            repetitions[input_value] = 1

    print("Repetitions of each input:")
    for input_value, count in repetitions.items():
        print(f"'{input_value}': {count} time(s)")


find_sum()
find_multiple()
find_max()
find_mini()
find_average()
print_positive_values()
print_negative_values()
count_repetitions()



