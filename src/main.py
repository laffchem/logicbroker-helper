import os
import inquirer
from config import queries
from logic import *

data = []


def main() -> None:
    try:
        # Use inquirer to select format
        format_choice = inquirer.list_input(
            "Select the format of ids provided",
            choices=["Calypso links", "ID values"],
        )

        # Process data based on selected format
        input_file_path = os.path.join(os.path.dirname(__file__), "../input-values.txt")
        data = get_values(input_file_path)
        data = (
            make_list_from_calypso(data)
            if format_choice == "Calypso links"
            else make_list_from_ids(data)
        )

        # Use inquirer to select query action
        action_choice = inquirer.list_input(
            "Select the query action",
            choices=["hold", "release", "bb_release", "repeat_customer_release"],
        )

        # Generate the query and write it to the output file
        query = generate_query(data, action_choice)
        select_query = generate_query(data, "view")
        write_query_to_file(
            query,
            select_query,
            os.path.join(os.path.dirname(__file__), "../output.txt"),
        )

        print("Generated Query written to output.txt")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
