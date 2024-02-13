def read_list():
    try:
        with open('shopping_list.txt', 'r') as file:
            file_contents = file.read()
        print(file_contents)
    except FileNotFoundError:
        print("No Shopping List not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def add_item():
    try:
        added_fruit = input("What are we shopping for today?")
        with open("shopping_list.txt", "a") as fruit_file:
            fruit_file.write(f"\n{added_fruit}")
    except FileNotFoundError:
        print("No Shopping List not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def delete_item():
    try:
        with open("shopping_list.txt", "r") as file:
            fruit_list = file.readlines()

        print("Current Shopping List:")
        for i, fruit in enumerate(fruit_list, start=1):
            print(f"{i}. {fruit.strip()}")

        if not fruit_list:
            print("No items to delete.")
            return

        while True:
            try:
                index_to_delete = int(input("Enter the number of the item you want to delete (0 to cancel): "))
                if index_to_delete == 0:
                    return
                elif 1 <= index_to_delete <= len(fruit_list):
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        fruit_to_delete = fruit_list.pop(index_to_delete - 1)

        with open("shopping_list.txt", "w") as file:
            file.writelines(fruit_list)

        print(f"'{fruit_to_delete.strip()}' has been deleted.")

    except FileNotFoundError:
        print("No Shopping List not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    while True:
        print("\Shopping List:")
        print("1. Check shopping list")
        print("2. Add an item")
        print("3. Delete an item")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            read_list()
        elif choice == '2':
            add_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
