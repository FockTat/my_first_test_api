class RegisterNoEmail:
    password = "pistol"

    @classmethod
    def user_no_email(cls):
        return {"password": cls.password}