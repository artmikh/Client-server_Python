""" Вариант 1: С использованием встроеного класса complex """
class Complex:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        return self.num + other.num
    
    def __mul__(self, other):
        return self.num * other.num

print('Мы хотим сложить и умножить комплексные числа')
print('Первое комплексное число')
complex_num_1 = Complex(complex(int(input('Введите действительную часть - ')), int(input('Введите мнимую часть - '))))
print(complex_num_1.num)
print('Второе комплексное число')
complex_num_2 = Complex(complex(int(input('Введите действительную часть - ')), int(input('Введите мнимую часть - '))))
print(complex_num_2.num)
print()
print(f'Сумма чисел {complex_num_1.num} и {complex_num_2.num} равна {complex_num_1 + complex_num_2}')
print(f'Произведение чисел {complex_num_1.num} и {complex_num_2.num} равна {complex_num_1 * complex_num_2}')