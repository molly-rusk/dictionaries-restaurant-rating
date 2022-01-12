"""Restaurant rating lister."""

def restaurantScores():
    
    scoresFile = open('scores.txt')

    restScores = {}

    for line in scoresFile:
        line = line.rstrip()
        name, score = line.split(':')
        restScores[name] = int(score)

    return restScores

def addNewRestaurant(restScores):
    print("Add a new restaurant below")
    restaurantName = input("Restaurant name:")
    restaurantRating = int(input("Rating(1-5):"))

    restScores[restaurantName] = restaurantRating

def displaySorted(restScores):
    for name, rating in sorted(restScores.items()):
        print(f"{name} is rated at {rating}")

restScores = restaurantScores()

addNewRestaurant(restScores)

displaySorted(restScores)