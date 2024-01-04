from csv_parser import CSVParser
from knapsack import Knapsack
from tsp import TSP
import time

def main():

    start = time.time()

    songs = CSVParser.parse_songs("data/songs_data_frank_ocean.csv")

    max_duration = 200  # Replace this value with your desired maximum duration
    selected_songs = Knapsack.knapsack(songs, max_duration)

    print()
    print(f"Choosen songs for max duration: {max_duration}")
    for song in selected_songs:
        print(f"Song: {song.name} Popularity - {song.popularity}, Duration - {song.duration}")
    print()

    file_name = "data/deniz_asli_cities.csv"

    cities = CSVParser.parse_cities(file_name)
    result = TSP.nearest_neighbor_tsp(cities)
    print()
    print(f"Optimal Tour Route: {[city.name for city in result]}")
    print()

    # Other parts of your code
    for city in result:
        print(f" For City: {city.name} we choose the songs {[(song.name, round(song.duration,2)) for song in Knapsack.knapsack(songs=selected_songs,max_duration=city.duration)]}")
        print()

    end = time.time()

    print(f"Runtime: {end - start}")

if __name__ == "__main__":
    main()
