class Url:
    main_paige= 'http://qa-scooter.praktikum-services.ru'
    create_courier_url=f'{main_paige}/api/v1/courier'
    login_url =f'{main_paige}/api/v1/courier/login'
    create_order_url =f'{main_paige}/api/v1/orders'
    delete_courier_url=f'{main_paige}/api/v1/courier/'
    all_orders=f'{main_paige}/api/v1/orders'
    track_order=f'{main_paige}/api/v1/orders/track'


class Order:
        order_body = {
            "firstName": "Дмитрий",
            "lastName": "Дмитров",
            "address": "Московская набережная 25",
            "metroStation": 6,
            "phone": "+79770000025",
            "rentTime": 4,
            "deliveryDate": "2024-07-20",
            "comment": "Hello world",
            "color": [],
        }

        scooter_colors = ["[]", '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']
class Answers:
    CREATE_COURIER='{"ok":true}'
    CREATE_SAME_COURIER='{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    CREATE_COURIER_WITHOUT_DATA='{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    COURIER_LOGIN = "id"
    COURIER_LOGIN_WITHOUT_LOG='{"code":400,"message":"Недостаточно данных для входа"}'
    COURIER_LOGIN_WITHOUT_PASS='{"code":400,"message":"Недостаточно данных для входа"}'
    COURIER_LOGIN_ERR_PASS='{"code":404,"message":"Учетная запись не найдена"}'
    COURIER_LOGIN_ERR_LOG='{"code":404,"message":"Учетная запись не найдена"}'
    COURIER_LOGIN_NONEXISTENT='{"code":404,"message":"Учетная запись не найдена"}'
    TRACK_ORDER='"track"'


