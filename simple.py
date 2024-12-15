from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import datetime
import pygame

class AlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.alarm_time_input = TextInput(
            multiline=False, 
            hint_text="Enter time (HH:MM AM/PM or 24hr format)", 
            size_hint_y=None, 
            height=40
        )
        layout.add_widget(self.alarm_time_input)

        self.alarm_label = Label(text="")
        layout.add_widget(self.alarm_label)

        # Create buttons layout
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        
        start_button = Button(text="Set Alarm")
        start_button.bind(on_press=self.start_alarm)
        button_layout.add_widget(start_button)

        # Add Stop button
        self.stop_button = Button(text="Stop Alarm", disabled=True)  # Initially disabled
        self.stop_button.bind(on_press=self.stop_alarm)
        button_layout.add_widget(self.stop_button)

        layout.add_widget(button_layout)
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
        pygame.mixer.music.load("/home/jemo/projects/alarmclock/sample.wav")
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        self.stop_button.disabled = False  # Enable stop button when alarm starts

    def stop_alarm(self, instance):
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
        self.stop_button.disabled = True  # Disable stop button after stopping
        self.alarm_label.text = "Alarm stopped"

if __name__ == '__main__':
    AlarmApp().run()