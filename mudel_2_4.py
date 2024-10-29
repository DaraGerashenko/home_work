
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for m in numbers:
    if m == 1:
        continue
    is_prime = True
    for j in range(2, m):
        if m % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(m)
    else:
        not_primes.append(m)
print('простые числа', primes)
print('не простые числа',not_primes)