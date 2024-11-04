import inquirer

data = []

queries = {
    "hold": """UPDATE `logicbroker-fulfillment`.order
SET status = 'hold'
WHERE AgreementId IN (
    {data}
)
AND status = 'signed';""",
    "release": """UPDATE `logicbroker-fulfillment`.order
SET status = 'signed'
WHERE AgreementId IN (
    {data}
)
AND status = 'hold';""",
    "view": """SELECT 
AgreementId, status, CONVERT_TZ(OrderDate, 'UTC', 'America/New_York') AS OrderDate_EST, CONVERT_TZ(DatePoSubmitted, 'UTC', 'America/New_York') AS DatePoSubmitted_EST, CONCAT('https://calypso.flexshopper.com/orders/', AgreementId) as Calypso_Order
FROM `logicbroker-fulfillment`.order where isTest=0
and AgreementId IN (
    {data}
)
;""",
}


def get_values() -> list[str]:
    with open("./risk-values.txt", "r") as f:
        lines = f.readlines()
    return lines


def make_list_from_calypso(data: list[str]) -> list[str]:
    return [
        item.strip("https://calypso.flexshopper.com/order/").strip("\n")
        for item in data
    ]


def make_list_from_ids(data: list[str]) -> list[str]:
    return [item.strip("\n") for item in data]


def write_query_to_file(query: str, select_query: str) -> None:
    with open("./output.txt", "w") as f:
        f.write(query)
        f.write("\n\n")
        f.write(select_query)


def generate_query(data: list[str], action: str) -> str:
    formatted_data = ",\n    ".join(f"'{item}'" for item in data)
    return queries[action].format(data=formatted_data)


def main() -> None:
    try:
        # Use inquirer to select format
        format_choice = inquirer.list_input(
            "Select the format of ids provided",
            choices=["Calypso links", "ID values"],
        )

        # Process data based on selected format
        data = get_values()
        data = (
            make_list_from_calypso(data)
            if format_choice == "Calypso links"
            else make_list_from_ids(data)
        )

        # Use inquirer to select query action
        action_choice = inquirer.list_input(
            "Select the query action:", choices=["hold", "release"]
        )

        # Generate the query and write it to the output file
        query = generate_query(data, action_choice)
        select_query = generate_query(data, "view")
        write_query_to_file(query, select_query)

        print("Generated Query written to output.txt")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
