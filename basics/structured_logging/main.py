from loguru import logger
import sys

""" giving logs a json structure """
logger.remove()
logger.add(sys.stdout,serialize=True)

logger.info("this will give us a json structured log")

""" contexualizing logs """

logger.remove()

# extra is a record attribute which helps us contextualize our logger
# extra is a dictionary
logger.add(sys.stdout,format="{extra[ip]} {extra[user]} {time} {level} {message}")
logger.add(sys.stdout,format="{extra} {message}")
context_logger = logger.bind(ip="127.0.0.1", user="bamdad")
context_logger.info('holy shit something happened')
