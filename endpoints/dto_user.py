class RegisterBody:
    email = "eve.holt@reqres.in"
    password = "pistol"

    @classmethod
    def user(cls):
        return {"email": cls.email, "password": cls.password}


