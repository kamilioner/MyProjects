### Ex. 4 (File read)

number_of_lines = 0
f = open("text.txt", "r")
for line in f:
    number_of_lines += 1
    if ("you " in line) or (" you" in line):
        print(str(number_of_lines) + ": " + line)