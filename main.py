import time
import pygame
import soundfile as sf
from plyer import notification


def main():
    # Define Some Varibles
    number = 0
    audio_file = "Ringtone Coffin Dance.mp3"
    title = "Take a Glass of Water"
    message = "Hey Praddymn Yadav! I am Watching for a Long time That you Are Working with your Full Dedication but Working This Hard and Ignoring Your Health is not a good Thing but I am Here to Remind You to Take a Glass of Water Get up from Chair and Walk a Little Bit it will Help You to Stay Healthy and it will also help me to stay Happy. Thank You."

    # Start the While Loop
    while True:
        number += 1
        trigger_notification(number, title, message, audio_file)
        time.sleep(30 * 60)


def trigger_notification(number, title, message, ringtone):
    # Trigger the Notification
    notification.notify(
        title=(title + " - " + str(number)),
        message=message,
        app_icon="logo.ico",
        timeout=10,
    )

    # Initialize Pygame
    pygame.init()

    # Load and Play the Ringtone
    pygame.mixer.music.load(ringtone)
    pygame.mixer.music.play()

    # Start Timer for 15 Seconds
    time.sleep(get_audio_length(ringtone))

    # Stop the Ringtone
    pygame.mixer.music.stop()

    # Quit Pygame
    pygame.quit()


# Create a Function for Checking Length of Audio
def get_audio_length(filename):
    with sf.SoundFile(filename) as f:
        return len(f) / f.samplerate


main()
