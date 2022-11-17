import requests
import json


    
def get_movie_datas():
    total_data = []
    actor_data = []
    actor_name_data = []


    for i in range(1,2):
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
            actor_data.append(actor['id'])
            # print(actor_data)
    
    
    for k in actor_data:
        request_url_3 = f"https://api.themoviedb.org/3/person/{k}?api_key=fc4061dbc8efeb36b5ca0d5006427fd4&language=ko-KR"
        actors_names = requests.get(request_url_3).json()
        print(actors_names)
        
    #     for actors_name in actors_names:
    #         fields = {
    #             'actor_name': actors_name['actors_name'],    
    #         }
            
    #         data = {
    #             "pk": k,
    #             "model": "movies.actor_name",
    #             "fields": fields
    #         }
            
    #         actor_name_data.append(data)
            
            
    # with open("movie_actor_name.json", "w", encoding="utf-8") as w:
    #     json.dump(actor_data, w, indent=4, ensure_ascii=False)

get_movie_datas()

            
            

            
            
        
        

