#file = open("example.txt", "w")
#file.write("Hello, World!")
#file.close()

file = open("example.txt", "r")
content = file.read()
print(content)  # Output: Hello, World!
file.close()