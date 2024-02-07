# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Ex1Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""
def high_imdb_score(movie):
    return movie["imdb"] > 5.5
movie_name = input()
print(high_imdb_score(movie_name))
?????
"""

#Ex2Write a function that returns a sublist of movies with an IMDB score above 5.5.
def get_sublist(movie_list):
    sublist = [movie for movie in movie_list if movie['imdb'] > 5.5]
    return sublist
sublist = get_sublist(movies)
print(sublist)

#Ex3Write a function that takes a category name and returns just those movies under that category.
def get_movies_category(movies, category):
    movies_category = [movie for movie in movies if movie['category']==category]
    return movies_category
category_input = input()
category_of_movies = get_movies_category(movies,category_input)
print(category_of_movies)

#Ex4Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb(movie_list):
    score = 0
    num_movies = len(movie_list)
    for movie in movie_list:
        score += movie['imdb']
    if num_movies > 0:
        av_score = score / num_movies
        return av_score
    else:
        return 0
av_imdb = average_imdb(movies)
print(av_imdb)

#Ex5Write a function that takes a category and computes the average IMDB score.
def av_imdb_category(movie_list, category):
    score = 0
    num_movies = 0

    for movie in movie_list:
        if movie['category'] == category:
            score += movie['imdb']
            num_movies += 1
    
    if num_movies>0:
        av_score = score / num_movies
        return av_score
    else:
        return 0
input_category = input()  
av_imdb = av_imdb_category(movies,input_category)
print(av_imdb)