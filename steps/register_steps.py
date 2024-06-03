from endpoints.base_endpoint import ApiClient
from endpoints.dto_user import RegisterBody
from endpoints.dto_body_email import RegisterNoEmail

from allure import step


class RegisterSteps:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
        self.register_url = '/register'

    @step('регистрация пользователя')
    def user_register(self):
        return self.api_client.post(route='/register', json=RegisterBody.user())

    @step('Регистрация без email')
    def register_without_email(self):
        return self.api_client.post(route='/register', json=RegisterNoEmail.user_no_email())





