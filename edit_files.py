"""Creates the folder structure for the advent of code solutions."""

import os

overwrite_solution = False

for year in range(2023, 2024):
    if not os.path.exists(str(year)):
        os.mkdir(str(year))
    for day in range(21, 25):
        day_folder = f"{year}/day_{day}"
        data_file = day_folder + "/data.txt"
        example_file = day_folder + "/example.txt"
        solution_file = day_folder + "/solution.py"
        template_file = "template.txt"

        if not os.path.exists(day_folder):
            os.mkdir(day_folder)

        # Ensure that the files exist without overwriting them.
        with open(data_file, 'a'), open(solution_file, 'a'), open(example_file, 'a'):
            pass

        if overwrite_solution:
            with open(template_file, 'r') as template, open(solution_file, 'w') as solution:
                solution.write(template.read())
