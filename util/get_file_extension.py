import os.path


def get_file_extension(match):
    path = match.group(4)

    extension = os.path.splitext(path)[1]

    return extension

