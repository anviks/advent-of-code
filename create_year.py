import os

for i in range(2015, 2022):
    os.mkdir(str(i))
    for x in range(1, 26):
        os.mkdir(f"{i}/day_{x}")
        with open(f"{i}/day_{x}/data.txt", "a") as a, open(f"{i}/day_{x}/solution.py", "a") as b, open(
                f"{i}/day_{x}/task_description.txt", "a") as c:
            pass
