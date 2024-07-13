import requests
import allure


@allure.id("SKYPRO-3")
@allure.story("Получение списка задач")
@allure.feature("GET")
@allure.title("Получение списка всех задач")
def test_get():
    with allure.step("Отправить запрос GET на получение списка задач"):
        response = requests.get("https://todo-app-sky.herokuapp.com/")
    
    with allure.step("Статус код запроса равен 200"):
        assert response.status_code == 200

    with allure.step("Тип данных ответа не равен list"):
        assert type(response.json()) is list
