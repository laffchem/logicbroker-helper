# This is to help with pushing the links to an array ingestible by SQL.


def get_values() -> list[str]:
    with open("./risk-values.txt", "r") as f:
        lines = f.readlines()
    return lines


def make_list_from_calypso(data: list[str]) -> list[str]:
    data = [
        item.strip("https://calypso.flexshopper.com/order/").strip("\n")
        for item in data
    ]
    return data


def make_list_from_ids(data: list[str]) -> list[str]:
    data = [item.strip("\n") for item in data]
    return data


def write_to_file(data: list[str], choice: str) -> None:
    if choice == "1":
        with open("./output.txt", "w") as f:
            for item in data:
                if data.index(item) == len(data) - 1:
                    f.write(f"'{item}'\n")
                else:
                    f.write(f"'{item}',\n")
    if choice == "2":
        with open("./output.txt", "w") as f:
            for item in data:
                if data.index(item) == len(data) - 1:
                    f.write(f"'{item}'\n")
                else:
                    f.write(f"'{item}',\n")


def main() -> None:
    while True:
        try:
            choice = input(
                "Please enter the format you need an array from\n1: for calypso links\n2: for id values\n"
            )
            if choice not in ["1", "2"]:
                raise ValueError("Please enter a valid choice")
            elif choice == "1":
                data = get_values()
                data = make_list_from_calypso(data)
                write_to_file(data, choice)
                break
            elif choice == "2":
                data = get_values()
                data = make_list_from_ids(data)
                write_to_file(data, choice)
                break
        except Exception as e:
            print(e)
    print(data)


if __name__ == "__main__":
    main()
