import csv
import json
from typing import List
INPUT_FILE = "output.csv"


def csv_to_list_dict(INPUT_FILE, delimiter = ',', new_line ='\n') -> List[dict]:
    with open(INPUT_FILE) as file:
        lines = [line for line in csv.DictReader(file)]
    return lines


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
