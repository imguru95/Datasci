import csv

class K_Means_Clustering:
    def euclidean_distance(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5 
         
    def iterate_k_means(self, data_points):
        # Set initial random centroids
        centroids = [(0, 0), (1, 1), (2, 2)] 
        print("Initial centroids : ", centroids) 
        cluster_points_1 = set()
        cluster_points_2 = set()
        cluster_points_3 = set()
        cnt = 0 
        while cnt < 10:
            cluster_points_1, cluster_points_2, cluster_points_3 = set(), set(), set() 
            for point in data_points:
                min_dist = float('inf') 
                centroid_number = -1 
                for i in range(len(centroids)):
                    dist = self.euclidean_distance(point, centroids[i])
                    if dist < min_dist: 
                        min_dist = dist 
                        centroid_number = i+1
                #Add to cluster list
                if centroid_number == 1:
                    cluster_points_1.add(data_points.index(point)+1)
                elif centroid_number == 2:
                    cluster_points_2.add(data_points.index(point)+1)
                elif centroid_number == 3:
                    cluster_points_3.add(data_points.index(point)+1)
                            
            x_0 = [data_points[p-1][0] for p in cluster_points_1]
            y_0 = [data_points[p-1][1] for p in cluster_points_1] 
            x_1 = [data_points[p-1][0] for p in cluster_points_2] 
            y_1 = [data_points[p-1][1] for p in cluster_points_2] 
            x_2 = [data_points[p-1][0] for p in cluster_points_3] 
            y_2 = [data_points[p-1][1] for p in cluster_points_3] 
        
            new_centroids = [(sum(x_0)/len(x_0), sum(y_0)/len(y_0)),(sum(x_1)/len(x_1), sum(y_1)/len(y_1)),(sum(x_2)/len(x_2), sum(y_2)/len(y_2))] 
            
            if new_centroids != centroids:
                centroids = new_centroids 
                cnt += 1 
            else:
                break
        
        print("Cluster 1: ", cluster_points_1)
        print("Cluster 2: ", cluster_points_2)
        print("Cluster 3: ", cluster_points_3)
        print("|C1|+|C2|+|C3| = ", len(cluster_points_1) + len(cluster_points_2) + len(cluster_points_3))
        print("Centroids at the end of convergence: ", centroids)
        print("Iterations for convergence = ", cnt)

input_data_points = []
with open('data_points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            input_data_points.append((int(row[1]), int(row[2])))
csv_file.close()
k = K_Means_Clustering()
k.iterate_k_means(input_data_points)
