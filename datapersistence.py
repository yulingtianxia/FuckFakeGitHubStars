import os.path
import json

global REPOSITORY_STARGAZERS
REPOSITORY_STARGAZERS = {}
global USER_STAR_REPOSITORIES
USER_STAR_REPOSITORIES = {}
global NODE_ID_CONTENT
NODE_ID_CONTENT = {}
global BLACK_LIST
BLACK_LIST = []


def create_file_if_not_exist(dir_path, file_name):
    file_path = dir_path + file_name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            print('create file:' + file_path)


def init_data_file():
    dir_path = 'data/'
    create_file_if_not_exist(dir_path, 'REPOSITORY_STARGAZERS.json')
    create_file_if_not_exist(dir_path, 'USER_STAR_REPOSITORIES.json')
    create_file_if_not_exist(dir_path, 'NODE_ID_CONTENT.json')
    create_file_if_not_exist(dir_path, 'BLACK_LIST.json')


def save_data():
    init_data_file()
    dir_path = 'data/'
    with open(dir_path + 'REPOSITORY_STARGAZERS.json', 'w') as f:
        json.dump(REPOSITORY_STARGAZERS, f)
    with open(dir_path + 'USER_STAR_REPOSITORIES.json', 'w') as f:
        json.dump(USER_STAR_REPOSITORIES, f)
    with open(dir_path + 'NODE_ID_CONTENT.json', 'w') as f:
        json.dump(NODE_ID_CONTENT, f)
    with open(dir_path + 'BLACK_LIST.json', 'w') as f:
        json.dump(BLACK_LIST, f)


def load_data():
    dir_path = 'data/'
    global REPOSITORY_STARGAZERS
    global USER_STAR_REPOSITORIES
    global NODE_ID_CONTENT
    global BLACK_LIST
    if os.path.exists(dir_path + 'REPOSITORY_STARGAZERS.json'):
        with open(dir_path + 'REPOSITORY_STARGAZERS.json', 'r') as f:
            REPOSITORY_STARGAZERS = json.load(f)
    if os.path.exists(dir_path + 'USER_STAR_REPOSITORIES.json'):
        with open(dir_path + 'USER_STAR_REPOSITORIES.json', 'r') as f:
            USER_STAR_REPOSITORIES = json.load(f)
    if os.path.exists(dir_path + 'NODE_ID_CONTENT.json'):
        with open(dir_path + 'NODE_ID_CONTENT.json', 'r') as f:
            NODE_ID_CONTENT = json.load(f)
    if os.path.exists(dir_path + 'BLACK_LIST.json'):
        with open(dir_path + 'BLACK_LIST.json', 'r') as f:
            BLACK_LIST = json.load(f)
