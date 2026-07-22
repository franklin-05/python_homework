import csv
from datetime import datetime
import sys
import custom_module
# Task 2

def read_employees():
    employees_dict = {}
    rows_list = []

    try:
        with open("../csv/employees.csv", mode="r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row
                else:
                    rows_list.append(row)
                    
        employees_dict["rows"] = rows_list
        return employees_dict

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

employees = read_employees()

# Task 3
def column_index(header_name):
    return employees["fields"].index(header_name)

employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_number):
    fname_col = column_index("first_name")
    return employees["rows"][row_number][fname_col]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    lname_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[lname_col])
    return employees["rows"]

# Task 8
def employee_dict(row):
    emp_dict = {}
    for header, value in zip(employees["fields"], row):
        if header != "employee_id":
            emp_dict[header] = value
    return emp_dict

# Task 9
def all_employees_dict():
    all_emp = {}
    emp_col = column_index("employee_id")
    for row in employees["rows"]:
        emp_id = row[emp_col]
        all_emp[emp_id] = employee_dict(row)
    return all_emp
#Task 10 
import os
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
print(custom_module.secret)

# Task 12
def _read_csv(filepath):
    """Helper function to keep code DRY."""
    with open(filepath, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}


def read_minutes():
    m1 = _read_csv("../csv/minutes1.csv")
    m2 = _read_csv("../csv/minutes2.csv")
    return m1, m2


minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


#Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()

#Task 14
def create_minutes_list():
    raw_list = list(minutes_set)
    mapped_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            raw_list
        )
    )
    return mapped_list


minutes_list = create_minutes_list()
print("Minutes List:", minutes_list)

#Task 15 
def write_sorted_list():
    sorted_data = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            sorted_data
        )
    )
    with open("./minutes.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list


write_sorted_list()