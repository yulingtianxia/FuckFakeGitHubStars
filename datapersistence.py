import os.path
import json


def init():
    global REPOSITORY_STARGAZERS
    REPOSITORY_STARGAZERS = {}
    global USER_STAR_REPOSITORIES
    USER_STAR_REPOSITORIES = {}
    global NODE_ID_CONTENT
    NODE_ID_CONTENT = {}


def create_file_if_not_exist(dir_path, file_name):
    file_path = dir_path + file_name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            print('create file:' + file_path)


def init_data_file(node_id):
    dir_path = 'data/' + node_id + '/'
    create_file_if_not_exist(dir_path, 'REPOSITORY_STARGAZERS.json')
    create_file_if_not_exist(dir_path, 'USER_STAR_REPOSITORIES.json')
    create_file_if_not_exist(dir_path, 'NODE_ID_CONTENT.json')


def save_data(node_id):
    init_data_file(node_id)
    dir_path = 'data/' + node_id + '/'
    with open(dir_path + 'REPOSITORY_STARGAZERS.json', 'w') as f:
        json.dump(REPOSITORY_STARGAZERS, f)
    with open(dir_path + 'USER_STAR_REPOSITORIES.json', 'w') as f:
        json.dump(USER_STAR_REPOSITORIES, f)
    with open(dir_path + 'NODE_ID_CONTENT.json', 'w') as f:
        json.dump(NODE_ID_CONTENT, f)


def load_data(node_id):
    dir_path = 'data/' + node_id + '/'
    global REPOSITORY_STARGAZERS
    global USER_STAR_REPOSITORIES
    global NODE_ID_CONTENT
    if os.path.exists(dir_path + 'REPOSITORY_STARGAZERS.json'):
        with open(dir_path + 'REPOSITORY_STARGAZERS.json', 'r') as f:
            REPOSITORY_STARGAZERS = json.load(f)
    if os.path.exists(dir_path + 'REPOSITORY_STARGAZERS.json'):
        with open(dir_path + 'USER_STAR_REPOSITORIES.json', 'r') as f:
            USER_STAR_REPOSITORIES = json.load(f)
    if os.path.exists(dir_path + 'REPOSITORY_STARGAZERS.json'):
        with open(dir_path + 'NODE_ID_CONTENT.json', 'r') as f:
            NODE_ID_CONTENT = json.load(f)
