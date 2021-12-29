import configparser

config = configparser.RawConfigParser()
configFilePath = ".\\Configurations\\config.ini"
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common-info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common-info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'password')
        return password
