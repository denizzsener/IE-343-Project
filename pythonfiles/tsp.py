class TSP:
    @staticmethod
    def nearest_neighbor_tsp(cities):
        num_cities = len(cities)
        visited = [False] * num_cities
        tour = []

        current_city_index = 0
        visited[current_city_index] = True
        tour.append(cities[current_city_index])

        while len(tour) < num_cities:
            nearest_city_index = -1
            min_distance = float('inf')

            for i, city in enumerate(cities):
                if not visited[i]:
                    distance = cities[current_city_index].distance_to(city)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_city_index = i

            visited[nearest_city_index] = True
            current_city_index = nearest_city_index
            tour.append(cities[current_city_index])

        return tour


 