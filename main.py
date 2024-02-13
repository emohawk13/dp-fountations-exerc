def print_file_contents_using_readline():
    with open('quotes.txt', 'r') as file:
        line = file.readline()
        if line:
            print(line, end='')

def print_file_contents_using_readlines():
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')

def print_file_contents_using_readlines_alt():
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        print(''.join(lines), end='')

def print_file_contents_using_for_loop():
    with open('quotes.txt', 'r') as file:
        for line in file:
            print(line, end='')

def main():
    while True:
        print("\nMenu:")
        print("1. Print file contents using readline()")
        print("2. Print file contents using readlines()")
        print("3. Print file contents using for loop")
        print("4. Print using readlines() without using a loop")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print_file_contents_using_readline()
        elif choice == '2':
            print_file_contents_using_readlines()
        elif choice == '3':
            print_file_contents_using_for_loop()
        elif choice == '4':
            print_file_contents_using_readlines_alt() 
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

