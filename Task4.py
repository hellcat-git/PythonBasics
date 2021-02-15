a = int(input("Please enter a number: "))
val = 0
while a > 0:
    d = a % 10
    if d > val:
            val = d
    a //= 10
print("Max digit is "+str(val))
