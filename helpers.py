import requests
import random
import string
from data import Url
import allure

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
#
@staticmethod

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
def generate_data_login():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name



def generate_data_payload():
    login, password, first_name = generate_data_login()
    payload = {
        "login": login,
        "password": password,
        "firstname": first_name
    }
    return payload


@allure.step("Регистрируем нового курьера  возвращаем логин и пароль")
def register_new_courier_and_return_login_password():
    login_pass = []
    payload = generate_data_payload()
    response = requests.post(Url.create_courier_url, data=payload)
    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstname'])
    return login_pass


@allure.step("Удаляем курьера")
def delete_courier(login, password):
    response_post = requests.post(Url.login_url, data={
        'login': login,
        'password': password
    })
    courier_id = response_post.json()['id']
    requests.delete(f'{Url.delete_courier_url}{courier_id}')
