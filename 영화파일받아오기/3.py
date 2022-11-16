import requests
import json



def get_genre_datas():
    #1. URL 정보 설정
    request_url_2 = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key' : 'fc4061dbc8efeb36b5ca0d5006427fd4',
        "language" : "ko-KR",
    }
    total_data = []
    # 2. 요청 및 응답
    genres = requests.get(request_url_2, params=params).json()
    genres = genres['genres']
    print(genres)


    for genre in genres:
        
        fields = {
            
            # 'id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }

        total_data.append(data)

    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_genre_datas()