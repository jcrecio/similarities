import sys
import csv

import pandas as pd
from utils import compute_method_similarity


class MethodData:
    def __init__(self, class_name, old_method_name, new_method_name, tokens):
        self.class_name = class_name
        self.old_method_name = old_method_name
        self.new_method_name = new_method_name
        self.tokens = tokens

        self.similarity = 0


df = pd.read_csv(sys.argv[1])

method_data_collection = []
for index, row in df.iterrows():
    method_data = MethodData(
        row["class"], row["oldMethodName"], row["newMethodName"], row["tokens"]
    )
    method_data.similarity = compute_method_similarity(
        method_data.old_method_name, method_data.new_method_name
    )
    method_data_collection.append(method_data)


header = ["class", "oldMethodName", "newMethodName", "tokens", "similarity"]

with open(sys.argv[2], "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for method_data in method_data_collection:
        writer.writerow(
            {
                "class": method_data.class_name,
                "oldMethodName": method_data.old_method_name,
                "newMethodName": method_data.new_method_name,
                "tokens": method_data.tokens,
                "similarity": method_data.similarity,
            }
        )
