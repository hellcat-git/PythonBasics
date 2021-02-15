height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
bmi = round(weight/((height/100) ** 2), 1)

if bmi <= 18.4:
    status = "under weight"
elif bmi <= 24.9:
    status = "healthy"
elif bmi <= 29.9:
    status = "overweight"
else:
    status = "obese"
print("your bmi index: " + str(bmi) + ", looks like "+status)
