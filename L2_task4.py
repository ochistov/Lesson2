'''
Generating a word list from a user-defined string using a 
space as a separator
------------------------------------------------------------
Формирование списка слов из заданной пользователем строки
с использованием пробела в качестве разделителя
'''
list_one = input("Say something: ").split()

'''
Displaying on the screen each word on a new line with line 
numbering. If there are more than ten characters in the word,
displaying the first 10
------------------------------------------------------------
Отображение на экране каждого слова с новой строки с 
нумерацией строк. Если в слове более десяти символов,
отображение первых 10
'''
for i in range(len(list_one)):
    print(f"{i + 1} word is {list_one[i][:10]}")

'''
Solution through enumerate()
------------------------------------
Решение с помощью функции enumerate()
'''
for number, word in enumerate(input("Say something: ").split()): # разбиение строки на кортежи формата (индекс, значение) с использованием пробела в качестве разделителя
    print(f"The {number} word is {word[:10]}") #вывод первых десяти символов каждого слова с новой строки, с нумерацией строк