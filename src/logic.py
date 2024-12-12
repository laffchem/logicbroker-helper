from config import queries
import os


def get_values(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


def make_list_from_calypso(data: list[str]) -> list[str]:
    return [
        item.strip("https://calypso.flexshopper.com/order/").strip("\n")
        for item in data
    ]


def make_list_from_ids(data: list[str]) -> list[str]:
    return [item.strip("\n") for item in data]


def write_query_to_file(query: str, select_query: str, output_file_path: str) -> None:
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, "w") as f:
        f.write(query)
        f.write("\n\n")
        f.write(select_query)


def generate_query(data: list[str], action: str) -> str:
    formatted_data = ",\n    ".join(f"'{item}'" for item in data)
    return queries[action].format(data=formatted_data)
