class RegisterNoLogin:
    email = "peter@klaven"

    @classmethod
    def user_no_login(cls):
        return {"email": cls.email}
