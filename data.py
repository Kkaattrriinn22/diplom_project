from datetime import date, timedelta


def get_order_data():
    """Возвращает данные для создания тестового заказа."""
    return {
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