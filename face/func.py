import os


def countFiles(source_path):
    count = 0
    for path in os.listdir(source_path):
        if os.path.isfile(os.path.join(source_path, path)):
            count += 1
    return count