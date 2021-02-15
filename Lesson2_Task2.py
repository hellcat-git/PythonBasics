string = input("Пожалуйста, введите произвольные значения через запятую: ")
li = string.split(',')
li_result = []
i = 0
while i <= len(li):
    li_result.extend(li[i:i+2][::-1])
    i += 2
print(li_result)
