import os


def print_subdirectories(directory_name):
    for filename in os.listdir(directory_name):
        path = os.path.join(directory_name, filename)
        if os.path.isdir(path):
            print(path)
            print_subdirectories(path)
