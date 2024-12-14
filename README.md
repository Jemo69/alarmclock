# alarmclock
run command
pip install -r requirements.txt
python3 simple.py
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

### Imports
```python
from kivy.app import App              # Base class for Kivy applications
from kivy.uix.boxlayout import BoxLayout  # Container widget for layout
from kivy.uix.label import Label      # Text display widget
from kivy.uix.textinput import TextInput  # Text input field
from kivy.uix.button import Button    # Clickable button widget
from kivy.clock import Clock          # Event scheduler
import time                           # Basic timing functionality
import datetime                       # Date and time handling
import pygame                         # Audio playback
```

### Main Application Class
The `AlarmApp` class inherits from `kivy.app.App` and implements the core alarm functionality.

#### UI Construction (`build` method)
The `build` method creates the user interface with the following components:
- A vertical `BoxLayout` with padding and spacing
- A `TextInput` field for entering the alarm time
- A `Label` for displaying status messages
- A "Set Alarm" button

```python
def build(self):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    # ... widget creation and configuration
    return layout
```

#### Alarm Setup (`start_alarm` method)
This method handles:
1. Time format parsing (12-hour and 24-hour)
2. Validation of user input
3. Calculation of delay until alarm
4. Scheduling of alarm trigger

Key features:
- Supports both "HH:MM AM/PM" and "HH:MM" formats
- Automatically adjusts for next-day alarms
- Provides user feedback through status messages

#### Alarm Trigger (`trigger_alarm` method)
Handles the actual alarm activation:
- Initializes pygame audio
- Loads and plays the alarm sound file
- Waits for sound completion

## Usage

### Time Input Formats
The application accepts two time formats:
- 12-hour format: "09:30 AM" or "09:30 PM"
- 24-hour format: "09:30" or "21:30"

### Setting an Alarm
1. Enter the desired time in either format
2. Click the "Set Alarm" button
3. The application will display a confirmation message with the formatted time

### Error Handling
- Invalid time formats trigger an error message
- The application validates input before setting the alarm
- Clear feedback is provided for any input errors

## Technical Notes
- The alarm sound file path must be updated to match your system configuration
- The application automatically handles next-day alarms if the specified time has already passed
- The UI is responsive and adjusts to window size changes