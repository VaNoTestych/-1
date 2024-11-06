# TODO Напишите функцию для поиска индекса товара

def search(items_list, item): #Создал функцию search для поиска в списках
    for i, search_item in enumerate(items_list): #За счет цикла for и enumerate получаем индекс и сам предмет, а потом сравниваем с тем, который передали в функцию
        if search_item == item: 
            return i

    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item) #Применяем функцию на наши списки
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
