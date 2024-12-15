# Kivy Alarm Clock Application Documentation

## Overview
This documentation covers a Kivy-based alarm clock application that provides a simple user interface for setting alarms with both 12-hour and 24-hour time formats.

## Dependencies
The application requires the following Python libraries:
- Kivy
- pygame
- datetime
- time

## Code Structure

## Alarm Clock App with Kivy (Improved Version)

This document describes an improved version of the Alarm Clock app built with Kivy. The enhancements include adding a "Stop Alarm" button and improved code readability.

### Imports

The code imports necessary modules for building the app:

* `kivy.app`: Provides functionalities for creating Kivy applications.
* `kivy.uix.boxlayout`: Used to create container widgets with horizontal or vertical layouts.
* `kivy.uix.label`: Used to display text on the screen.
* `kivy.uix.textinput`: Used to allow users to enter text.
* `kivy.uix.button`: Used to create clickable buttons that trigger actions.
* `kivy.clock`: Provides functions to schedule events within the application.
* `datetime`: Used for working with dates and times.
* `pygame`: Used for playing audio (alarm sound).

### Class: AlarmApp

The `AlarmApp` class inherits from `kivy.app.App` and defines the core functionalities of the app.

* **build(self):** This method defines the user interface (UI) of the app when it starts.
    * Creates a vertical `BoxLayout` with padding and spacing for visual formatting.
    * Creates a `TextInput` widget with properties like `multiline=False` (single line input), a hint text to guide users on the format, and sets its height. This allows users to enter the desired alarm time.
    * Creates a `Label` widget with an initial empty text, which will be used to display the alarm status later.
    * Creates a horizontal `BoxLayout` for the buttons (`button_layout`).
        * Creates a `Button` with the text "Set Alarm", sets its height, and binds its `on_press` event to the `start_alarm` method. This button triggers setting the alarm.
        * Creates a disabled `Button` with the text "Stop Alarm" and binds its `on_press` event to the `stop_alarm` method. This button is initially disabled and becomes enabled when the alarm starts playing.
    * Adds both buttons to the `button_layout`.
    * Finally, adds the `button_layout` and the `Label` to the main vertical `BoxLayout` and returns it as the root widget of the UI.
* **start_alarm(self, instance):** This method is called when the user presses the "Set Alarm" button.
    * It tries to parse the user-entered alarm time from the `TextInput` widget.
        * Removes leading/trailing whitespaces and converts the input to uppercase for case-insensitive parsing.
        * Attempts to parse the time in 12-hour format (HH:MM AM/PM) using `datetime.datetime.strptime`.
        * If 12-hour format fails, it tries parsing in 24-hour format (HH:MM) with another `strptime` call.
        * If both parsing attempts fail, it raises a `ValueError` with a specific message to be displayed to the user.
    * Formats the alarm time with AM/PM indicator using `strftime`.
    * Gets the current date and time using `datetime.datetime.now()`.
    * Calculates the difference between the current time and the alarm time using `total_seconds`.
    * Schedules the `trigger_alarm` method to be called once after the calculated number of seconds using `Clock.schedule_once`. This schedules the actual alarm sound to play at the desired time.
    * Updates the `Label` text to display a message indicating that the alarm is set for the formatted time.
    * In case of any parsing errors (`ValueError`), it updates the `Label` text with an error message explaining the expected format.
* **trigger_alarm(self, dt):** This method is called by the `Clock` scheduler after the calculated delay.
    * Initializes the `pygame` mixer for playing audio.
    * Loads the alarm sound file (replace "/home/jemo/projects/alarmclock/sample.wav" with the path to your actual sound file).
    * Plays the loaded sound in a loop (`pygame.mixer.music.play(-1)`) using `pygame.mixer`. This ensures the alarm plays continuously until stopped.
    * Enables the "Stop Alarm" button as the alarm starts playing.
* **stop_alarm(self, instance):** This method is called when the user presses the "Stop Alarm" button.
    * Checks if Pygame is initialized (`pygame.mixer.get_init()`).
    * If initialized, stops the playing music using `pygame.mixer.music.stop()`.
    * Disables the "Stop Alarm" button.
    * Updates the `Label` text

## Commands to Run

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python3 simple.py
```

Make sure you are in the correct directory containing both the `requirements.txt` file and `simple.py` before running these commands.