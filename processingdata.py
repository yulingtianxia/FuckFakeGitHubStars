import datapersistence as dp
import fetchdata as fd
import time

CLUSTER_SIMILARITY = 0.5


def calculate_similarity(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return len(set_a.intersection(set_b)) / len(set_a.union(set_b))


def cluster_data(data):
    nodes = data.keys()
    for node in nodes:
        dp.NODE_ID_CONTENT[node]['cluster'] = node
    for i, node_a in enumerate(nodes):
        for j, node_b in enumerate(nodes):
            if j <= i:
                continue
            if 'similarity' not in dp.NODE_ID_CONTENT[node_a]:
                dp.NODE_ID_CONTENT[node_a]['similarity'] = {}
            if 'similarity' not in dp.NODE_ID_CONTENT[node_b]:
                dp.NODE_ID_CONTENT[node_b]['similarity'] = {}
            if node_b not in dp.NODE_ID_CONTENT[node_a]['similarity']:
                similarity = calculate_similarity(data[node_a], data[node_b])
                dp.NODE_ID_CONTENT[node_a]['similarity'][node_b] = similarity
                dp.NODE_ID_CONTENT[node_b]['similarity'][node_a] = similarity
            else:
                similarity = dp.NODE_ID_CONTENT[node_a]['similarity'][node_b]
            if similarity >= CLUSTER_SIMILARITY:
                dp.NODE_ID_CONTENT[node_b]['cluster'] = dp.NODE_ID_CONTENT[node_a]['cluster']


def generate_blacklist():
    clusters = {}
    for node, content in dp.NODE_ID_CONTENT.items():
        if 'cluster' in content:
            if content['cluster'] not in clusters:
                clusters[content['cluster']] = []
            clusters[content['cluster']].append(node)

    log = ''
    for cluster_id, cluster_content in clusters.items():
        cluster_description = ''
        if 'login' in dp.NODE_ID_CONTENT[cluster_id]:
            if len(cluster_content) > 100:
                for node in cluster_content:
                    cluster_content_list = dp.USER_STAR_REPOSITORIES[node]
                    if len(cluster_content_list) < 100:
                        if node not in dp.BLACK_LIST:
                            dp.BLACK_LIST.append(node)
                        cluster_description += 'user login name: ' + \
                                               dp.NODE_ID_CONTENT[node]['login'] + \
                                               '; star num: ' + \
                                               format(len(cluster_content_list)) + \
                                               '\n'
                if len(cluster_description) > 0:
                    cluster_description += '===============================\n\n'
        log += cluster_description
    blacklist_set = set(dp.BLACK_LIST)
    for cluster_id, cluster_content in clusters.items():
        cluster_description = ''
        if 'owner' in dp.NODE_ID_CONTENT[cluster_id]:
            for node in cluster_content:
                cluster_content_list = dp.REPOSITORY_STARGAZERS[node]
                black_match_count = len(blacklist_set.intersection(set(cluster_content_list)))
                if black_match_count > 0:
                    black_percent = black_match_count / len(cluster_content_list)
                    dp.NODE_ID_CONTENT[node]['black_percent'] = black_percent
                    cluster_description += 'repo owner/name: ' + \
                                           dp.NODE_ID_CONTENT[node]['owner'] + \
                                           '/' + \
                                           dp.NODE_ID_CONTENT[node]['name'] + \
                                           '; stargazer num: ' + \
                                           format(len(cluster_content_list)) +\
                                           '; black percent:' + \
                                           format(black_percent) + \
                                           '\n'
            if len(cluster_description) > 0:
                cluster_description += '===============================\n\n'
        log += cluster_description
    dir_path = 'data/'
    with open(dir_path + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '_blacklist.log', 'wt') as f:
        f.write(log)


def search_blacklist():
    for user in dp.BLACK_LIST:
        fd.bfs_users_star_repos(user, 2)


if __name__ == '__main__':
    fd.load_token()
    dp.load_data()
    cluster_data(dp.USER_STAR_REPOSITORIES)
    cluster_data(dp.REPOSITORY_STARGAZERS)
    generate_blacklist()
    search_blacklist()
    dp.save_data()
