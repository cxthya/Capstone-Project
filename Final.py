'''Cinthya Calderon-Hernandez
CSMC 111
Spring 2026
Final Project
'''
#Used ChaptGBPT

#Added JSON library and file uploading system
import json

# LOAD SAVED DATA
#added error handling blocks~~~

def load_data(filename="media_log.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("!!!!Warning!!!!: Data file corrupted. Starting fresh.")
        return []


# SAVE DATA TO FILE
#save_data funtion for storage

def save_data(log, filename="media_log.json"):
    try:
        with open(filename, "w") as file:
            json.dump(log, file, indent=4)
    except Exception as e:
        print("Error saving file:", e)


# GET USER INPUT

def get_basic_info():
    title = input("Title: ")
    media_type = input("Type (book/movie/tv show): ").lower().strip()
    rating = input("Rating (1-10): ")
    return title, media_type, rating



# CREATE MEDIA ENTRY

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
        entry["Seasons"] = input("Number of seasons: ")
        entry["Genre"] = input("Genre: ")

    else:
        entry["Type"] = "Other"

    return entry


# VIEW ALL ENTRIES

def view_entries(log):
    if not log:
        print("Whoopsies! No entries yet.")
        return

    for i, item in enumerate(log):
        print(f"\n{i+1}. {item}")



# DATA ANALYSIS DASHBOARD

def show_stats(log):
    if not log:
        print("Oh no! No data to analyze.")
        return

    ratings = [int(item["Rating"]) for item in log]
    average = sum(ratings) / len(ratings)

    highest = max(log, key=lambda x: int(x["Rating"]))

    books = len([x for x in log if x["Type"] == "book"])
    movies = len([x for x in log if x["Type"] == "movie"])
    tv = len([x for x in log if x["Type"] == "tv show"])

    print("\n📊 MEDIA STATISTICS")
    print("-------------------")
    print("Total entries:", len(log))
    print("Average rating:", round(average, 2))
    print("Highest rated:", highest["Title"], f"({highest['Rating']})")
    print("Books:", books)
    print("Movies:", movies)
    print("TV Shows:", tv)


# MAIN PROGRAM

media_log = load_data()

print("⋆.ೃ࿔*:･ Welcome to your Media Consumption Library! ⋆.ೃ࿔*")

while True:
    print("\n1. Add entry")
    print("2. View entries")
    print("3. View statistics")
    print("4. Exit")

    choice = input("Choose an option: ")

    # ADD ENTRY
    if choice == "1":
        try:
            title, media_type, rating = get_basic_info()

            rating = int(rating)

            if rating < 1 or rating > 10:
                print("Rating must be 1-10.")
                continue

            entry = create_entry(title, media_type, str(rating))
            media_log.append(entry)

            save_data(media_log)

            print("Yippie!!!!! Entry saved!")

        except ValueError:
            print("!!!Error!!!: Rating must be a number.")

    # VIEW ENTRIES
    elif choice == "2":
        view_entries(media_log)

    # STATISTICS
    elif choice == "3":
        show_stats(media_log)

    # EXIT
    elif choice == "4":
        print("Goodbye~! See ya later alligator!")
        break

    else:
        print("WOMP! Invalid option")
