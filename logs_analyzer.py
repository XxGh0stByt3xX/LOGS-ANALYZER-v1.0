import os
import re

def accounts_searcher(starting_directory, url_to_search, output_file_name):
    results = []
    count = 0
    output_file_name = output_file_name + '.txt'

    with open(output_file_name, 'w') as out_file:
        for root, dirs, files in os.walk(starting_directory):
            if 'Passwords.txt' in files:
                file_path = os.path.join(root, 'Passwords.txt')
                try:
                    with open(file_path, 'r') as file:
                        file_content = file.read()
                except OSError as e:
                    print(f"Error opening file {file_path}: {e}")
                    continue

                try:
                    url_match = re.search(r'URL: ([^\n]+)', file_content)
                    usr_match = re.search(r'Username: ([^\n]+)', file_content)
                    pass_match = re.search(r'Password: ([^\n]+)', file_content)

                    if url_match and usr_match and pass_match:
                        url = url_match.group(1)
                        username = usr_match.group(1)
                        password = pass_match.group(1)

                        if url_to_search.lower() in url.lower():
                            result = {'path': root, 'usr': username, 'pass': password}
                            results.append(result)
                            out_file.write(f"Path: {result['path']}\n")
                            out_file.write(f"Username\\Email: {result['usr']}\n")
                            out_file.write(f"Password: {result['pass']}\n")
                            out_file.write("\n")
                            count += 1
                except OSError as e:
                    print(f"Error handling file {file_path}: {e}")
                except re.error as e:
                    print(f"Error in regex search in file {file_path}: {e}")

    absolute_output_path = os.path.abspath(output_file_name)
    print(str(count) + ' accounts found. Results written to file ' + str(absolute_output_path))
    return results


def main():
    print("=== LOGS ANALYZER v1.0 ===")
    print("Developed by Gh0stByt3\n")

    while True:
        choice = input("Enter 1 to start the analysis tool, or 0 to quit: ").strip()

        if choice == '1':
            starting_directory = input('Enter the directory path where your logs are located: ').strip()
            print(f"Entered path: {starting_directory}")

            if not os.path.isdir(starting_directory):
                print("The specified path is not a valid directory.")
                continue

            url_to_search = input('Enter the website or URL you are searching for (e.g., Amazon or https://amazon.com): ').strip()
            output_file_name = input('Enter the output file name (e.g., "Amazon"): ')
            accounts_searcher(starting_directory, url_to_search, output_file_name)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter either 1 or 0.")

if __name__ == "__main__":
    main()
