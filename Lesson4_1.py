from sys import argv


def salary_calc():
    try:
        hour_rate, hours, bonus = map(float, argv[1:])
        return f"Ваша зарплата: {hour_rate * hours + bonus}"
    except ValueError:
        return "Введены некорректные параметры"


print(salary_calc())
