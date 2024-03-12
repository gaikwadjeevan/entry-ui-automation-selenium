import logging

from testCases.conftest import project_root


class logGen:

    @staticmethod
    def getLogGen():
        logging.basicConfig(
            filename=f"{project_root}/logs/automation.log",
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S', force=True,
        )
        print("Started logfile creation")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
