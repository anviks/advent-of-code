import subprocess
from pathlib import Path

for solution_file in Path('.').rglob('solution.py'):
    print(f"Running: {solution_file}")
    subprocess.run(["python", 'solution.py'], check=False, cwd=solution_file.parent)
