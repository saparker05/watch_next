'''
This program defines a function which takes in a description of a movie and uses the similarity function in SpaCy
to compare the movies description against other movies stored in the file movies.txt. The function returns the most
similar movie as a recommendation to watch next. 
'''

# Import SpaCy and load the required model. 
import spacy

nlp = spacy.load('en_core_web_md')


# Define a function which takes in the description of a movie and returns the most similar movie in the films dictionary. 
def watch_next(description):

    description = nlp(description)

    highest_similarity = 0

    next_movie = None

    # For each film in the dictionary, compare the film description with the description passed to the function. 
    for film in films:

        films[film] = nlp(films[film])

        comparison = films[film].similarity(description)

        # If the similarity value is the highest so far, save this film as next_movie.
        if  comparison > highest_similarity:
            highest_similarity = comparison
            next_movie = film
    
    # Return the move with the highest similarity value. 
    return next_movie


# Create an empty dictionary to store the movie descriptions from the file movies.txt.
films = {}

try:
    movie_file = open('movies.txt', 'r', encoding='utf-8')

    # Read from the file movies.txt and store the films and descriptions in the films dictionary.
    for line in movie_file:
        line_split = line.split(':')
        films[line_split[0].strip()] = line_split[1]

    movie_file.close()

except FileNotFoundError as e:
    print("Error: the file movies.txt could not be found.")
    exit()

description1 = """Will he save the world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk landed on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Call the watch_next function using the description above and print the result. 
print(f"The next movie you should watch is {watch_next(description1)}.")
