current_movies = {
    "the rrind": "11:30am",
    "spiderman": "12:15pm",
    "motor": "2:30pm"
}
for movies in current_movies:
    print(movies)
movie = input("what is the movie: ")    
showtime = current_movies.get(movie)
print("movie",movie, "is at", showtime)
if showtime == None:
    print("not in the list ")  