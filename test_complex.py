import unittest
from complex import *


class TestComplex(unittest.TestCase):
    real_part_1 = 10
    mnimo_part_1 = 25
    real_part_2 = 5
    mnimo_part_2 = 13

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass
    def tearDown (self):
        # Выполнить завершающие действия (если необходимо)
        pass
    
    def _test_converting_num_1(self):
        self.complex_number_1 = Complex(int(self.real_part_1), int(self.mnimo_part_1))
        # print(complex_number_1)

    def _test_converting_num_2(self):
        self.complex_number_2 = Complex(int(self.real_part_2), int(self.mnimo_part_2))
        # print(complex_num_2)

    def _test_complex_num_1(self):
        self.compl_num_1 = Complex(complex(int(self.real_part_1), int(self.mnimo_part_1)))

    def _test_complex_num_2(self):
        self.compl_num_2 = Complex(complex(int(self.real_part_2), int(self.mnimo_part_2)))

    def test_sum(self):
        self._test_converting_num_1()
        self._test_converting_num_2()
        self._test_complex_num_1()
        self._test_complex_num_2()
        self.assertEqual((self.complex_number_1 + self.complex_number_2), (self.compl_num_1 + self.compl_num_2), 'не варик')


# Запустить тестирование
if __name__ == '__main__' :
    unittest.main()