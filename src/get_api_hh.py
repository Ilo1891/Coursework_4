import json

import requests

from src.abstract_api_hh import ABCApiHH


class HHApi(ABCApiHH):

    def __init__(self):
        self.all_vacancy = []

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self, name_vacancy: str) -> None | str:
        """Получаем игформацию о вакансиях"""

        if name_vacancy.isalpha():
            keys_response = {'text': f'NAME:{name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', params=keys_response)
            self.all_vacancy = json.loads(info.text)['items']
        else:
            return "Vacancy not found"
