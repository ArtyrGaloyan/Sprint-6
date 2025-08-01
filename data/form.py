from ..utilities.utilits import get_tomorrow_day


class PageOneTestData:
    first_name = "Артур"
    last_name = "Галоян"
    address = "Москва"
    station = "Митино"
    phone = "+79625668543"


class PageTwoTestData:
    date = get_tomorrow_day()
    rend_day = 'семеро суток'
    color = 'чёрный жемчуг'
    comment = "Тестовый коммент"


class DataOrderForm:
    
    @staticmethod
    def get_data():
        return {
            'page_one': {
                "fname": PageOneTestData.first_name,
                "lname": PageOneTestData.last_name,
                "address": PageOneTestData.address,
                "metro": PageOneTestData.station,
                "phone": PageOneTestData.phone
            },
            'page_two': {
                "date": PageTwoTestData.date,
                "rend_day": PageTwoTestData.rend_day,
                "color": PageTwoTestData.color,
                "comment": PageTwoTestData.comment
            }
        }

    @staticmethod
    def get_new_data():
        return {
            'page_one': {
                "fname": "Артур",
                "lname": "Галоян",
                "address": "Москва, красная площадь",
                "metro": "Бибирево",
                "phone": "88549395734"
            },
            'page_two': {
                "date": PageTwoTestData.date,
                "rend_day": "трое суток",
                "color": "серая безысходность",
                "comment": PageTwoTestData.comment
            }
        }