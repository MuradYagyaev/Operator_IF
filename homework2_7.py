# Модуль 2 урок №2. "Условный оператор. Как работает оператор if."
# что нельзя сравнивать - разные типы
if '6' > 5:         # Ошибка: '>' не поддерживается между строками и целыми числами
    print('успех')
if [5, 6] > 5:      # Ошибка: '>' не поддерживается между списками и целыми числами
    print('успех')
if '6' != 5:        # А вот оператор неравенство допустим и нормально отрабатывает
    print('успех')