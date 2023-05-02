import logging


def test_piyush():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('Piyushlogs.log')
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)

    logger.debug("This is a debug")
    logger.info("This is Info")
    logger.error("This is a error")
    logger.warning("this is a warning")
    logger.critical("This is a critical")