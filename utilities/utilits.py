import datetime
import allure


@allure.step("Получаем завтрашнюю дату")
def get_tomorrow_day():
    "Возвращяет завтрашную дату"
    return str((datetime.date.today() + datetime.timedelta(days=1)
                ).strftime("%d.%m.%Y"))
