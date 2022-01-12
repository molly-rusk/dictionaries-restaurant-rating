"""Restaurant rating lister."""

dictionary = {}
with open("scores.txt") as file:
    for line in file:
        (key, value) = line.split(':')

        dictionary[key] = int(value[0])

print(dictionary)
