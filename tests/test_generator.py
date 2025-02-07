import pytest

from conftest import GenerateTestData


class TestGenerator:
    def __init__(self):
        self._generator = GenerateTestData()

    def test_email_generator(self):
        assert self._generator.generate_email() == f'Andrey_Busyrev_18_{str(self._generator._random_number)}@yandex.ru'
