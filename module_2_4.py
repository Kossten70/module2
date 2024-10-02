numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Список простых.
not_primes = []  # Список не простых

for num in numbers:
    is_prime = True
    if num > 1:
        for j in range(2, num):  # Делитель. Перебирает делители от 2 до числа num.
            if num % j == 0:  # Проверка на простое число.
                is_prime = False
                break
        if is_prime:
            primes.append(num)  # Добавляет число в список простых
        else:
            not_primes.append(num)  # Добавляет в список не простых

print(primes)
print(not_primes)