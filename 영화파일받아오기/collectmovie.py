import requests
import json


def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(3,8):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        print(movies['results'])

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'adult': movie['adult'],
                    'backdrop_path': movie['backdrop_path'],
                    'released_date': movie['release_date'],
                    'original_language': movie['original_language'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()