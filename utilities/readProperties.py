import configurations
import configparser

from testCases.conftest import project_root

config = configparser.RawConfigParser()
config.read(f"{project_root}/configurations/config.ini")


class readConfig:

    @staticmethod
    def getURL():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


rc = readConfig()
print(rc)
