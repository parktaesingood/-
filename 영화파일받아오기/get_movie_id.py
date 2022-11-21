import requests
import json


def get_movie_datas():
    total_data = []
    actor_data = []

    
    for i in range(3,8):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        # print(movies)

        for movie in movies['results']:
            total_data.append(movie['id'])
    
    # return total_data
    

    for j in total_data:
        request_url_2 = f"https://api.themoviedb.org/3/movie/{j}/credits?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR"
        actors = requests.get(request_url_2).json()
        # print(actors)
        for actor in actors['cast']:
            if actor['known_for_department'] == 'Acting':
                fields = {
                        'movie_id': j,
                        'actor_id': actor['id'],
                        'name': actor['name'],
                        'profile_path': actor['profile_path'],
                        'character': actor['character'],
                }
                
                data = {
                    "pk": actor['id'],
                    "model": "movies.actor",
                    "fields": fields
                }
            
                actor_data.append(data)
    

    with open("movie_actor.json", "w", encoding="utf-8") as w:
        json.dump(actor_data, w, indent=4, ensure_ascii=False)


get_movie_datas()