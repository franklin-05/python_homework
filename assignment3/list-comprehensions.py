import csv

with open("../csv/employees.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

full_names = [f"{row[0]} {row[1]}" for row in data[1:]]
print("All Names:", full_names)

names_with_e = [name for name in full_names if "e" in name.lower()]
print("Names with 'e':", names_with_e)