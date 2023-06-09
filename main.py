# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# Будем считать цифру 0 решкой, а цифру 1 - орлом.
# соответственно количество решек - это будет количество менет, которые надо перевернуть орлом
# а количество орлов - количество монет, которые надо повернуть решкой

from random import randint

print("Введите число монет n:")
n = int(input())

coins = list()
for i in range(n):
    coin = randint(0, 1)
    coins.append(coin)

print("Монеты:", coins)

count_revers = 0
for i in range(n):
    if coins[i] == 0:
        count_revers = count_revers + 1

count_avers = n - count_revers

print("Решки:", count_revers)
print("Орлы:", count_avers)

