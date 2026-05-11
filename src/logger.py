import logging
import os
from datetime import datetime

# File name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path to logs folder
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO
)


#Documentation :


"""
======================== FILE EXPLANATION ========================

PURPOSE OF THIS FILE:
This file sets up a logging system for the project.

Instead of printing important events/errors manually,
this file automatically stores logs inside a log file.

These logs help in:

1. Debugging errors
2. Tracking program execution
3. Monitoring application behavior
4. Keeping permanent records of important events


----------------------------------------------------------------
1) import logging
----------------------------------------------------------------

import logging

-> logging is a built-in Python module.

Purpose:
Used to record messages/events during program execution.

It can store logs in:
- terminal
- files
- remote servers
- databases

Common logging levels:

logging.debug()      -> detailed debugging info
logging.info()       -> normal program events
logging.warning()    -> warning messages
logging.error()      -> errors
logging.critical()   -> severe errors


Example:

logging.info("Program started")


----------------------------------------------------------------
2) import os
----------------------------------------------------------------

import os

-> os is a built-in Python module.

Purpose:
Allows interaction with operating system.

Used for:

- creating folders
- navigating file paths
- handling directories
- working with file systems


Examples:

os.getcwd()      -> current working directory
os.mkdir()       -> create single folder
os.makedirs()    -> create nested folders
os.path.join()   -> safely combine paths


----------------------------------------------------------------
3) from datetime import datetime
----------------------------------------------------------------

from datetime import datetime

-> datetime is a built-in Python module.
-> datetime class helps work with date and time.


Used here to generate unique log file names.


Example:

datetime.now()

returns current time:

2026-05-11 17:30:45


----------------------------------------------------------------
4) LOG_FILE variable
----------------------------------------------------------------

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Purpose:
Creates unique log file name based on current date/time.

strftime() converts datetime object into formatted string.

Format breakdown:

%m -> month
%d -> day
%Y -> year
%H -> hour
%M -> minute
%S -> second


Example output:

05_11_2026_17_30_45.log


Why needed?
Prevents old logs from being overwritten.


----------------------------------------------------------------
5) datetime.now()
----------------------------------------------------------------

Returns current local date and time.


Example:

2026-05-11 17:30:45


----------------------------------------------------------------
6) strftime()
----------------------------------------------------------------

Converts datetime object into custom string format.


Example:

datetime.now().strftime("%Y")

Output:

2026


----------------------------------------------------------------
7) logs_path variable
----------------------------------------------------------------

logs_path = os.path.join(os.getcwd(), "logs")

Purpose:
Creates path for logs directory.


Breakdown:

os.getcwd()
-> gets current working directory

Example:

/home/anshuman/project


"os.getcwd(), "logs"

creates:

/home/anshuman/project/logs


----------------------------------------------------------------
8) os.getcwd()
----------------------------------------------------------------

Returns current working directory where program runs.


Example:

/home/user/project


----------------------------------------------------------------
9) os.path.join()
----------------------------------------------------------------

Safely combines file/folder paths.

Why use it?

Different OS use different path separators:

Windows:
\

Linux/Mac:
/

os.path.join() handles this automatically.


Example:

os.path.join("folder","file.txt")

Output:

folder/file.txt


----------------------------------------------------------------
10) os.makedirs()
----------------------------------------------------------------

os.makedirs(logs_path, exist_ok=True)

Purpose:
Creates logs folder.

If folder doesn't exist:
-> creates it

If folder already exists:
-> no error due to exist_ok=True


Without exist_ok=True:
Python would raise FileExistsError


----------------------------------------------------------------
11) LOG_FILE_PATH variable
----------------------------------------------------------------

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

Purpose:
Creates complete path of final log file.


Example:

/home/project/logs/05_11_2026_17_30_45.log


----------------------------------------------------------------
12) logging.basicConfig()
----------------------------------------------------------------

This configures entire logging system.


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=...,
    level=logging.INFO
)


It tells Python:

- where to store logs
- how logs should look
- what logs should be recorded


----------------------------------------------------------------
13) filename parameter
----------------------------------------------------------------

filename=LOG_FILE_PATH

Tells logging module where to save logs.


Example:

logs/05_11_2026_17_30_45.log


----------------------------------------------------------------
14) format parameter
----------------------------------------------------------------

format="[ %(asctime)s ] %(lineno)d - %(levelname)s - %(message)s"

Controls appearance of log message.


%(asctime)s
-> time when log happened

%(lineno)d
-> line number where log was triggered

%(levelname)s
-> log type (INFO/ERROR/etc)

%(message)s
-> actual message


Example output:

[ 2026-05-11 17:30:45 ] 22 - INFO - Logging has started


----------------------------------------------------------------
15) level parameter
----------------------------------------------------------------

level=logging.INFO

Tells logger to record INFO level and above.

It records:

INFO
WARNING
ERROR
CRITICAL

It ignores:

DEBUG


----------------------------------------------------------------
16) if __name__ == "__main__":
----------------------------------------------------------------

This checks whether file is being run directly.


If file is run directly:

python logger.py

Then code inside this block runs.


If imported into another file:

from logger import logging

Then this block won't run.


----------------------------------------------------------------
17) __name__
----------------------------------------------------------------

Built-in Python variable.

If file runs directly:

__name__ = "__main__"

If imported:

__name__ = file/module name


----------------------------------------------------------------
18) logging.info()
----------------------------------------------------------------

logging.info("Logging has started")

Creates an INFO log entry.


Output in log file:

[ timestamp ] line_number - INFO - Logging has started


----------------------------------------------------------------
FULL EXECUTION FLOW
----------------------------------------------------------------

Program starts
    ↓
Imports modules
    ↓
Creates unique log file name
    ↓
Creates logs folder
    ↓
Creates full log file path
    ↓
Configures logging system
    ↓
Writes log messages


----------------------------------------------------------------
EXAMPLE OUTPUT FILE
----------------------------------------------------------------

logs/
    05_11_2026_17_30_45.log


Inside file:

[ 2026-05-11 17:30:45 ] 22 - INFO - Logging has started


===============================================================
"""