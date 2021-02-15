value = input("Please enter a number 1-9: ")

i = 0
line = ''
res = 0

while i <= 2:
    line += value
    res += int(line)
    i = i+1

print(res)
