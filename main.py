# Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является
# степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.

def power_of_two(number):
    power_two = 'yes'
    not_power_two = 'no'
    if number == 2:
        return power_two
    elif number % 2 != 0:
        return not_power_two
    else:
        return power_of_two(number / 2)


print(power_of_two(512))
