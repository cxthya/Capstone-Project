'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Capstone Project: Assignment 1
'''

#Media Log List
media_log = []

print("⋆.ೃ࿔*:･Welcome to your  Media Consumption Library!⋆.ೃ࿔*:･")

title = input("What was the title?: ")
media_type = input("Fun! What type of content was it? (Book, Movie, TV Show): ").lower()
rating = input("How many stars would you rate it? (1-10): ")

#conditional statments based on what media type
if media_type == "book":
    author = input("Author: ")
    genre = input("Genre: ")

    entry = {
        "Title": title,
        "Type": media_type,
        "Rating": rating,
        "Author": author,
        "Genre": genre
    }
elif media_type == "movie":
    director = input("Director: ")
    genre = input("Genre: ")

    entry = {
        "Title": title,
        "Type": media_type,
        "Rating": rating,
        "Director": director,
        "Genre": genre
    }
else:
    print("Unkown media type. Entry will be saved as 'Other'.")
    entry = {
        "Title": title,
        "Type": "Other",
        "Rating": rating
    }

#Add entry to media log
media_log.append(entry)
print("Entry saved! ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ Yummy! Have fun consuming!")
