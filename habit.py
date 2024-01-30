import datetime
from db import *
from datetime import *

class Habit:
    # Python implementation of a habit tracking app

    def __init__(self, db, name: str, frequency):
        """Habit class for creating habits

        :param db: database 
        :param name: name of the habit, has to be a string
        :param frequency: weekly or daily
        """
        self.db = db
        self.name = name
        self.frequency = frequency
        self.created_at = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        self.streak = 0

    def increment(self):
        # Increases streak by 1
        self.streak = display_current_streak(self.db, self.name)
        self.streak += 1

    def reset(self):
        # Reset streak
        self.streak = 1

    def __str__(self):
        # String presentation
        return f"{self.name}: {self.frequency}"

    def new_habit(self, db):
        # Adds a habit to the database
        add_habit(self.db, self.name, self.frequency)

    def delete_habit(self, db):
        # Removes a habit from the database
        name = check(self.db, self.name)
        if name:
            remove_habit(self.db, self.name)
            self.name = None
            self.frequency = None
            self.streak = 0
        else:
            print("\nHabit not found.")

    def longest_calculation(self,db):
        # Calculate the longest streak with the current streak
        current_streak = display_current_streak(self.db, self.name)
        current_streak_tracker = display_current_streak_tracker(self.db, self.name)
        if current_streak >= current_streak_tracker:
            self.current_streak = display_current_streak(self.db, self.name)
            update_habit_tracker(self.db, self.name, self.streak)

    def track_habit_up(self, db):
        # Track today's date for streak days increase
        # Needed for the completion functions
        self.increment()
        track(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest_calculation(self.db)

    def track_habit_down(self, db):
        # Decrement streak to 1 after breaking the habit
        # Needed for the completion functions
        self.streak = 1
        track(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest_calculation(self.db)

    def completion_habit_daily(self, db):
        # Add information to db when user has completed a habit - daily
        # Needed for the completion_habit function
        today = date.today()
        format = "%d-%m-%Y, %H:%M:%S"
        last = last_track(self.db, self.name)
        last_1 = [i[0] for i in last]
        ls = last_1[-1]
        if len(ls) < 0:
            self.track_habit_up(self)     
        else:
            last_tracked = datetime.strptime(ls, format).date()
            if today - last_tracked < timedelta(days=1):
                print("\nThis habit was already tracked today.")
            elif today - last_tracked < timedelta(days=2):
                self.track_habit_up(self)
            else:
                self.track_habit_down(db)

    def completion_habit_weekly(self, db):
        # Add information to db when user has completed a habit - weekly
        # Needed for the completion_habit function
        today = date.today()
        format = "%d-%m-%Y, %H:%M:%S"
        last = last_track(self.db, self.name)
        last_1 = [i[0] for i in last]
        if len(last_1) < 0:
            self.track_habit_up(self)     
        else:
            ls = last_1[-1]
            last_tracked = datetime.strptime(ls, format).date()
            if today - last_tracked < timedelta(days=7):
                print("\nThis habit was already tracked this week.")
            elif today - last_tracked < timedelta(days=8):
                self.track_habit_up(self)
            else:
                self.track_habit_down(db)

    def completion_habit(self, db):
        # Complete the habit
        name = check(self.db, self.name)
        if name:
            streak = display_current_streak(self.db, self.name)
            frequency = display_frequency(self.db, self.name)
            if frequency == 'daily':
                if streak == 0:
                    self.track_habit_up(self)
                else:
                    self.completion_habit_daily(db)
            else:
                if streak == 0:
                    self.track_habit_up(self)
                else:
                    self.completion_habit_weekly(db)
        else:
            print("\nHabit not found.")