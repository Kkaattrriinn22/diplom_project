import os

import requests


BASE_URL = os.getenv(
    "BASE_URL",
    "https://8719f17c-31d3-4cd2-9ab5-430b83800d6e.serverhub.praktikum-services.ru",
).rstrip("/")


def create_order(order_data):
    """Отправляет запрос на создание заказа."""
    return requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_data,
        timeout=10,
    )


def get_order_by_track(track):
    """Запрашивает заказ по его трек-номеру."""
    return requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track},
        timeout=10,
    )