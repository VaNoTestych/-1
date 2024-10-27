money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0; #Количество дней, которые можно протянуть
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while(money_capital > 0):
    money_capital += (salary - spend)
    if(money_capital >= 0):
        spend += spend * increase
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
