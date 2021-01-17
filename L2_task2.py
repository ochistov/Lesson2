'''
Create an empty list, entering a variable 
that specifies the length of the list
------------------------------------------
Создание пустого списка, введение переменной,
определяющей длину списка
'''
list_one = []
while True:
    try:
        list_len = int(input("Insert lenght of the list (integer number): ")) 
    except:
        print("That's not an integer number!\nPlease try again")
        continue
    break
for element in range(list_len):
    list_one.append(input(f"Please insert {element} element of list: ")) #appending new element to the list
print(f"Here is your list: {list_one}")
'''
Exchange of values of two adjacent elements 
of the list, provided that the current element 
is not the last in the list
----------------------------------------------
Обмен значениями двух соседних элементов в списке, 
при условии, что текущий элемент не последний в спике
(на случай нечётного количества элементов)
'''
for element in range(0, list_len, 2):
    if element + 1 < list_len:
        list_one[element], list_one[element + 1] = list_one[element + 1], list_one[element]

print(f"Here is your new list: {list_one}") #displaying result on the screen