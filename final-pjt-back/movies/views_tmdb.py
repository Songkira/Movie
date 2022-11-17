from django.http import JsonResponse, HttpResponse
import requests
from .models import Genre, Movie, Actor, Director

API_KEY = '65aefd05a6499f9a39973a6de70bb586'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

def tmdb_genres():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        print(genre)
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)


def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
        movie.actors.add(actor_id)
        if movie.actors.count() == 5:       # 5명의 배우 정보만 저장
            break

def get_director(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('crew'):
        if person.get('job') != 'Director': continue
        director_id = person.get('id')
        if not Director.objects.filter(pk=director_id).exists():
            director = Director.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
        movie.director.add(director_id)
        if movie.director.count() == 1:       # 감독 1명 정보만 저장
            break

def get_runtime_value(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    runtime_value = response.get('runtime')
    print(runtime_value)
    if runtime_value:
        return runtime_value
    return 0

def get_tagline(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    tagline = response.get('tagline')
    if tagline:
        return tagline
    return 'nothing'

def get_production_countries(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    production_countries = response.get('production_countries')
    if len(production_countries) == 0: return ("", "")
    iso = production_countries[0].get('iso_3166_1')
    name = production_countries[0].get('name')
    print(iso)
    print(name)
    if iso or name:
        return (iso, name)
    return ("", "")

def movie_data(page=1):     # 2. Movie popular 데이터를 불러와서 movie DB 형태로 정리하는 함수
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
            'page': page,     
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)       # 3. 유튜브 키 따로 가져오기
        runtime_value = get_runtime_value(movie_dict)   # 3. 런타임 정보 따로 불러오기
        tagline = get_tagline(movie_dict)               # 3. 태그라인 정보 따로 불러오기
        production_countries = get_production_countries(movie_dict)     # 3. 제조국 정보 따로 불러오기

        movie = Movie.objects.create(       # 4. movie 정보 만들기
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key,
            runtime=runtime_value,
            tagline=tagline,
            production_countries=production_countries[0],
            production_countries_name=production_countries[1],
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        get_actors(movie)
        get_director(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)    

def tmdb_data(request):     # 1. DB 처음 불러올 때
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Movie.objects.all().delete()
    Director.objects.all().delete()

    tmdb_genres()
    for i in range(1, 6):
        movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')