import json

def add_to_json(filename, new_data):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(new_data)

    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    # Sample Json data
    # json_data = [
    #     {
    #         "name": "Ram",
    #         "age": 30
    #     },
    #     {
    #         "name": "Sita",
    #         "age": 25
    #     }
    # ]

    # Example usage to add a new entry
    filename = "file_IO/data.json"
    new_entry = {"name": "Hanuman", "age": 35}
    add_to_json(filename, new_entry)
    print(f"New entry added to {filename}.")

    # Verify the updated JSON data
    with open(filename, 'r') as file:
        updated_data = json.load(file)
    print(updated_data)
