# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


S = int (input("Введите количество сделанных журавликов: "))

print(f"Петя сделал журавликов: {S // 6} шт")
print(f"Сережа сделал журавликов: {S // 6} шт")
print(f"Катя сделала журавликов: {S * 4 // 6} шт")

