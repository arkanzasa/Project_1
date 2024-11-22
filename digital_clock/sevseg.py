"""
Модуль sevseg.

Отображает числа на семи-сегментном дисплее.
Источники:
- Основы работы с семи-сегментными дисплеями: из книги "Python for Kids", проект #64, Al Sweigart (https://inventwithpython.com/).
"""

def get_sevseg_str(value, min_width=0):
    """
    Возвращает строку, представляющую значение в формате семи-сегментного дисплея.
    
    Аргументы:
    - value: число или строка для отображения.
    - min_width: минимальная ширина строки, дополненная нулями.

    Возвращает:
    - Строку, содержащую три строки (верхняя, средняя, нижняя) для семи-сегментного отображения.
    """
    # Конвертируем значение в строку.
    value = str(value).zfill(min_width)

    rows = ['', '', '']
    for i, char in enumerate(value):
        if char == '.':  # Десятичная точка.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
        elif char == '-':  # Минус.
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif char == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif char == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif char == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif char == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif char == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif char == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif char == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif char == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif char == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif char == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        elif char == '°':  # Символ градуса.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '    '
        elif char == 'C':  # Символ "C" для Цельсия.
            rows[0] += ' __ '
            rows[1] += '|   '
            rows[2] += '|__ '

        # Пробел между символами.
        if i != len(value) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)
