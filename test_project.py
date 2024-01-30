import pytest

from habit import *
from analyze import *
from db import *


class TestHabit:
  # Class for testing main functions of the habit tracking app

  def setup_method(self):
    # Create a testing database
    self.db = get_db("test_habits.db")

  def test_add_habit(self):
    # Adding 5 habits to the database
    add_habit(self.db, "Meditate", "daily")
    add_habit(self.db, "Exercise", "weekly")
    add_habit(self.db, "Journaling", "weekly")
    add_habit(self.db, "Read a chapter", "weekly")
    add_habit(self.db, "Drink 1l of water", "weekly")

  def test_add_predefined_habits(self):
    # Adding 4 weeks of tracking data for the 5 predefined habits
    db = sqlite3.connect("test_habits.db")
    cur = db.cursor()
    tracking_data = [ # Daily habit with 4 weeks of daily completion
                     ("Meditate", "30-01-2024, 00:00:00", 28),
                     ("Meditate", "29-01-2024, 00:00:00", 27),
                     ("Meditate", "28-01-2024, 00:00:00", 26),
                     ("Meditate", "27-01-2024, 00:00:00", 25),
                     ("Meditate", "26-01-2024, 00:00:00", 24),
                     ("Meditate", "25-01-2024, 00:00:00", 23),
                     ("Meditate", "24-01-2024, 00:00:00", 22),
                     ("Meditate", "23-01-2024, 00:00:00", 21),
                     ("Meditate", "22-01-2024, 00:00:00", 20),
                     ("Meditate", "21-01-2024, 00:00:00", 19),
                     ("Meditate", "20-01-2024, 00:00:00", 18),
                     ("Meditate", "19-01-2024, 00:00:00", 17),
                     ("Meditate", "18-01-2024, 00:00:00", 16),
                     ("Meditate", "17-01-2024, 00:00:00", 15),
                     ("Meditate", "16-01-2024, 00:00:00", 14),
                     ("Meditate", "15-01-2024, 00:00:00", 13),
                     ("Meditate", "14-01-2024, 00:00:00", 12),
                     ("Meditate", "13-01-2024, 00:00:00", 11),
                     ("Meditate", "12-01-2024, 00:00:00", 10),
                     ("Meditate", "11-01-2024, 00:00:00", 9),
                     ("Meditate", "10-01-2024, 00:00:00", 8),
                     ("Meditate", "09-01-2024, 00:00:00", 7),
                     ("Meditate", "08-01-2024, 00:00:00", 6),
                     ("Meditate", "07-01-2024, 00:00:00", 5),
                     ("Meditate", "06-01-2024, 00:00:00", 4),
                     ("Meditate", "05-01-2024, 00:00:00", 3),
                     ("Meditate", "04-01-2024, 00:00:00", 2),
                     ("Meditate", "03-01-2024, 00:00:00", 1),
                     # Weekly habit with 4 weeks of completion
                     ("Exercise", "25-01-2024, 00:00:00", 4),
                     ("Exercise", "17-01-2024, 00:00:00", 3),
                     ("Exercise", "09-01-2024, 00:00:00", 2),
                     ("Exercise", "01-01-2024, 00:00:00", 1),
                     # Weekly habit with 3 weeks of completion
                     ("Journaling", "31-01-2024, 00:00:00", 3),
                     ("Journaling", "25-01-2024, 00:00:00", 2),
                     ("Journaling", "17-01-2024, 00:00:00", 1),
                     ("Journaling", "01-01-2024, 00:00:00", 1),   
                     # Weekly habit with 2 weeks of completion
                     ("Read a chapter", "05-02-2024, 00:00:00", 2),
                     ("Read a chapter", "31-01-2024, 00:00:00", 1),
                     ("Read a chapter", "17-01-2024, 00:00:00", 1),
                     ("Read a chapter", "01-01-2024, 00:00:00", 1), 
                     # Weekly habit with 1 week of completion - struggling habit                                      
                     ("Drink 1l of water", "17-02-2024, 00:00:00", 1),
                     ("Drink 1l of water", "05-02-2024, 00:00:00", 1),
                     ("Drink 1l of water", "17-01-2024, 00:00:00", 1),
                     ("Drink 1l of water", "01-01-2024, 00:00:00", 1)]

    cur.executemany('''INSERT INTO tracker VALUES(?, ?, ?)''', tracking_data)
    db.commit()

  def test_new_habit(self):
    # Check that new habits are added to the database correctly
    alcohol = Habit(self.db, "No alcohol", "weekly")
    alcohol.new_habit(self.db)
    assert check(self.db, "No alcohol")

  def test_remove_habit(self):
    # Check that habits are removed from the database correctly
    remove_habit(self.db, "No alcohol")
    assert check(self.db, "No alcohol") is None

  def test_track(self):
    # Track a habit and check if it was tracked correctly
    track(self.db, "Journaling", "05-02-2024, 00:00:00")
    track(self.db, "Journaling", "17-02-2024, 00:00:00")
    assert last_track(self.db, "Journaling") is not None

  def test_display_habits(self):
    # Check that habits are retrieved from the database correctly
    # Check that habits are then displayed to the user correctly
    assert display_habits(self.db) is not None

  def test_display_habits_frequency(self):
    # Check that habits are retrieved from the database correctly based on the frequency
    # Check that habits are then displayed to the user correctly

    # For daily habits
    assert display_habits_frequency(self.db, "daily") is not None

    # For weekly habits
    assert display_habits_frequency(self.db, "weekly") is not None

  def test_display_longest_streak(self):
    # Check that the longest streak is retrieved from the database correctly
    # Check that the longest streak is then displayed to the user correctly
    assert display_longest_streak(self.db) == None

  def test_display_longest_streak_habit(self):
    # Check that the longest streak is retrieved from the database correctly based on the frequency
    # Check that the longest streak is then displayed to the user correctly
    assert display_longest_streak_habit(self.db, "Meditate") == None

  def teardown_method(self):
    # Delete database after tests
    import os
    os.remove("test_habits.db")