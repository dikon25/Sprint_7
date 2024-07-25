import pytest
import requests
import json
from data import *
import allure

@allure.feature("Создание заказа")
class TestOrder:
    @pytest.mark.parametrize('color',Order.scooter_colors)
    @allure.title('Проверка создания заказа с выбором разных цветов самоката')
    def test_create_order_random_color(self,color):
        payload = Order.order_body
        payload['color'] = color
        r = requests.post(Url.create_order_url, data=json.dumps(payload))
        assert r.status_code == 201
        assert Answers.TRACK_ORDER in r.text

