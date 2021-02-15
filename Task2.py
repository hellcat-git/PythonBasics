value = int(input("Please enter time in sec: "))
days = value // (24*3600)
seconds = value - (days*(24*3600))
hour = seconds // 3600
minutes = int((seconds-(hour*3600))//60)
seconds = int((seconds-(hour*3600))-(minutes*60))

print(str(days) + " day(s) " + f"{hour:02}:{minutes:02}:{seconds:02}")
