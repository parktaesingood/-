import requests
import json


def get_movie_datas():
    total_data = []

    
    for i in range(1,2):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            total_data.append(movie['id'])
    
    for movie in movies
    for j in total_data:
        request_url2 = f"https://api.themoviedb.org/3/movie/{j}/credits?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KO"
        actors = requests.get(request_url2)

    with open("movie_id.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()