from logging import getLogger, FileHandler, DEBUG
# name : __name__
# how to use
# logger=createLogger(__name__,"./test.log")
# logger.debug("test")
def create_logger(name,log_filepath):
    logger = getLogger(name)
    handler =FileHandler(log_filepath)
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    return logger