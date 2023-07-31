import os
import random
import time
import webbrowser
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button

# Function to get the full path of the script's directory
def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

# Function to read the URL list from urllist.txt
def read_url_list():
    script_dir = get_script_directory()
    file_path = os.path.join(script_dir, 'urllist.txt')
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

# Function to read the list of words from wordlist.txt
def read_word_list():
    script_dir = get_script_directory()
    file_path = os.path.join(script_dir, 'wordlist.txt')
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to perform a smooth and natural scroll on the webpage
def smooth_scroll():
    # Implementation of smooth_scroll() as before
    pass

# Function to simulate human-like keyboard typing with random delays
def human_like_typing(words, words_per_minute):
    keyboard = KeyboardController()
    for word in words:
        keyboard.type(word + ' ')
        time.sleep(random.uniform(60 / words_per_minute - 0.05, 60 / words_per_minute + 0.05))

# Function to simulate human-like mouse movements to different sections of the screen
def human_like_mouse_movement(target_x, target_y):
    mouse = MouseController()
    current_x, current_y = mouse.position
    distance = ((target_x - current_x) ** 2 + (target_y - current_y) ** 2) ** 0.5
    steps = int(distance / 10)  # Divide the movement into smaller steps

    for step in range(steps):
        next_x = int(current_x + (target_x - current_x) * step / steps)
        next_y = int(current_y + (target_y - current_y) * step / steps)

        # Add jitter to the mouse movement
        jitter_x = random.randint(-5, 5)
        jitter_y = random.randint(-5, 5)
        next_x += jitter_x
        next_y += jitter_y

        mouse.position = (next_x, next_y)
        time.sleep(random.uniform(0.1, 0.2))  # Random delay between steps

    # Finally, move the mouse to the exact target position with a small delay
    mouse.position = (target_x, target_y)
    time.sleep(random.uniform(0.1, 0.2))

# Function to perform mouse click with random button (left or right)
def random_mouse_click():
    mouse = MouseController()
    button = random.choice([Button.left, Button.right])
    mouse.click(button)

def main():
    urls = read_url_list()
    words = read_word_list()

    start_time = time.time()
    end_time = start_time + 300  # 5 minutes (5 minutes * 60 seconds/minute)

    try:
        while time.time() < end_time:
            # Open a random webpage from the URL list
            url = random.choice(urls)
            webbrowser.open_new_tab(url)

            # Wait for the webpage to load (you might need to adjust this delay)
            time.sleep(5)

            # Perform a smooth and natural scroll on the webpage
            smooth_scroll()

            # Randomly select three words for typing in this iteration
            selected_words = random.sample(words, 3)

            # Simulate human-like keyboard typing with random delays
            words_per_minute = random.randint(38, 40)  # Typing speed between 38 and 40 WPM
            human_like_typing(selected_words, words_per_minute)

            # Simulate human-like mouse movements to different sections of the screen
            for _ in range(random.randint(3, 5)):
                target_x = random.randint(100, 500)  # Change the range as needed
                target_y = random.randint(100, 500)  # Change the range as needed
                human_like_mouse_movement(target_x, target_y)

            # Random mouse click
            random_mouse_click()

            # Wait for a random amount of time before the next iteration (adjust as needed)
            time.sleep(random.randint(5, 15))

    except KeyboardInterrupt:
        print("Script stopped manually.")

if __name__ == "__main__":
    main()
