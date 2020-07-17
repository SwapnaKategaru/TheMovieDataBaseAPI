import requests

# &language=en-US&page=1

path = "https://api.themoviedb.org/3/movie/top_rated?api_key=d77b5ab884174f60f4c9e8f50a70d99c"


def movies():
    data = requests.get(path).json()
    return data


print(len(movies()['results']))

titles = []
for i in movies()['results']:
    titles.append(i['title'])

print(titles)



class MovieDetails:

    def __init__(movies, title, popularity, vote_count, vote_average):
        movies.title = title
        movies.popular = popularity
        movies.votes = vote_count
        movies.avg_votes = vote_average

    #def votes(self):
       # self.avg_votes

print(movies)