import os


def print_subdirectories(directory_name):

    for filename in os.listdir(directory_name):
        if os.path.isdir(filename):
            path = os.path.join(directory_name, filename)
            print(path)

            for filename2 in os.listdir(path):
                path2 = os.path.join(path, filename2)
                if os.path.isdir(path2):
                    print(path2)
