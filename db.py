import sqlite3
import datetime
from datetime import *

def get_db(name='habits.db'):
  # Connect to the database (or create it if it doesn't exist)
  db = sqlite3.connect(name)
  create_tables(db)
  return db 

def create_tables(db):
  # Create tables into the database

  # Create cursor for executing SQL commands
  cur = db.cursor()

  # Create table "habits" for storing static habit data
  cur.execute("""
  CREATE TABLE IF NOT EXISTS habits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  frequency TEXT NOT NULL,
  created_at DATE NOT NULL,
  streak INTEGER
  )
  """)

  # Create table "tracker" for storing tracking events
  cur.execute("""
  CREATE TABLE IF NOT EXISTS tracker (
  name TEXT NOT NULL,
  tracked_at DATE,
  streak INTEGER NOT NULL,
  FOREIGN KEY (name) REFERENCES habits(name)
  )
  """)

  db.commit()

def add_habit(db, name, frequency, streak=0):
  # Insert a new habit into the created table "habits"
  cur = db.cursor()
  created_at = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
  cur.execute('''
  INSERT INTO habits VALUES (NULL, ?, ?, ?, ?)
  ''', (name, frequency, created_at, streak))
  db.commit()
  print("\nThe habit was added to the list.")

def remove_habit(db, name):
  # Remove a habit from the database (both tables)
  cur = db.cursor()
  cur.execute('''DELETE FROM habits WHERE name=?''', (name,))
  cur.execute('''DELETE FROM tracker WHERE name=?''', (name,))
  db.commit()
  print("\nThe habit was removed from the list.")

def track(db, name, tracked_at=None, streak=0):
  # Track a given habit
  cur = db.cursor()
  if tracked_at is None:
    tracked_at = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
  cur.execute('''INSERT INTO tracker VALUES (?, ?, ?)''', (name, tracked_at, streak))
  db.commit()
  print("\nThe habit has been tracked.")

def last_track(db, name):
  # Get the date and time of the latest tracking for a given habit
  cur = db.cursor()
  cur.execute('''SELECT tracked_at FROM tracker WHERE name=?''', (name,))
  return cur.fetchall()

def update_habit(db, name, streak):
  # Update the streak of a given habit in the habits table
  cur = db.cursor()
  cur.execute('''UPDATE habits SET streak=? WHERE name=?''', (streak, name))
  db.commit()

def update_habit_tracker(db, name, streak):
  # Upadte the streak of a given habit in the tracker table
  cur = db.cursor()
  cur.execute('''UPDATE tracker SET streak=? WHERE name=?''', (streak, name))
  db.commit()

def check(db, name):
  # Check whether a habit exists in the database or not
  # Useful in the testing code
  cur = db.cursor()
  cur.execute('''SELECT name FROM habits WHERE name=?''', (name,))
  return cur.fetchone()

def display_current_streak(db, name):
  # Display the current streak of a given habit from the habits table
  cur = db.cursor()
  cur.execute('''SELECT streak FROM habits WHERE name=?''', (name,))
  current_streak = cur.fetchall()
  return current_streak[0][0]

def display_current_streak_tracker(db, name):
  # Display the current streak of a given habit from the tracker table
  cur = db.cursor()
  cur.execute('''SELECT streak FROM tracker WHERE name=?''', (name,))
  current_streak_tracker = cur.fetchall()
  return current_streak_tracker[0][0]

def display_frequency(db, name):
  # Display the frequency of a given habit
  cur = db.cursor()
  cur.execute('''SELECT frequency FROM habits WHERE name=?''', (name,))
  frequency_1 = cur.fetchall()
  return frequency_1[0][0]

def display_habits(db):
  # Retrieve all habits from the database
  cur = db.cursor()
  cur.execute('''SELECT * FROM habits''')
  return cur.fetchall()

def display_habits_frequency(db, frequency):
  # Retrieve all habits based on their frequency from the database
  if frequency == "daily":
    cur = db.cursor()
    cur.execute('''SELECT * FROM habits WHERE frequency=?''', (frequency,))
    return cur.fetchall()
  else:
    cur = db.cursor()
    cur.execute('''SELECT * FROM habits WHERE frequency=?''', (frequency,))
    return cur.fetchall()

def display_longest_streak(db):
  # Retrieve the longest streak from all habits from the tracker table
  cur = db.cursor()
  cur.execute('''SELECT MAX(streak) FROM tracker''')
  return cur.fetchall()[0][0]

def display_longest_streak_habit(db, name):
  # Retrieve the longest streak for a given habit from the tracker table
  cur = db.cursor()
  cur.execute('''SELECT MAX(streak) FROM tracker WHERE name=?''', (name,))
  return cur.fetchall()[0][0]

def display_struggling_habit(db):
  # Retrieve a habit with the least streak number from the tracker table
  cur = db.cursor()
  cur.execute('''SELECT name FROM tracker WHERE streak = 1''')
  return cur.fetchall()[0][0]