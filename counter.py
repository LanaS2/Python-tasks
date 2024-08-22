A = []
counter = {}


for i in range(1, 5):
    inputs = input("Enter a number: ")
    A.append(int(inputs))


for num in A:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

print(counter)
