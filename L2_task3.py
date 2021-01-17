'''
Setting a variable indicating the number of the 
month the user is interested in
--------------------------------------------------
Создание переменной, определяющей номер месяца, 
интересующий пользователя
'''
while True:
    try:
        numb_month = int(input("Insert number of month (integer number): "))
        if numb_month > 12 or numb_month <= 0:
            print("There are only 12 months in year!\nPlease, try again")
            continue
    except:
        print("That's not an integer number!\nPlease, try again")
        continue
    break
# Solution through dict()
'''
Creating dict() "seasons" where the keys are the names of 
the seasons and the values are lists of the numbers of the 
months
----------------------------------------------------------
Создание словаря "seasons", в котором ключами являются
названия времён года, а значениями - списки из номеров
месяцев
'''
seasons = dict()
seasons['winter'] = [12, 1, 2]
seasons['spring'] = [3, 4, 5]
seasons['summer'] = [6, 7, 8]
seasons['autumn'] = [9, 10, 11]

'''
Checking for all dictionary keys if there is a "numb_month"
among the values and, if successful, display the key value 
on the screen as an answer
-----------------------------------------------------------
Проверка по всем ключам словаря, есть ли среди их значений
номер месяца, введённый пользователем и в случае успеха
вывод ключа словаря на экран в качестве ответа
'''

for season, months in seasons.items():
        if numb_month in months:
            print(f"The {numb_month} month of year is {season}")

#solution through list()
'''
Creation of four lists, each of which consists of the 
numbers of the months included in the season
----------------------------------------------------
Создание четырёх списков, каждый из которых состоит из
номеров месяцев, входящих во время года
'''

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

'''
Checking if the "numb_month" is in one of the lists, if 
successful, display the result on the screen
--------------------------------------------------------
Проверка, находится ли номер месяца, заданный
пользователем, в одном из списков, в случае успеха
вывод результата на экран
'''

if numb_month in winter:
    print(f"The {numb_month} month of year is winter")
elif numb_month in spring:
    print(f"The {numb_month} month of year is spring")
elif numb_month in summer:
    print(f"The {numb_month} month of year is summer")
elif numb_month in autumn:
    print(f"The {numb_month} month of year is autumn")