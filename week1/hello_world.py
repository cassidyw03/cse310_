import time
import os

def clear():
        os.system('clear')

def flash_text(text, duration=5, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        print(text)
        time.sleep(interval)
        clear()
        time.sleep(interval)

# Example usage
flash_text("Hello, World!", duration=10, interval=0.3)