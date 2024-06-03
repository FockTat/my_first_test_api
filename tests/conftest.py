from endpoints.base_endpoint import ApiClient
from steps.register_steps import RegisterSteps
from steps.login_steps import LoginSteps

import pytest


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def register_steps(api_client):
    return RegisterSteps(api_client)


@pytest.fixture
def login_steps(api_client):
    return LoginSteps(api_client)
