#! usr/env/bin/python3 

import parameter_data as data_file

print(data_file.read_stocklist_to_set())


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Option 5")
        print("6. Option 6")
        print("7. Option 7")
        print("0. Exit")

        choice = input("Enter your choice (0–7): ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice in [str(i) for i in range(1, 8)]:
            print(f"You selected option {choice}")
        else:
            print("Invalid input. Please choose a number between 0 and 7.")

if __name__ == "__main__":
    main()