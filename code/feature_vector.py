import numpy as np
import networkx as nx
import numpy as np
import networkx as nx

def calculate_network_characteristics(adjMatrix):
    # 从邻接矩阵创建图
    G = nx.from_numpy_matrix(np.array(adjMatrix))
    
    # 计算各种拓扑特征
    features = {}
    
    # 节点的度
    degrees = dict(G.degree())
    features['degrees'] = degrees
    features['average_degree'] = sum(degrees.values()) / len(degrees)
    
    # 聚类系数
    clustering_coeffs = nx.clustering(G)
    features['clustering_coeffs'] = clustering_coeffs
    features['average_clustering_coefficient'] = sum(clustering_coeffs.values()) / len(clustering_coeffs)
    
    # 平均路径长度和直径
    if nx.is_connected(G):
        features['average_shortest_path_length'] = nx.average_shortest_path_length(G)
        features['diameter'] = nx.diameter(G)
    else:
        features['average_shortest_path_length'] = None
        features['diameter'] = None
    
    # 密度
    features['density'] = nx.density(G)
    
    # 节点中心性
    features['degree_centrality'] = nx.degree_centrality(G)
    features['closeness_centrality'] = nx.closeness_centrality(G)
    features['betweenness_centrality'] = nx.betweenness_centrality(G)
    
    # 网络连通性
    features['is_connected'] = nx.is_connected(G)
    features['number_connected_components'] = nx.number_connected_components(G)
    
    return features

adjMatrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

def features_to_vector(features):
    feature_vector = []

    # 添加平均度
    feature_vector.append(features['average_degree'])

    # 添加平均聚类系数
    feature_vector.append(features['average_clustering_coefficient'])

    # 添加平均最短路径长度（如果网络不连通，则添加一个默认值或不添加）
    feature_vector.append(features['average_shortest_path_length'] if features['average_shortest_path_length'] is not None else 0)

    # 添加网络直径（如果网络不连通，则添加一个默认值或不添加）
    feature_vector.append(features['diameter'] if features['diameter'] is not None else 0)

    # 添加网络密度
    feature_vector.append(features['density'])

    # 由于中心性是字典格式，计算其平均值并添加
    feature_vector.append(sum(features['degree_centrality'].values()) / len(features['degree_centrality']))
    feature_vector.append(sum(features['closeness_centrality'].values()) / len(features['closeness_centrality']))
    feature_vector.append(sum(features['betweenness_centrality'].values()) / len(features['betweenness_centrality']))

    # 添加网络是否连通的特征（二元特征）
    feature_vector.append(1 if features['is_connected'] else 0)

    # 添加网络连通分量数量
    feature_vector.append(features['number_connected_components'])

    return np.array(feature_vector)


import scipy.io as scio
file = r'e:\Administrator\Down\adjacency_matrices.mat'
data = scio.loadmat(file)
adjMatrix = data['adj_matrices']
# print(adjMatrix)
print(adjMatrix.shape)
feature_vector_list = []
for i in range(adjMatrix.shape[0]):
    # print(adjMatrix[i][0])
    print(adjMatrix[i][0].shape)
    network_features = calculate_network_characteristics(adjMatrix[i][0])
    feature_vector = features_to_vector(network_features)
    feature_vector_list.append(feature_vector)

print(feature_vector_list)
print(len(feature_vector_list))

# 将feature_vector_list保存到文件
scio.savemat('e:\\Administrator\\Down\\feature_vector_list.mat', {'feature_vector_list': feature_vector_list})

    
# # 使用前面计算的网络特征
# network_features = calculate_network_characteristics(adjMatrix)

# # 将特征转换为特征向量
# feature_vector = features_to_vector(network_features)
# print(feature_vector)
