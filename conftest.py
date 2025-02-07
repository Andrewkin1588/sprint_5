import random
from faker import Faker

r = random.Random()
fake_pass = Faker()


class GenerateTestData:
    def __init__(self):
        self._random_number = r.randint(100, 999)
        self._password_positive = fake_pass.password(length=6)
        self._password_negative_for_unit = fake_pass.password(length=5)

    def generate_email(self):
        return f'Andrey_Busyrev_18_{str(self._random_number)}@yandex.ru'

    def generate_password(self):
        return self._password_positive

    def generate_password_negative(self):
        return self._password_negative_for_unit
