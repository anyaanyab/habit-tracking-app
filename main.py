from habit import * 
from analyze import *
from db import *

def menu():
    # Main menu
    print("\nMenu:")
    print("1. Add Habit")
    print("2. Track Habit")
    print("3. Delete Habit")
    print("4. View Habits")
    print("5. Analyze Habits")
    print("6. Exit")  

def menu_2():
    # Menu for 4. View Habits
    print("\nChoose which habits you want to view:")
    print("\n1. All Habits")
    print("\n2. Daily Habits")
    print("\n3. Weekly Habits")

def menu_3():
    # Menu for 5. Analyze Habits
    print("\nChoose what you want to analyze:")
    print("\n1. Longest Streak Of All Habits")
    print("\n2. Longest Streak Of One Habit")
    print("\n3. Display Most Struggling Habit")


def main():
    # CLI for user interaction
    db = get_db()
    global habits
    habits = []
    while True:
        menu()
        choice = input("\nEnter choice: ")
        # Users are entering their choice as numbers through the input function
        if choice == "1":
            name = input("\nEnter habit name: ")
            frequency = input("Enter habit frequency (daily/weekly): ")
            habit = Habit(db, name, frequency)
            habit.new_habit(db)
        elif choice == "2":
            name = input("\nEnter habit name: ")
            habit = Habit(db, name, "NULL")
            habit.completion_habit(db)
        elif choice == "3":
            name = input("\nEnter habit name: ")
            habit = Habit(db, name, "NULL")
            habit.delete_habit(db)
        elif choice == "4":
            menu_2()
            choice = input("\nEnter choice: ")
            if choice == "1":
                view_habits(db)
            elif choice == "2":
                view_habits_frequency(db, frequency="daily")
            elif choice == "3":
                view_habits_frequency(db, frequency="weekly")
            else:
                print("\nInvalid choice.")
        elif choice == "5":
            menu_3()
            choice = input("\nEnter choice: ")
            if choice == "1":
                view_longest_streak(db)
            elif choice == "2":
                name = input("\nEnter habit name: ")
                view_longest_streak_habit(db, name)
            elif choice == "3":
                view_struggling_habit(db)
            else:
                print("\nInvalid choice.")
        elif choice == "6":
            print("\nHope to see you tracking your habits again soon!")
            break
        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()