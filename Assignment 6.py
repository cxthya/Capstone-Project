'''
Cinthya Calderon-Hernandez
CSMC 111
Spring 2026
Assignment 6: Libraries
'''
#Using ChaptGBT to write this code

import json

#Loading data
def load_data(filename="media_log.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved file found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        print("File is corrupted. Starting fresh.")
        return []

#Saving the data
def save_data(log, filename="media_log.json"):
    try:
        with open(filename, "w") as file:
            json.dump(log, file, indent=4)
    except Exception as e:
        print("Error saving data:", e)

#Going back and getting basic info
def get_basic_info():
    title = input("What was the title?: ")
    media_type = input("Type (book, movie, tv show): ").lower().strip()
    rating = input("Rating (1-10): ")
    return title, media_type, rating

#User to creat entry
def create_entry(title, media_type, rating):

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
        entry["Seasons"] = input("How many seasons?: ")
        entry["Genre"] = input("Genre: ")

    else:
        entry["Type"] = "Other"

    return entry

#Viewing the entries
def view_entries(log):
    if not log:
        print("No entries yet!")
    else:
        for i, item in enumerate(log):
            print(f"\nEntry {i+1}: {item}")

#Main program
media_log = load_data()

print("⋆.ೃ࿔*:･ Welcome to your Media Consumption Library! ⋆.ೃ࿔*:･")

while True:
    print("\n1. Add entry")
    print("2. View entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            title, media_type, rating = get_basic_info()

            rating = int(rating)
            if rating < 1 or rating > 10:
                print("Rating must be between 1 and 10.")
                continue

            entry = create_entry(title, media_type, str(rating))
            media_log.append(entry)

            save_data(media_log)
            print("Entry saved!")

        except ValueError:
            print("Womp womp. Invalid input! Rating must be a number.")

    elif choice == "2":
        view_entries(media_log)

    elif choice == "3":
        print("Goodbye~! See ya later, alligator!")
        break

    else:
        print("Whoops! Invalid option. ")