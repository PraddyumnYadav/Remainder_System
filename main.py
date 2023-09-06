import time
import pygame
import soundfile as sf
from plyer import notification


def trigger_notification(number, title, message, ringtone):
    # Trigger the Notification
    notification.notify(
        title=(title + " - " + str(number)),
        message=message,
        app_icon="logo.jpeg",
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
