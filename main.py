from src.get_api_hh import HHApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy

response = HHApi()
file_json = JsonSaver()

while True:
    user_vacancy: str = input("Text name vacancy for search:\n")
    user_city: str = input("Text city in where you want to find vacancies:\n")
    if isinstance(user_city, str) and isinstance(user_vacancy, str):
        break
    print(f"Please, text alpha, not {user_city}")

while True:
    user_salary = input("Text min salary for search:\n")
    if user_salary.isdigit():
        break
    print(f"Please, text digit, not {user_salary}")

# Получаем вакансии
response.get_vacancy_from_api(user_vacancy)

# Сохраняем в фаиле JSON
file_json.save_file(response.all_vacancy)

# Открываем фаил JSON
file_vacancies = file_json.read_file()

# Показываем вакансии для пользователя
vacancy = Vacancy.get_vacancy_list(file_vacancies, user_city, int(user_salary))
sorted_vacancies = sorted(vacancy)

while True:
    count = input("How vacancies do you want to see:\n")
    if count.isdigit():
        break
    print(f"Please, text digit, not {count}")

print(*sorted_vacancies[:int(count)])
