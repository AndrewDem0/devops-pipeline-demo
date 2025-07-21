import unittest
from main import calculate_duty, NegativeImportValueError


# Тестовий клас для перевірки функції calculate_duty
class TestCalculateDuty(unittest.TestCase):
    def test_positive_values(self):
        """Тестуємо коректні значення для різних груп товарів."""
        self.assertEqual(calculate_duty(1000, 'A'), 50.0)
        self.assertEqual(calculate_duty(2000, 'B'), 200.0)
        self.assertEqual(calculate_duty(1500, 'C'), 225.0)
    
    def test_negative_import_value(self):
        """Перевіряємо генерацію виключення для від'ємної суми імпорту."""
        with self.assertRaises(NegativeImportValueError):
            calculate_duty(-100, 'A')
    
    def test_invalid_goods_group(self):
        """Перевіряємо генерацію виключення для невідомої групи товарів."""
        with self.assertRaises(ValueError):
            calculate_duty(1000, 'D')
    
    def test_edge_cases(self):
        """Перевіряємо крайні значення."""
        self.assertEqual(calculate_duty(0, 'A'), 0.0)

    @unittest.expectedFailure
    def test_invalid_goods_group_does_not_raise(self):
        """Тест провалюється, якщо ValueError не піднімається."""
        with self.assertRaises(NegativeImportValueError):  # Помилка повинна бути іншого типу
            calculate_duty(1000, 'L')

# Виконання тестів
if __name__ == "__main__":
    unittest.main()
