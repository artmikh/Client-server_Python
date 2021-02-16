import unittest
from complex import Complex_class


class TestComplex(unittest.TestCase):
    # Задаем исходные данные для проверки
    real_part_1 = 10
    mnimo_part_1 = 25
    real_part_2 = 5
    mnimo_part_2 = 13

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        self._test_converting_num_1()
        self._test_converting_num_2()
        
        self._test_complex_num_1()
        self._test_complex_num_2()

    def tearDown (self):
        # Выполнить завершающие действия (если необходимо)
        # как здесь вывести принт самого теста, т.е. "test_sum: (10+25j) + (5+13j) = (15+38j)"
        pass
    
    def _test_converting_num_1(self):
        # данные из модуля
        self.complex_number_1 = Complex_class(int(self.real_part_1), int(self.mnimo_part_1))
        return self.complex_number_1
       

    def _test_converting_num_2(self):
        # данные из модуля
        self.complex_number_2 = Complex_class(int(self.real_part_2), int(self.mnimo_part_2))
        return self.complex_number_2
      

    def _test_complex_num_1(self):
        # проверочные данные
        self.compl_num_1 = complex(int(self.real_part_1), int(self.mnimo_part_1))
        return self.compl_num_1

    def _test_complex_num_2(self):
        # проверочные данные
        self.compl_num_2 = complex(int(self.real_part_2), int(self.mnimo_part_2))
        return self.compl_num_2

    def test_sum(self):
        self.assertEqual(complex(self.complex_number_1 + self.complex_number_2), (self.compl_num_1 + self.compl_num_2), 'не варик')

    def test_mul(self):
        self.assertEqual(complex(self.complex_number_1 * self.complex_number_2), (self.compl_num_1 * self.compl_num_2), 'не варик')
  

    # def test_common(self):
    #     self._test_converting_num_1()
    #     self._test_converting_num_2()
        
    #     self._test_complex_num_1()
    #     self._test_complex_num_2()

    #     self.assertEqual(complex(self.complex_number_1 + self.complex_number_2), (self.compl_num_1 + self.compl_num_2), 'не варик')
    #     self.assertEqual(complex(self.complex_number_1 * self.complex_number_2), (self.compl_num_1 * self.compl_num_2), 'не варик')
  


# Запустить тестирование
if __name__ == '__main__' :
    unittest.main()