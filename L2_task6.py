'''
Setting the variables necessary for the solution
--------------------------------------------------
Задаём переменные, необходимые для решения
'''
goods_template = {"name" : None, # шаблон словаря, содержащего сведения о товаре
                    "price" : None,
                    "count" : None,
                    "unit" : None}
goods_temp = [] # список, используемый для временного хранения данных
all_goods = [] # итоговый список, который будет состоять из кортежей, включающих в себя номер товара и словарь со сведениями
cnt = 0 # счётчик, необходимый для прерывания цикла while
dict_temp = [] # список из словарей, который нужен для аналитики товаров
fin_dict = dict() # итоговый словарь, включающий в себя характеристики товаров и списки их значений, полученных в первой части программы

'''
We find out the total number of products, form a list 
consisting of tuples, including the product number and a 
dictionary with information about the product. We also form
a list of dictionaries with information about the product
which will be needed further for analytics. Display result
on the screen.
-----------------------------------
Узнаём общее количество товаров, формируем список,
состоящий из кортежей, включающих в себя номер товара и
словарь со сведениями о товаре. Также формируем список из
словарей со сведениями о товаре, который понадобится далее
для аналитики. Выводим результат на экран.
'''
goods_cnt = int(input("How much goods we have?: ")) # количество товаров, которые будут заданы
while cnt < goods_cnt:
    goods_template['name'] = input(f'Name of {cnt + 1} good: ') 
    goods_template['price'] = float(input('Price: '))
    goods_template['count'] = int(input('Count (integer number): '))
    goods_template['unit'] = input('Unit: ')
    goods_temp.append(cnt + 1) # добавляем во временный список номер товара (+1, т.к. cnt начинается с нуля)
    goods_temp.append(goods_template.copy()) # добавляем во временный список копию заполненного словаря с информацией о товаре
    dict_temp.append(goods_template.copy()) # добавляем копию заполненного словаря с информацией о товаре в список из словарей, необходимый для аналитики
    goods = tuple(goods_temp) # преобразовываем временный список goods_temp в кортеж
    all_goods.append(goods) # добавляем полученный кортеж в итоговый список
    cnt += 1 # увеличиваем счётчик
    goods_temp.clear() # очищаем временный список
print(all_goods) # выводим на экран итоговый список

'''
We form a dictionary, the keys in which are the names of
the characteristics of the goods, and the values are lists
of the values obtained in the first part of the program.
Display result on the screen
----------------------------------------------------------
Формируем словарь, ключами в котором являются названия
характеристик товаров, а значениями списки из значений,
полученных в первой части программы
'''
for diction in dict_temp:
    for key, value in diction.items():
        if key not in fin_dict.keys(): #если ключ отсутствует в итоговом словаре, добавляем его вместе с его значением
            fin_dict.update({key : value})
        else:
            new_value = fin_dict.get(key) # присваиваем временной переменной значение ключа
            temp_value = [] # создаем пустой список
            temp_value.append(new_value) # добавляем в список значение ключа, которое уже есть в итоговом словаре
            temp_value.append(value) # добавляем в список новое значение ключа
            fin_dict.update({key : temp_value}) # обновляем значение итогового словаря по ключу (значением будет список)
print(f"Answer is {fin_dict}") # выводим на экране итоговый словарь с аналитикой

'''
Я не до конца понял, нужно ли дублировать одинаковые значения, но, т.к.
в задании речь идёт об аналитики, в итоге необходимо видеть полную картину.
В этой связи я не стал "сворачивать в 1" одинаковые значения.
'''
            
            