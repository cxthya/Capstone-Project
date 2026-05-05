'''
Cinthya Caldron-Hernandez
CSMC 111
Spring 2026
Capstone Assignment 2: Loops and Functions
'''
#Using ChatGBT to write code

media_log = []
print("⋆.ೃ࿔*:･ Welcome to your Media Consumption Library! ⋆.ೃ࿔*:･")

#These are the function for entries
def get_basic_info():
    title = input("What was the title?: ")
    media_type = input("Was it a book, movie or tv show? ").lower()
    rating = input("What do you rate it on a scale from 1-10?")
    return title, media_type, rating

def create_entry (title, media_type, rating):
    entry = {
        "Title": title,
        "Type": media_type,
        "Rating": rating
    }
    if media_type == "book":
        entry["Author"] = input("Author: ")
        entry["Genre"] = input("Genre: ")
    elif media_type == "movie":
        entry["Director"] = input("Director: ")
        entry["Genre"] = input("Genre: ")
    elif media_type == "tv show":
        entry["Number of Season"] = input("How many seasons?: ")
        entry["Genre"] = input("Genre: ")
    else:
        entry["Type"] = "Other"

    return entry

def view_entries(log):
    if not log:
        print("No entries yet!")
    else:
        for i, item in enumerate(log):
            print(f"\nEntry {i+1}: {item}")

#Okay now for the loop

while True:
    print("1. Add entry")
    print("2. View exisiting entries.")
    print("3. Leave")

    choice = input("Please choose an option :)")

    if choice == "1":
        title, media_type, rating = get_basic_info()
        entry = create_entry(title, media_type, rating)
        media_log.eppend(entry)
        print("Yayy! Entry saved!")

    elif choice == "2":
        view_entries(media_log)

    elif choice == "3":
        print("Okie!!! Goodbye~!")
        break

    else:
        print("Whoops! Invalid entry!")