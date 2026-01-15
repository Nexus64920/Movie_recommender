import json
import os
from datetime import datetime

type_choices = ["movie", "series"]
genre_choices = ["Action", "Drama", "Comedy", "Horror", "Sci-Fi", "Fantasy", "Historical"]
stars_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yn_choices = ["yes", "no"]
length_choices = ["<1h 30m", "1h 30m - 2h", "2h - 2h 30m", "2h 30m-3h", "3h+"]
release_choices = ["<1 yr", "1-10 yrs", "10-20 yrs", "20-30 yrs", "30+ yrs"]

#file opener with os to locate
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "films.json")
year = datetime.now().year

with open(FILE_PATH, "r", encoding="utf-8") as f:
    films = json.load(f)
    
def survey(choices):
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    selection = int(input("Choose a number: "))
    print("\nYou selected: " + str(choices[selection - 1]) + "\n")
    return str(choices[selection - 1])

def point_system(movie):
    score = 0
    
    #genre and film type give the most amount of points as the most important
    if movie["type"] == film_type:
        score += 2
        
    #if the genre tag is related in anyway, the points are given
    for i in range(len(movie["genre"])):
        if genre in movie["genre"][i]:
            score += 2
            
    if movie["rating"] >= stars:
        score += 1
        
    if movie["animated"] == animated:
        score += 1
        
    #although emmies and oscars are not the same, they are both considered as an award winner    
    if (movie["award_winner"] == winner):
        score += 1
        
    length_range = time_conversion(movie)
    if (film_type == "movie"):
        if(length_range == length):
            score += 1
            
    release_range = release_conversion(movie)
    if(release_range == release_date):
        score += 1
        
    return score
        
def time_conversion(movie):
    length = movie["length"]
    result = ""
    
    if("1h" in length):
        if(len(length) <= 5):
            result = "<1h 30m"
        elif((len(length) > 5) and int(length[3:5]) <= 30):
            result = "<1h 30m"
        else:
            result = "1h 30m - 2h"
            
    if("2h" in length):
        if(len(length) <= 5 and len(length) > 3):
            result = "2h - 2h 30m"
        elif((len(length) > 5) and int(length[3:5]) <= 30):
            result = "2h - 2h 30m"
        else:
            result = "2h 30m - 3h"
            
    if("3h" in length):
        if(len(length) > 2):
            result = "3h+"
        else:
            result = "2h 30m - 3h"
            
    return result       

def release_conversion(movie):
    result = ""
    distance = year - movie["release_date"]
    
    if (distance < 1):
        result = "<1 yr"
        
    elif(distance >= 1 and distance <= 10):
        result = "1-10 yrs"
        
    elif(distance > 10 and distance <= 20):
        result = "10-20 yrs"
        
    elif(distance > 20 and distance <= 30):
        result = "20-30 yrs"
        
    elif(distance > 30):
        result = "30 yrs"
    
    return result
        
print("Movie or Series?")
film_type = survey(type_choices)

print("Favorite genre?")
genre = survey(genre_choices)

print("movie rating? (Out of 10)")
stars = int(survey(stars_choices))

print("Animated film?")
animated = survey(yn_choices)
animated = (animated == "yes")

if(film_type == "movie"):
    print("Preferable movie length?")
    length = survey(length_choices)

if(film_type == "movie"):
    print("Oscar winner?")
    winner = survey(yn_choices)
else:
    print("Emmy winner?")
    winner = survey(yn_choices)
winner = (winner == "yes")

print("released how long ago?")
release_date = survey(release_choices)

scored_films = {}
for film in films:
    film_score = point_system(film)
    if(film_score > 0):
        scored_films[film["title"]] = film_score
        
#sorting the films in a new list based on respective scores 
sorted_films = sorted(scored_films, key = scored_films.get, reverse = True)

#keyword to end the program
stopped = False

#initial amount of recommendations
displayed_amount = 5

while (stopped == False):
    if(len(sorted_films) - displayed_amount >= 0):
        for i in range(displayed_amount - 5, displayed_amount):
            print(f"{i+1}. {sorted_films[i]}")
    
    else:
        for i in range(len(sorted_films)):
            print(f"{i+1}. {sorted_films[i]}")
        
    print("would you like more options?")
    more = survey(yn_choices)
    
    if(more == "no"):
        stopped = True
        
    elif(len(sorted_films) - displayed_amount < 5 and len(sorted_films) - displayed_amount > 0):
        displayed_amount += (len(sorted_films) - displayed_amount)
    
    #in case the amount of movies to display is less than 5 or is 0
    elif(len(sorted_films) - displayed_amount == 0):
        stopped = True
        print("All movie recommendations sent")
    else:
        displayed_amount += 5
    
    
