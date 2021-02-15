val = int(input("Type a month number from 1 to 12: "))

# проверка на ввод 0
if val > 12 or val <= 0:
    val = int(input("Incorrect month. Type a month number from 1 to 12: "))
months_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

# заполняем список значениями из словаря
months_list = []
i = 1
while i <= 12:
    months_list.append(months_dict.get(i))
    i += 1
print("your birth was in "+months_dict.get(val))
print("let's check again. your birth was in "+months_list[val-1])

# решение 2 - совмещение list и dict
months_seasons = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 0}
months_seasons_list = ['winter', 'spring', 'summer', 'autumn']
print(months_seasons_list[months_seasons.get(val)])
