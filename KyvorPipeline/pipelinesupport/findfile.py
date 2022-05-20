import os
import fnmatch


def filepath(path, file_keyword):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.xlsx'):
            matches.append(os.path.join(root, filename))
    return_file = ""
    for match in matches:
        if file_keyword in match:
            return_file = match
            break

    return return_file
