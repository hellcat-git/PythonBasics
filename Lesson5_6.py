file = open('text_6.txt', 'r', encoding='utf-8')
my_dict = {}

while True:
    line = file.readline().strip()
    if not line:
        break
    arr = line.split()

    hours = []
    for i in arr:
        string = "".join([ele for ele in i if ele.isdigit()])
        if string.isdigit():
            hours.append(string)
    my_dict.update({arr[0].replace(":", ""): sum(map(int, hours))})

file.close()

print(my_dict)
