"""
Модуль clock.

Отображает текущее время в формате семи-сегментного дисплея.
Источники:
- Основы работы с цифровыми часами: из книги "Python for Kids", проект #19, Al Sweigart (https://inventwithpython.com/).
"""

import time
import logging
from sevseg import get_sevseg_str
from weather import get_location, get_weather


def configure_logging():
    """
    Настраивает уровень логирования из config.json.
    """
    import json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    level = getattr(logging, config.get("log_level", "INFO").upper(), logging.INFO)
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")


def run_clock():
    """
    Основной цикл часов.
    """
    configure_logging()
    logging.info("Запуск цифровых часов.")

    city = get_location()
    weather = get_weather()
    logging.info(f"Местоположение: {city}. Погода: {weather}.")

    try:
        while True:
            print("\n" * 50)  # Очищаем экран.
            current_time = time.localtime()
            hours = f"{current_time.tm_hour:02}"
            minutes = f"{current_time.tm_min:02}"
            seconds = f"{current_time.tm_sec:02}"

            # Получаем строки для отображения.
            h_segments = get_sevseg_str(hours)
            m_segments = get_sevseg_str(minutes)
            s_segments = get_sevseg_str(seconds)
            weather_segments = get_sevseg_str(weather)

            # Вывод часов.
            h_top, h_mid, h_bot = h_segments.splitlines()
            m_top, m_mid, m_bot = m_segments.splitlines()
            s_top, s_mid, s_bot = s_segments.splitlines()
            w_top, w_mid, w_bot = weather_segments.splitlines()

            print(h_top + "   " + m_top + "   " + s_top)
            print(h_mid + " * " + m_mid + " * " + s_mid)
            print(h_bot + " * " + m_bot + " * " + s_bot)
            print()
            print(w_top)
            print(w_mid)
            print(w_bot)
            print(f"Город: {city}")
            print("\nНажмите Ctrl+C для завершения программы.")

            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Программа завершена пользователем.")
        print("\nПрограмма завершена.")
