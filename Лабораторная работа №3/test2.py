# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, separator=","):
    list1 = str1.split(separator)
    list2 = str2.split(separator)
    list_final = []
    for participants1 in list1:
        for participants2 in list2:
            if participants1 == participants2:
                list_final += [participants1]

    return sorted(list_final)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

list_ = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(list_)