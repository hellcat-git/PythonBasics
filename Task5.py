income = int(input("please enter your company income in $: "))
loss = int(input("please enter your company loss in $: "))

margin = income - loss

profitability = round((margin/income)*100, 1)

if margin > 0:
    print("Your company has margin for " + str(margin) + "$")
    print("Your company profitability is "+str(profitability)+"%")
    headcount = int(input("Please enter your company headcount: "))
    margin_per_person = round(float(margin/headcount), 1)
    print("Margin per employee is: "+str(margin_per_person)+"$")
else:
    print("Your company has loss for " + str(margin) + "$")
