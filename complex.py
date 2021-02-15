""" Вариант 2: С самодельным созданием комплексных чисел """
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a}+{self.b}j)'

    def __add__(self, other):
        return f'({(self.a + other.a)}+{(self.b + other.b)}j)'
    
    def __mul__(self, other):
        return f'({self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}j)'

print('Мы хотим сложить и умножить комплексные числа')
print('Первое комплексное число')
complex_num_1 = Complex(int(input('Введите действительную часть - ')), int(input('Введите мнимую часть - ')))
print(complex_num_1)
print('Второе комплексное число')
complex_num_2 = Complex(int(input('Введите действительную часть - ')), int(input('Введите мнимую часть - ')))
print(complex_num_2)
print()
print(f'Сумма чисел {complex_num_1} и {complex_num_2} равна {complex_num_1 + complex_num_2}')
print(f'Произведение чисел {complex_num_1} и {complex_num_2} равна {complex_num_1 * complex_num_2}')