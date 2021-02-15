goods_dict_list = []
goods_no = 1
array = []
while True:
    attr_list = ['название', 'цена', 'кол-во', 'ед']
    print(f"Заполняем сведения о товаре {goods_no}")
    for i in attr_list:
        a = input(f"Введите значение атрибута '{i}': ")
        goods_dict_list += [(i, a)]
    array += [(goods_no, dict(goods_dict_list))]
    goods_dict_list.clear()
    print(array)
    menu = input("Продолжаем ввод данных? Y or N? ")
    if menu.upper() == "Y":
        goods_no = goods_no + 1
    else:
        break
# print(array)
analytics = {}
for i in attr_list:
    value_set = set()
    for val in array:
        value_set.add(val[1].get(i))
    dd = {i: list(value_set)}
    analytics.update(dd)
print(analytics)
