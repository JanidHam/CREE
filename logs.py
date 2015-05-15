import logging

#logging.error("error")
logger = logging.getLogger(__name__)
#logger = logging.getLogger("INFO")
logger.setLevel(logging.DEBUG)

# create a file handler

handler = logging.FileHandler('logs.log')
handler.setLevel(logging.DEBUG)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)