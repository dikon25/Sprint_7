from helpers import *
import allure
from data import *

@allure.feature("Авторизация курьера")
class TestCourierLogin:
    @allure.title('Проверка авторизациии курьера с валидными значениями')
    def test_courier_login(self, create_courier):
        login=create_courier
        payload = {
            'login': login[0],
            'password': login[1],
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code==200
        assert Answers.COURIER_LOGIN in  r.text

    @allure.title('Проверка авторизациии курьера без логина')
    def test_courier_login_without_log(self,create_courier):
        login=create_courier
        payload = {
            'login': '',
            'password': login[1],
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code==400
        assert Answers.COURIER_LOGIN_WITHOUT_LOG ==  r.text

    @allure.title('Проверка авторизациии курьера без пароля')
    def test_courier_login_without_pass(self, create_courier):
        login = create_courier
        payload = {
            'login': login[0],
            'password': '',
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code == 400
        assert Answers.COURIER_LOGIN_WITHOUT_PASS == r.text

    @allure.title('Проверка авторизациии курьера с неверным паролем')
    def test_courier_login_with_err_pass(self, create_courier):
        login = create_courier
        payload = {
            'login': login[0],
            'password': '123456',
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code == 404
        assert Answers.COURIER_LOGIN_ERR_PASS == r.text

    @allure.title('Проверка авторизациии курьера с неверным логином')
    def test_courier_login_with_err_Log(self, create_courier):
        login = create_courier
        payload = {
            'login': 'Sam',
            'password': login[1],
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code == 404
        assert Answers.COURIER_LOGIN_ERR_LOG == r.text

    @allure.title('Проверка авторизациии несуществующего курьера')
    def test_courier_login_nonexistent(self, create_courier):
        login = create_courier
        payload = {
            'login': 'Sam',
            'password': '12345',
        }
        r = requests.post(f"{Url.login_url}", data=payload)

        assert r.status_code == 404
        assert Answers.COURIER_LOGIN_NONEXISTENT == r.text


