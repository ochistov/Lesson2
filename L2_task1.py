'''
Creating a list of different data types
------------------------------------------------
Создание списка, состоящего из различных типов данных
'''

list_one = [1, 12.7, 25, "elephant", "horse", 22, True, ['1', '2', '3', '4', '5'], {1:'a', 2:'b', 3:'c'}] 
print(list_one) # display our list on the screen

'''
Checking the type of each item in the list, displaying 
this information on the screen
-------------------------------------------------------
Проверка, к какому типу данных относится каждый элемент
списка, выведение этой информации на экран
'''
for element in range(len(list_one)):
    print(f"{element} element of list have class: {type(list_one[element])}")