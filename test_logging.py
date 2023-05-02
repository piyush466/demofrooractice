import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)



    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    logger.debug("this is  debug statement")

    logger.info("this is  information   statement")

    logger.warning("this is  warning statement")

    logger.error("this is majjor error statement")

    logger.critical("thisiid critiacl issue")