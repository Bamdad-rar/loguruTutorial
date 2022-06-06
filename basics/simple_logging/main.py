from loguru import logger
import sys


"""
handler:
    The log handler is the component that effectively writes/displays a log:
    Display it in the console (via StreamHandler), 
    in a file (via FileHandler), or even by sending you an email via SMTPHandler, etc.
filter:
    used for filtering log records. this is a simple way of ensuring a logger or handler
    will only output desired logs, with the use of levels.
formatter:
    The log formatter basically enriches a log message by adding context information to it. 
    It can be useful to know when the log is sent, where (Python file, line number, method, etc.), 
    and additional context such as the thread and process (can be extremely useful when debugging 
    a multithreaded application).
"""

# removes the default handlers and what not
logger.remove()

# this wont be logged because there are no handlers present
logger.info("I won't be logged!")

# adding a handler
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

# this will be logged
logger.info("I'm being called!")


# adding two handlers
logger.add("info.log",colorize=False, format="[<green>{time:YY-MM-DD@HH:mm:ss}</green>/<red>{level}</red>]: {message}", level="INFO")
logger.add(sys.stdout,colorize=True, format="[<green>{time:YY-MM-DD@HH:mm:ss}</green>/<red>{level}</red>]: {message}", level="INFO")

logger.info("I will be logged both into all three declared handlers")