import sys
import numpy as np
import matplotlib.pyplot as plt
with open("HW_7_data_2D(1).dat", 'r') as f:
    rows = [line.strip() for line in f]
data = np.array(rows)
data = np.genfromtxt("HW_7_data_2D(1).dat", dtype=float, delimiter='  ')
a = data[1, :]

def Euclidean_Dist(X, Y):
    i = 0
    j = 0
    sum = 0
    while i < len(X):
        while j < len(Y):
            sum = sum + np.square(X[i]-Y[j])
            j += 1
            break
        i += 1
    return np.sqrt(sum)
def sqr_error(X, Y):
    i = 0
    j = 0
    sum = 0
    while i < len(X):
        sum = sum + Euclidean_Dist(X[i], Y[i])
        i += 1
    return sum



def k_mean_clustering(data, No_of_Clusters, threshold):
    data = data
    Cluster_centroids = []
    Clusters = {}
    for i in range(No_of_Clusters):
        random_index = np.random.randint(len(data))
        Cluster_centroids.append(data[random_index, :])
        Clusters[i] = np.empty(shape=(2, ), dtype=float)
    while True:
        for i in range(len(data)):
            temp = []
            for j in Cluster_centroids:
                distance = Euclidean_Dist(data[i, :], j)
                temp.append(distance)
            for k in range(len(temp)):
                if temp[k] == min(temp):
                    Clusters[k] = np.vstack((Clusters[k], np.array(data[i, :])))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.scatter(Clusters[0][1:, 0], Clusters[0][1:, 1], color='red')
        ax1.scatter(Clusters[1][1:, 0], Clusters[1][1:, 1], color='blue')
        ax1.scatter(Cluster_centroids[0][0] ,Cluster_centroids[0][1], color='black')
        ax1.scatter(Cluster_centroids[1][0] ,Cluster_centroids[1][1], color='black')
        plt.show()
        Old_Cluster_centroids = []
        for i in range(len(Cluster_centroids)):
            Old_Cluster_centroids.append(Cluster_centroids[i])
            Cluster_centroids[i] = np.mean(Clusters[i][1:, :], axis=0)
            Clusters[i] = np.empty(shape=(2, ), dtype=float)

        if sqr_error(Cluster_centroids, Old_Cluster_centroids) <= threshold:
            sys.exit()

k_mean_clustering(data, 2, 0.01)
