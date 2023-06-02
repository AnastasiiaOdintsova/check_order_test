# Анастасия Одинцова, 5-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data
def create_order(): # создание заказа и получение трек-номера
    current_order = data.order_body.copy()
    order_response = sender_stand_request.post_new_order(current_order)
    return order_response.json()["track"]

def test_kod_positive(): # получение заказа по треку и проверка, что код ответа 200
    track_number = create_order()
    track_response = sender_stand_request.get_order(track_number)
    assert track_response.status_code == 200
