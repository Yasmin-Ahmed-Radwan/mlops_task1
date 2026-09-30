import csv
import subprocess
from itertools import islice

result = subprocess.run(
    ["osascript", "-e",
     'POSIX path of (choose file with prompt "Select a CSV file")'],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    file_path = result.stdout.strip()

    with open(file_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        print("Headers:", next(reader, []))

        for row in islice(reader, 3):
            print(row)
else:
    print("No file selected.")
