import requests
from pprint import pprint
import json

TMDB_API_KEY = 'fc4061dbc8efeb36b5ca0d5006427fd4'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f'https://api.themoviedb.org/3/movie/popular?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR&page={i}'
        movies = requests.get(request_url).json()
        total_data.append(movies)
        
        return total_data

    # with open("movie_data.json", "w", encoding="utf-8") as w:
    #     json.dump(total_data, w, indent="\\t", ensure_ascii=False)

# print(get_movie_datas())

if __name__ == '__main__':
    pprint(get_movie_datas())
