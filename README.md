# Key Logger

This Python script logs all key presses to a file named `key_log.txt` using the `pynput` library. The script runs continuously and records each key press along with a timestamp until the "Escape" key (`Key.esc`) is pressed to stop the logging.

## Prerequisites

- Python 3.x
- `pynput` library

## Installation

1. **Clone the repository or download the script:**
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
## Usage
Run the script:
`python key_logger.py`
The script will start logging all key presses to `key_log.txt` file in the same directory:

The log entries will be in the format: (key) is pressed at : timestamp.
To stop the script, press the "Escape" key (Key.esc).
