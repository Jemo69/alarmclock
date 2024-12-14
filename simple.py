# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.clock import Clock
# import time
# import pygame

# class AlarmApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='vertical')

#         self.alarm_time = TextInput(multiline=False)
#         layout.add_widget(self.alarm_time)

#         self.alarm_label = Label(text="")
#         layout.add_widget(self.alarm_label)

#         start_button = Button(text="Set Alarm")
#         start_button.bind(on_press=self.start_alarm)
#         layout.add_widget(start_button)

#         return layout

#     def start_alarm(self, instance):
#         try:
#             alarm_time = int(self.alarm_time.text)
#             self.alarm_label.text = f"Alarm set for {alarm_time} seconds"
#             Clock.schedule_once(self.trigger_alarm, alarm_time)
#         except ValueError:
#             self.alarm_label.text = "Invalid input. Please enter a number."

#     def trigger_alarm(self, dt):
#         pygame.mixer.init()
#         pygame.mixer.music.load("/home/jemo/projects/alarmclock/sample.wav")  # Replace with your sound file
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             pass

# if __name__ == '__main__':
#     AlarmApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import time
import datetime
import pygame

class AlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.alarm_time_input = TextInput(multiline=False, hint_text="Enter time in HH:MM format", size_hint_y=None, height=40)
        layout.add_widget(self.alarm_time_input)

        self.alarm_label = Label(text="")
        layout.add_widget(self.alarm_label)

        start_button = Button(text="Set Alarm" ,size_hint_y=None, height=40)
        start_button.bind(on_press=self.start_alarm)
        layout.add_widget(start_button)

        return layout
    def start_alarm(self, instance):
        try:
            alarm_time_str = self.alarm_time_input.text
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")

            # Format the alarm time with AM/PM indicator
            formatted_alarm_time = alarm_time.strftime("%I:%M %p")

            current_time = datetime.datetime.now()
            time_difference = alarm_time - current_time
            seconds_to_wait = time_difference.total_seconds()

            Clock.schedule_once(self.trigger_alarm, seconds_to_wait)
            self.alarm_label.text = f"Alarm set for {formatted_alarm_time}"
        except ValueError:
            self.alarm_label.text = "Invalid time format. Please enter in HH:MM format."

    

    def trigger_alarm(self, dt):
        pygame.mixer.init()
        pygame.mixer.music.load("/home/jemo/projects/alarmclock/sample.wav")  # Replace with your sound file
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

if __name__ == '__main__':
    AlarmApp().run()