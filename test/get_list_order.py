import requests
import allure
from data import *

@allure.feature("Список заказов")
class TestOrderList:
    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order_list(self):
        r=requests.get(Url.all_orders)
        assert r.status_code==200
        assert Answers.TRACK_ORDER in r.text
