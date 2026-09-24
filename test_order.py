# Екатерина Данилова, 1-я когорта — Финальный проект. Инженер по тестированию плюс
import os
from datetime import date, timedelta

import requests


BASE_URL = os.getenv(
    "BASE_URL",
    "https://7d9e2c35-455c-4ecf-975d-8f7883dc39c5.serverhub.praktikum-services.ru",
)


def test_create_order_and_get_it_by_track():
    order_data = {
        "firstName": "Тест",
        "lastName": "Клиент",
        "address": "Москва, тестовый адрес",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": (date.today() + timedelta(days=1)).isoformat(),
        "comment": "Автотест",
        "color": ["BLACK"],
    }

    create_response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_data,
        timeout=10,
    )

    assert create_response.status_code == 201, (
        f"Заказ не создался: {create_response.status_code}, "
        f"{create_response.text}"
    )

    track = create_response.json().get("track")
    assert track, "В ответе на создание заказа отсутствует трек"

    get_response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track},
        timeout=10,
    )

    assert get_response.status_code == 200, (
        f"Заказ по треку {track} не найден: "
        f"{get_response.status_code}, {get_response.text}"
    )