"""
Модуль weather.

Определяет местоположение пользователя и получает данные о погоде.
Источники:
- Местоположение пользователя через IP: http://ip-api.com/json/
- Погода Open-Meteo API: https://open-meteo.com/.
"""

import requests


def get_location():
    """
    Определяет местоположение пользователя через IP.

    Возвращает:
    - Город пользователя (строка).
    """
    try:
        response = requests.get("http://ip-api.com/json/")
        response.raise_for_status()
        data = response.json()
        return data.get("city", "Неизвестный город")
    except requests.RequestException as e:
        print("Не удалось определить местоположение:", e)
        return "Неизвестный город"


def get_weather():
    """
    Получает текущую температуру для местоположения пользователя.

    Функция создана при помощи ChatGPT
    """
    try:
        # Получаем широту и долготу пользователя.
        location_response = requests.get("http://ip-api.com/json/")
        location_response.raise_for_status()
        location_data = location_response.json()

        latitude = location_data.get("lat")
        longitude = location_data.get("lon")

        if latitude is None or longitude is None:
            return "Нет данных о погоде"

        # Получаем данные о погоде с помощью Open-Meteo API.
        weather_response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # Извлекаем текущую температуру.
        current_weather = weather_data.get("current_weather", {})
        temperature = current_weather.get("temperature")

        if temperature is not None:
            return f"{temperature}°C"
        else:
            return "Нет данных о погоде"

    except requests.RequestException as e:
        print("Не удалось получить данные о погоде:", e)
        return "Нет данных о погоде"
