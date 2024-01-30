# Habit Tracking App

A simple habit tracking app to help you build good habits.

## What is it?

Habit tracking apps are widely used for monitoring different habits people want to maintain. Created with *Python 3.9.13* and having simple input functions within the command line interface, the app can be run on any device with *Python 3.9* on it. After launching the habit tracker, users are able to create, track, delete, analyze and view habits.

## Features

- Track daily and weekly habits
- Analyze streaks of habits
- Save and load habits to/from a database
- View habits - all or based on their frequency

## Requirements

For using the habit tracker please install the required packages (pytest):
    pip install pytest

## Installation

To run this project locally, clone the repository:
    git clone https://github.com/anyaanyab/habit-tracking-app

## Usage

To start, run the following command:
    python main.py

This will open the main menu where you can navigate through different functionalities of the application:


    Menu:
    1. Add Habit
    2. Track Habit
    3. Delete Habit
    4. View Habits
    5. Analyse Habits
    6. Exit
    
    Enter choice: 


To create a new habit, enter "1". After that, you will be asked to enter the new habit's name and the desired frequency: 

    Enter choice: 1
    
    Enter habit name: Run 1 km
    Enter habit frequency (daily/weekly): daily
    
    The habit was added to the list.

To track a habit, enter "2". By entering the habit name, the habit will be tracked with the current date and time:

    Enter choice: 2
    
    Enter habit name: Run 1 km
    
    The habit has been tracked.

To delete a habit, enter "3". By entering the habit name, the habit will be deleted:

    Enter choice: 3
    
    Enter habit name: Run 1 km
    
    The habit was removed from the list.

To view all, daily or weekly habits, enter "4". Depending on which habits you want to view, enter "1", "2" or "3":

    Enter choice: 4
    
    Choose which habits you want to view:
    
    1. All Habits
    
    2. Daily Habits
    
    3. Weekly Habits
    
    Enter choice: 

To view the habit you struggle with the most or longest streak for all habits or for a given habit, enter "5". Depending on what you want to view, enter "1", "2" or "3":

    Enter choice: 5 
    
    Choose what you want to analyze:
    
    1. Longest Streak Of All Habits
    
    2. Longest Streak Of One Habit
    
    3. Display Most Struggling Habit
    
    Enter choice: 

To exit the program, enter "6":

    Enter choice: 6
    
    Hope to see you tracking your habits again soon!

## Tests

 The file test_project.py contains unit tests that can be ran with pytest:
    pytest . 

 ### Enjoy the habit tracking app!
