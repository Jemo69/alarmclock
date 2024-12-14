import time
import simpleaudio as sa

def alarm(duration, sound_file):
    time.sleep(duration)

    # Load the sound file
    wave_obj = sa.WaveObject.from_wave_file(sound_file)

    # Play the sound
    play_obj = wave_obj.play()
    play_obj.wait_done()
alarm_time = 3 # Adjust this to your desired time
sound_file = "sample.wav"  # Replace with your desired sound file

alarm(alarm_time, sound_file)