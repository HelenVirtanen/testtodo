import requests
import allure 


@allure.id("SKYPRO-4")
@allure.story("Удаление задачи")
@allure.feature("DELETE")
@allure.title("Удаление одной задачи")
def test_delete():
    with allure.step("Создать задачу с названием и статусом Не выполнено"):
        body = {"title":"generated","completed":False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    with allure.step("Получить id созданной задачи"):
        id = response.json()["id"]
    
    with allure.step("Удалить созданную задачу по указанному id"):
        response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    
    with allure.step("Статус код запроса на удаление равен 200"):
        assert response.status_code == 200
        
