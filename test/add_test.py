import requests
import allure


@allure.id("SKYPRO-1")
@allure.story("Добавление задачи")
@allure.feature("POST")
@allure.title("Добавление задачи с названием и статусом 'не выполнено'")
def test_add():
    with allure.step("Создать задачу с названием и статусом Не выполнено"):
        body = {"title":"новая задача","completed":False}
        with allure.step("Вызвать api-метод для создания задачи"):
            response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
            response_body = response.json()
    
    with allure.step("Проверить, что статус-код создания задачи равен 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что статус выполнения задачи равен None"):
        assert response_body['completed'] == None
