import logging
import os
import sys

dirname = os.path.dirname(__file__)

#exec(open(dirname+"\\simulatedata.py").read())


# Debug: These are used to give Detailed information,
#        typically of interest only when diagnosing problems.

# Info: These are used to Confirm that things are working as expected

# Warning: These are used an indication that something unexpected happened,
#          or indicative of some problem in the near future

# Error: This tells that due to a more serious problem,
#        the software has not been able to perform some function

# Critical: This tells serious error, indicating that the program
#           itself may be unable to continue running

# logging.basicConfig(level=logging.DEBUG)

#Creating an object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
#file_handler.setFilemode("w")

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#logging.basicConfig(filename="test.log",
#                    level=logging.INFO,
#                    format="%(asctime)s:%(levelname)s:%(message)s",
#                    filemode="w")

#Setting the threshold of logger to DEBUG
#logger.setLevel(logging.DEBUG)

#Test messages
#logger.debug("Harmless debug Message")
#logger.info("Just an information")
#logger.warning("Its a Warning")
#logger.error("Did you try to divide by zero")
#logger.critical("Internet is down")

logger.error(2+2)
logger.exception('3+3')
logger.debug(dirname)
logger.info(2+2)
logging.info(__name__)
