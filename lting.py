import os, sys


def get_files(path):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(f)
    return files


def main():
    path = input("Enter a directory path: ")
    if not os.path.exists(path):
        print("Path doesn't exist")
        sys.exit()
    files = get_files(path)
    print("Files:")
    for f in files:
        print(f)


main()


# ruff check lting.py-->it show your code error in terminal(gives linting suggestions)
# for correct/auto-format:black <your_file>.py
