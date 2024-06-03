import requests
from allure import step


class ApiClient:  # Not in the fixtures for convenient hints in the steps!
    def __init__(self):
        self.url = 'https://reqres.in/api'

    @step('POST-запрос к серверу')
    def post(self, route=None, data=None, headers=None, params=None, json=None, files=None):
        return requests.post(f'{self.url}{route}', data=data, json=json, headers=headers, params=params, files=files)

    @step('GET-запрос к серверу')
    def get(self, route=None, headers=None, params=None):
        return requests.get(f'{self.url}{route}', headers=headers, params=params)

    @step('PUT-запрос к серверу')
    def put(self, route=None, data=None, headers=None, params=None, json=None):
        return requests.put(f'{self.url}{route}', data=data, headers=headers, params=params, json=json)

    @step('PATCH-запрос к серверу')
    def patch(self, route=None, headers=None, params=None):
        return requests.patch(f'{self.url}{route}', headers=headers, params=params)

    @step('DELETE-запрос к серверу')
    def delete(self, route=None, headers=None, params=None):
        return requests.delete(f'{self.url}{route}', headers=headers, params=params)





