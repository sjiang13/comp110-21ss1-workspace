"""Data utility functions."""
from csv import DictReader

def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    table: list[dict[str, str]] = []
    for row in csv_reader:
        table.append(row)
    return table

def column_values(table: list[dict[str,str]], column: str) -> list[str]: 
    """Return a column's values."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Convert a table of rows to a table of columns."""
    result: dict[str, list[str]] = {}
    keys = table[0].keys()
    for key in keys:
        # print(f"The key is {key}")
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Get first n rows."""
    result: dict[str, list[str]] = {}
    for key in table:
        result[key] = table[key][:rows]
    return result


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Select a subset of columns."""
    result: dict[str, list[str]] = {}
    for col_name in cols:
        result[col_name] = table[col_name]
    return result


table = read_csv_rows("data/weather.csv")
# print(table)
column_oriented = columnar(table)
print(head(column_oriented, 2))
