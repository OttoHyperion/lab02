def eratosthenes(n):
    # Инициализируем список для отметки составных чисел
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            # Убираем все кратные числа p, начиная с p^2
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Собираем список простых чисел
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

N = int(input("Введите число N: "))
primes = eratosthenes(N)
print(f"Простые числа до {N}: {primes}")