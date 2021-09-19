# Fase 1


"""
I primi dodici numeri della sequenza di Fibonacci sono:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

Il 12° numero è il primo della sequenza a essere di 3 cifre. Quale è il primo numero della sequenza ad avere 1000 cifre?
"""


def fibonacci_1000():
    numbers = []
    i = 0
    while True:
        if i == 0 or i == 1:
            n_in = 1
        else:
            n_in = numbers[i - 1] + numbers[i - 2]
        numbers.append(n_in)
        i += 1
        if len(str(n_in)) == 1000:
            return len(numbers)


if __name__ == '__main__':
    print(fibonacci_1000())
