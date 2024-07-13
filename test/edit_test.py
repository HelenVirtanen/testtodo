import requests
import allure 


@allure.id("SKYPRO-2")
@allure.story("Изменение задачи")
@allure.feature("UPDATE")
@allure.title("Изменение названия задачи")
def edit_task_test():
    with allure.step("Создать задачу с названием и статусом Не выполнено"):
        body = {"title":"generated","completed":False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        id = response.json()["id"]
    
    with allure.step("Изменить название в задаче"):
        body = {"title":"generated-1"}
        response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)

    with allure.step("Проверить, что статус код запроса равен 200"):
        assert response.status_code == 200
    
    with allure.step("Найти измененную задачу и проверить что статус код запроса равен 200"):
        response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
        assert response.status_code == 200
    
    with allure.step("Название задачи изменено"):
        assert response.json()['title']=="generated-1"
      
