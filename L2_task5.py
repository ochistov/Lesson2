'''
Сreating a list filled with arbitrary natural numbers
---------------------------------------------------
Создание списка, заполненного произвольными
натуральными числами
'''
list_one = [7, 5, 3, 3, 2]
'''
Adding a user-specified number to the list
sorting the list from smallest to largest, inverting the list
(placing items from largest to smallest), display
result on the screen
------------------------------------------------
Добавление к списку числа, указанного пользователем,
сортировка списка от меньшего к большему, инверсия списка
(размещение элементов от большего к меньшему), вывод 
результата на экран
'''

while True:
    try:
        list_one.append(int(input("Insert number: "))) #добавление к списку числа с преобразованием в int
        print(list(reversed(sorted(list_one)))) #сортировка, реверс и вывод на экран списка
        
    except ValueError:
        print("That's not an integer number!\nPlease try again")
        continue
    break