import sender_stand_request
import requests
import configuration
import data

post_order_response = sender_stand_request.post_new_order(data.order_body)

# Герман Корнилков, 41-я когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order_by_number():
    get_order_response = sender_stand_request.get_order()
    assert get_order_response.status_code == 200






