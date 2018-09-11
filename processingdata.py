import json
import os


if __name__ == '__main__':
    node_id = 'MDEwOlJlcG9zaXRvcnkxMTc1MTM4NTI='
    global REPOSITORY_STARGAZERS
    dir_path = 'data/' + node_id
    file_path = dir_path + '/REPOSITORY_STARGAZERS.json'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(file_path, 'w') as f:
        print(f)
