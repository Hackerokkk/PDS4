import itertools

# Задано натуральне число n. Навести в лексикографічному порядку всі перестановки елементів множини {1, 2, ..., n}.
def generate_permutations(n):
    # Створення множини {1, 2, ..., n}
    elements = list(range(1, n + 1))

    # Генерація всіх перестановок та сортування їх в лексикографічному порядку
    permutations = list(itertools.permutations(elements))

    # Повернення перестановок
    return permutations

# Задано натуральне число n і невід’ємне ціле число r (r ≤ n). Навести в лексикографічному порядку всі r-сполучення без повторень з елементів множини {1, 2, ... , n}.
def generate_combinations(n, r):
    # Створення множини {1, 2, ..., n}
    elements = list(range(1, n + 1))

    # Генерація всіх r-сполучень без повторень та сортування їх в лексикографічному порядку
    combinations = list(itertools.combinations(elements, r))

    # Повернення r-сполучень
    return combinations


# Виконання першого завдання: Навести в лексикографічному порядку всі перестановки елементів множини {1, 2, ..., n}.
n = int(input("Введіть натуральне число n: "))
permutations = generate_permutations(n)
print("Усі перестановки елементів множини {1, 2, ...,", n, "} в лексикографічному порядку:")
for permutation in permutations:
    print(permutation)


# Виконання другого завдання: Навести в лексикографічному порядку всі r-сполучення без повторень з елементів множини {1, 2, ..., n}.
n = int(input("Введіть натуральне число n: "))
r = int(input("Введіть невід'ємне ціле число r (r ≤ n): "))
combinations = generate_combinations(n, r)
print("Усі", r, "-сполучення без повторень елементів множини {1, 2, ...,", n, "} в лексикографічному порядку:")
for combination in combinations:
    print(combination)
