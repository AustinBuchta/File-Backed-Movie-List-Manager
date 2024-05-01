print("The Movie List Program")

def display_menu():
    print("==== Movie Library ====")
    print("1. List all movies")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")

def display_titles(movie_list):
    print("\n=== Movie Titles ===")
    for idx, title in enumerate(movie_list, start=1):
        print(f"{idx}. {title}")

def add_title(movie_list):
    title = input("Enter the title to add: ")
    movie_list.append(title)
    print(f"{title} has been added to the list.")
    display_titles(movie_list)

def delete_title(movie_list):
    display_titles(movie_list)
    try:
        index = int(input("Enter the number of the title to delete: ")) - 1
        if 0 <= index < len(movie_list):
            deleted_title = movie_list.pop(index)
            print(f"{deleted_title} has been deleted from the list.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    display_titles(movie_list)

def main():
    movie_list = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
    print()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_titles(movie_list)
        elif choice == "2":
            add_title(movie_list)
        elif choice == "3":
            delete_title(movie_list)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please enter a valid option.")

if __name__ == "__main__":
    main() 


