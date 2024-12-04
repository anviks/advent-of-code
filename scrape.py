import os
import re

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from html2text import html2text
from utils_anviks import b64decode
from datetime import datetime as dt

load_dotenv()

LOGIN_URL = 'https://github.com/session'
EMAIL = os.getenv('EMAIL')


def get_int_input(prompt: str, default: int) -> int:
    while True:
        try:
            return int(input(prompt) or default)
        except ValueError:
            print('Invalid input. Please enter a number.')


def get_bool_input(prompt: str) -> bool:
    while True:
        answer = input(prompt).lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        print('Invalid input. Please enter y/yes or n/no.')


def create_files(*, overwrite_solution: bool):
    for year in range(start_year, start_year + years_count):
        for day in range(start_day, start_day + days_count):
            day_folder = f"{year}/day_{day}"
            data_file = day_folder + "/data.txt"
            example_file = day_folder + "/example.txt"
            solution_file = day_folder + "/solution.py"
            template_file = "template.txt"

            os.makedirs(day_folder, exist_ok=True)

            # Ensure that the files exist without overwriting them.
            with open(data_file, 'a'), open(solution_file, 'a'), open(example_file, 'a'):
                pass

            if overwrite_solution:
                with open(template_file, 'r') as template, open(solution_file, 'w') as solution:
                    solution.write(template.read())


def get_input_data():
    session = requests.Session()
    session.headers['User-Agent'] = f'Private non-automated script by {EMAIL}'
    req = session.get(LOGIN_URL).text
    html = BeautifulSoup(req, features='html.parser')
    token = html.find('input', {'name': 'authenticity_token'}).attrs['value']

    payload = {
        'login': EMAIL,
        'password': b64decode(os.getenv('PASSWORD'), 20),
        'authenticity_token': token
    }

    # POST request to the login page
    response = session.post(LOGIN_URL, data=payload)
    response.raise_for_status()

    # AOC auth page.
    session.get('https://adventofcode.com/auth/github')

    for year in range(start_year, start_year + years_count):
        for day in range(start_day, start_day + days_count):
            dir_ = f'{year}/day_{day}/'

            personal_data = session.get(f'https://adventofcode.com/{year}/day/{day}/input')
            task_description = session.get(f'https://adventofcode.com/{year}/day/{day}')

            with open(dir_ + 'data.txt', 'w') as f:
                f.write(personal_data.text.removesuffix('\n'))

            pretty_description = html2text(task_description.text)

            # Replace homepage link with a link to current day's task.
            pretty_description = re.sub(r'(?<=# \[Advent of Code]\()/(?=\))',
                                        f'https://adventofcode.com/{year}/day/{day}',
                                        pretty_description)

            # Replace root-relative links with absolute links.
            pretty_description = re.sub(r'(\[.*]\()(/.*\))',
                                        r'\1https://adventofcode.com\2',
                                        pretty_description)

            # Replace relative input link with absolute link.
            pretty_description = re.sub(r'(\[get your puzzle input]\()(\d{1,2}/input\))',
                                        fr'\1https://adventofcode.com/{year}/day/\2',
                                        pretty_description)

            with open(dir_ + 'task_description.md', 'w', encoding='utf-8') as f:
                f.write(pretty_description)

    session.close()


now = dt.now()
day_default = now.day if now.month == 12 and now.day <= 25 else -1

start_year = get_int_input('Start year: ', now.year)
years_count = get_int_input('Years count: ', 1)
start_day = get_int_input('Start day: ', day_default)
days_count = get_int_input('Days count: ', 1)

if start_day == -1:
    raise ValueError('Invalid day.')

create_files(overwrite_solution=get_bool_input('Do you want to overwrite the solution files? (y/n): '))
if get_bool_input('Do you want to fetch the input data? (y/n): '):
    get_input_data()
