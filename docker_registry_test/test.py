import time
import os
import logging

logger = logging.getLogger("test")

i = 0
while True:
    logger.warning("this is running")
    logger.warning(f"cwd is {os.getcwd()}")
    time.sleep(1)
    i += 1
    if i == 5:
        break
