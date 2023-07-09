
from configparser import ConfigParser

Conf = ConfigParser()

try:
    '''Full path'''

    # Conf.read("D:/TestAutomation/GeneralFiles/Conf.cfg")

    '''Current Directory Path'''

    Conf.read("./GeneralFiles/Conf.cfg")
    print(Conf.get("Section","usr"))

except Exception as e:
    print(e)
