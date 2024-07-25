import requests
import allure
from data import Url
from helpers import *
from data import Answers

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title('Проверка создать курьера')
    def test_create_courier(self):
        login, password, first_name=generate_data_login()
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 201
        assert Answers.CREATE_COURIER == r.text
        delete_courier(login, password)

    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_both_same_couriers(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 409
        assert  Answers.CREATE_SAME_COURIER == r.text

    @allure.title('Проверка создать курьера без логина и пароля')
    def test_create_courier_without_login_password(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {
            'login': '',
            'password': '',
            'firstname': first_name
        }
        r = requests.post(f"{Url.create_courier_url}", data=payload)
        assert r.status_code == 400
        assert Answers.CREATE_COURIER_WITHOUT_DATA == r.text
