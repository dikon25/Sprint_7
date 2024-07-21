class Url:
    main_paige= 'http://qa-scooter.praktikum-services.ru'
    create_courier_url='http://qa-scooter.praktikum-services.ru/api/v1/courier/'
    login_url ='http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    create_order_url ='http://qa-scooter.praktikum-services.ru/api/v1/orders'
    delete_courier_url='http://qa-scooter.praktikum-services.ru/api/v1/courier'
    all_orders='http://qa-scooter.praktikum-services.ru/api/v1/orders'
    track_order='http://qa-scooter.praktikum-services.ru/api/v1/orders/track'


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