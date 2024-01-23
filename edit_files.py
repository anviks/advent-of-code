"""Creates the folder structure for the advent of code solutions."""

import os

for year in range(2023, 2024):
    if not os.path.exists(str(year)):
        os.mkdir(str(year))
    for day in range(10, 26):
        day_folder = f"{year}/day_{day}"
        data_file = f"{day_folder}/data.txt"
        solution_file = f"{day_folder}/solution.py"
        template_file = "template.txt"

        if not os.path.exists(day_folder):
            os.mkdir(day_folder)

        with open(data_file, "a") as a, open(solution_file, "a") as b:
            pass
        with open(template_file) as template, open(solution_file, "w") as solution:
            solution.write(template.read())
