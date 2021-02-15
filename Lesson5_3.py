def salary_func():
    with open("text_3.txt", 'r', encoding='utf-8') as f:
        total_list = f.readlines()
    new_list = [el.strip() for el in total_list if float(el.split()[1]) > 20000]
    salary = [float(el.split()[1]) for el in total_list if float(el.split()[1]) > 20000]
    avg_salary = sum(salary) / len(new_list)

    st = ", ".join(new_list)

    print(f"Список сотрудников с зарплатой больше 20000: {st}.\nСредняя зарплата выбранных сотрудников: {avg_salary}")


salary_func()
