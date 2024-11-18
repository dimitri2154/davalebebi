import json

def modify_movies(filename="movies.json"):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

        modified_movies = []
        for page_data in data:
            for movie in page_data['results']:
                year = int(movie['release_date'].split('-')[0])
                genre = movie['genres']

                if year > 2000 and "Crime" in genre:
                    genre[:] = ["New_Crime" if g == "Crime" else g for g in genre]
                    modified_movies.append(movie)
                elif year < 2000 and "Drama" in genre:
                    genre[:] = ["Old_Drama" if g == "Drama" else g for g in genre]
                    modified_movies.append(movie)
                elif year == 2000:
                    genre.append("New_Century")
                    modified_movies.append(movie)

        with open(filename, 'w') as json_file:
            json.dump(modified_movies, json_file, indent=4)

    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

modify_movies()