# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, separator=","): #Создаем функцию по поиску из двух строк, начальным значением separator выбираем по условию запятую
    list1 = str1.split(separator) #Создаем список из строк с фамилиями 
    list2 = str2.split(separator) # Анлогично для второй строки
    list_final = [] #Создаем пустой список, куда будем "закидывать" совпадащие фамилии
    for participants1 in list1:
        for participants2 in list2: #С помощью вложенного цикла проходимся по двум спискам и сравниваем значения, если совпадают -> в список
            if participants1 == participants2:
                list_final += [participants1]

    return sorted(list_final) #Возвращаем отсортированный список

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

list_ = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(list_)
