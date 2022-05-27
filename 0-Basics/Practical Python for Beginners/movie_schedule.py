current_movies = {'Grinch':'11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty': '3:00pm',
                  'Christmas':'5:00pm'}

print("We are showing the following movies:")
for key in current_movies:
    print(key)
movie = input('movie name?\n')

showtime = current_movies.get(movie)
if showtime==None:
    print("Requested showtime isn't playing")
else:
    print(movie, 'is playing at', showtime)