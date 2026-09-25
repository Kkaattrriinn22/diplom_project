# Екатерина Данилова, 47-я когорта — Финальный проект. Инженер по тестированию плюс
from data import get_order_data
from helpers import create_order, get_order_by_track


def test_create_order_and_get_it_by_track():
    # Создаём заказ и проверяем, что API вернул успешный код.
    create_response = create_order(get_order_data())
    assert create_response.status_code == 201, (
        f"Заказ не создался: {create_response.status_code}, "
        f"{create_response.text}"
    )

    # Сохраняем трек из ответа, чтобы запросить заказ по нему.
    track = create_response.json().get("track")
    assert track, "В ответе на создание заказа отсутствует трек"

    # Получаем созданный заказ по треку и проверяем код ответа.
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, (
        f"Заказ по треку {track} не найден: "
        f"{get_response.status_code}, {get_response.text}"
    )