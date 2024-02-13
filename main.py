def read_fruits():
    try:
        with open('fruits.txt', 'r') as file:
            file_contents = file.read()
        print(file_contents)
    except FileNotFoundError:
        print("File 'fruits.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def add_fruit():
    try:
        added_fruit = input("What kind of fruit would you like to add?")
        with open("fruits.txt", "a") as fruit_file:
            fruit_file.write(f"\n{added_fruit}")
    except FileNotFoundError:
        print("File 'fruits.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def main():
    while True:
        print("\nMenu:")
        print("1. Check Fruit")
        print("2. Add Fruit")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            fruit_lines = read_fruits()
            if fruit_lines:
                for line in fruit_lines:
                    print(line, end='')
        elif choice == '2':
            add_fruit()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
