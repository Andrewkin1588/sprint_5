from helpers import GenerateTestData

generator = GenerateTestData()


class TestGenerator:

    def test_email_generator(self):
        assert generator.generate_email() == f'Andrey_Busyrev_18_{str(generator._random_number)}@yandex.ru'

    def test_len_password_generator_positive(self):
        assert len(generator.generate_password()) == 6

    def test_len_password_generator_negative(self):
        assert len(generator.generate_password_negative()) == 5
