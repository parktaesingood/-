import requests
import json

TMDB_API_KEY = 'fc4061dbc8efeb36b5ca0d5006427fd4'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        total_data.append(movies)
    return total_data

    #     for movie in movies['results']:
    #         if movie.get('release_date', ''):
    #             fields = {
    #                 'movie_id': movie['id'],
    #                 'title': movie['title'],
    #                 'released_date': movie['release_date'],
    #                 'popularity': movie['popularity'],
    #                 'vote_avg': movie['vote_average'],
    #                 'overview': movie['overview'],
    #                 'poster_path': movie['poster_path'],
    #                 'genres': movie['genre_ids']
    #             }

    #             data = {
    #                 "pk": movie['id'],
    #                 "model": "movies.movie",
    #                 "fields": fields
    #             }

    #             total_data.append(data)

    # with open("movie_data.json", "w", encoding="utf-8") as w:
    #     json.dump(total_data, w, indent="\\t", ensure_ascii=False)

print(get_movie_datas())
