# Імпортуємо необхідний модуль для обробки виключень
class NegativeImportValueError(Exception):
    """Виняток, який генерується, якщо введена сума імпорту менше 0"""
    pass

# Функція для розрахунку мита
def calculate_duty(import_value: int, goods_group: str):
    """
    Розраховує мито залежно від суми імпорту та групи товарів.
    
    Параметри:
    - import_value (float): Сума імпорту (має бути >= 0).
    - goods_group (str): Група товарів (наприклад, 'A', 'B', 'C').
    
    Повертає:
    - float: Сума мита.
    
    Генерує:
    - NegativeImportValueError: Якщо import_value < 0.
    """
    if import_value < 0:
        raise NegativeImportValueError("Сума імпорту не може бути менше 0!")
    
    # Визначаємо ставки мита для кожної групи товарів
    duty_rates = {
        'A': 0.05,  # Група A: 5%
        'B': 0.10,  # Група B: 10%
        'C': 0.15   # Група C: 15%
    }
    
    # Отримуємо ставку мита для вибраної групи товарів
    rate = duty_rates.get(goods_group)
    if rate is None:
        raise ValueError("Невідома група товарів. Доступні групи: 'A', 'B', 'C'.")
    
    # Розрахунок мита
    duty = import_value * rate
    return duty

# Основна програма
if __name__ == "__main__":
    try:
        # Введення даних користувачем
        import_value = float(input("Введіть суму імпорту: "))
        goods_group = input("Введіть групу товарів (A, B, C): ").strip().upper()
        
        # Обчислення суми мита
        duty = calculate_duty(import_value, goods_group)
        print(f"Сума мита: {duty:.2f}")
    except NegativeImportValueError as e:
        print(f"Помилка: {e}")
    except ValueError as e:
        print(f"Помилка: {e}")
