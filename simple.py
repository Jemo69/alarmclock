import time
import pygame

def alarm(duration, sound_file):
    time.sleep(duration)
    
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

alarm_time = 3
sound_file = "/home/jemo/projects/alarmclock/sample.wav"
alarm(alarm_time, sound_file)   