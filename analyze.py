from db import *

def view_habits(db):
    # Display all habits
    print(display_habits(db)) 

def view_habits_frequency(db, frequency):
    #Display all habits based on their frequency
    print(display_habits_frequency(db, frequency))

def view_longest_streak(db):
    # Displays the longest streak of all habits
    longest_streak = display_longest_streak(db)
    print(f"\n{longest_streak} days is the longest streak of all habits.")
    
def view_longest_streak_habit(db, name):  
    # Displays the longest streak of a given habit
    checking = check(db, name)
    if checking:
        cur = db.cursor()
        cur.execute('''SELECT name FROM tracker where name=?''', (name,))
        result = cur.fetchone()
        if result:
            longest_streak_habit = display_longest_streak_habit(db, name)
            print(f"\n{longest_streak_habit} days is the longest streak for the habit {name}.")
            return longest_streak_habit
        else:
            print(f"\nThe habit {name} doesnt have a streak.")
    else:
        print("\nHabit not found.")

def view_struggling_habit(db):
    # Displays a habit with the least streak number
    struggling_habit = display_struggling_habit(db)
    print(f"\n{struggling_habit} is the habit you are struggling the most with. Keep it up!")