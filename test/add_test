import requests
import allure


@allure.id("SKYPRO-1")
@allure.story("Добавление задачи")
@allure.feature("POST")
@allure.title("Добавление задачи с названием и статусом 'не выполнено'")
def test_add():
    with allure.step("Создать задачу с названием и статусом Не выполнено"):
        body = {"title":"новая задача","completed":False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        response_body = response.json()
    
    with allure.step("Проверить статус код создания задачи"):
        assert response.status_code == 200

    with allure.step("Проверть что статус выполнения равен None"):
        assert response_body['completed'] == None
