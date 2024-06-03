def test_successful_register(register_steps):
    response = register_steps.user_register()
    assert response.ok
    assert response.json()['id'] == 4


def test_unsuccessful_email(register_steps):
    response = register_steps.register_without_email()
    assert response.status_code == 400
    assert response.json().get('error') == 'Missing email or username'


def test_unsuccessful_login(login_steps):
    response = login_steps.register_unsuccessful_login()
    assert response.status_code == 400
    assert response.json().get('error') == 'Missing password'


