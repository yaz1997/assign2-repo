import csv

def filter_adults(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        adults = [row for row in reader if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(adults)

if __name__ == "__main__":
    input_file = "file_IO/data.csv"
    output_file = "file_IO/adults.csv"
    filter_adults(input_file, output_file)
    print(f"Filtered adults data written to {output_file}.")





