import json
import re

import requests
from bs4 import BeautifulSoup
from html2text import html2text
from utils_anviks import b64decode

login_url = "https://github.com/session"
session = requests.Session()
session.headers["User-Agent"] = "Private non-automated script by andreasviks0@gmail.com"
req = session.get(login_url).text
html = BeautifulSoup(req, features="lxml")
token = html.find("input", {"name": "authenticity_token"}).attrs['value']

with open("login.json") as f:
    creds: dict = json.load(f)

payload = {
    "login": creds.get("email"),
    "password": b64decode(creds.get("password"), 20),
    "authenticity_token": token
}

# POST request to the login page
response = session.post(login_url, data=payload)
print(response.status_code)

# AOC auth page.
session.get("https://adventofcode.com/auth/github")

for year in range(2023, 2024):
    for day in range(16, 24):
        dir_ = f"{year}/day_{day}/"

        personal_data = session.get(f"https://adventofcode.com/{year}/day/{day}/input")
        task_description = session.get(f"https://adventofcode.com/{year}/day/{day}")

        with open(dir_ + "data.txt", "w") as f:
            f.write(personal_data.text.removesuffix("\n"))

        pretty_description = html2text(task_description.text)

        # Replace homepage link with a link to current day's task.
        pretty_description = re.sub(r"(?<=# \[Advent of Code]\()/(?=\))",
                                    f"https://adventofcode.com/{year}/day/{day}",
                                    pretty_description)

        # Replace root-relative links with absolute links.
        pretty_description = re.sub(r"(\[.*]\()(/.*\))",
                                    r"\1https://adventofcode.com\2",
                                    pretty_description)

        # Replace relative input link with absolute link.
        pretty_description = re.sub(r"(\[get your puzzle input]\()(\d{1,2}/input\))",
                                    fr"\1https://adventofcode.com/{year}/day/\2",
                                    pretty_description)

        with open(dir_ + "task_description.md", "w", encoding='utf-8') as f:
            f.write(pretty_description)

session.close()
