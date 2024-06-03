from endpoints.base_endpoint import ApiClient
from endpoints.dto_body_login import RegisterNoLogin

from allure import step


class LoginSteps:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
        self.register_url = '/login'

    @step('Регистрация без пароля')
    def register_unsuccessful_login(self):
        return self.api_client.post(route='/login', json=RegisterNoLogin.user_no_login())
