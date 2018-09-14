import datapersistence as dp
import fetchdata as fd

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


if __name__ == '__main__':
    dp.load_data(fd.SEARCH_NODE_ID)
    cluster_data(dp.USER_STAR_REPOSITORIES)
    cluster_data(dp.REPOSITORY_STARGAZERS)
    dp.save_data(fd.SEARCH_NODE_ID)
    clusters = {}
    for node, content in dp.NODE_ID_CONTENT.items():
        if 'cluster' in content:
            if content['cluster'] not in clusters:
                clusters[content['cluster']] = []
            clusters[content['cluster']].append(node)
    for cluster in clusters.values():
        if len(cluster) > 100:
            print(cluster)

