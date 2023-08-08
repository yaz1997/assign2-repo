def search_log(log_file, search_keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")

if __name__ == "__main__":
    log_file = "file_IO/example.log"
    search_keyword = "ERROR"
    search_log(log_file, search_keyword)
