import requests
import allure
from data import Url
from helpers import *
from operator import itemgetter

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title('Проверка создать курьера')
    def test_create_courier(self):
        reg_data= add_new_corier()
        login, password, first_name=itemgetter(0,1,2)(reg_data)
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 201
        assert '{"ok":true}' == r.text
        delete_courier(login, password)

    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_both_same_couriers(self):
        data=register_new_courier_and_return_login_password()
        login, password, first_name = itemgetter(0, 1, 2)(data)
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 409
        assert  '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}' == r.text

    @allure.title('Проверка создать курьера без логина и пароля')
    def test_create_courier_without_login_password(self):
        reg_data = add_new_corier()
        login, password, first_name = itemgetter(0, 1, 2)(reg_data)
        payload = {
            'login': '',
            'password': '',
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 400
        assert '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == r.text
