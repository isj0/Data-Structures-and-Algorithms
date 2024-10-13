import os


def print_subdirectories(directory_name):

    for filename in os.listdir(directory_name):
        if os.path.isdir(filename):
            path = os.path.join(directory_name, filename)
            print(path)
