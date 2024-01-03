# Heuristic Greedy Knapsack -> choosen heuristic = popularity / duration 

class Knapsack:
    @staticmethod
    def knapsack(songs, max_duration):
        
        # Calculate song value densities ( popularity/duration ) and store it along with the song index
        song_densities = [(song.popularity / song.duration, song) for song in songs]

        # Sort the songs based on the popularity/duration ratio in descending order
        song_densities.sort(key=lambda x: x[0], reverse=True)

        selected_songs = []

        remaining_duration = max_duration

        # Iterate over sorted song list and select the best songs until max_duration is reached
        for _, song in song_densities:
            if song.duration <= remaining_duration:
                selected_songs.append(song)
                remaining_duration -= song.duration

        return selected_songs

