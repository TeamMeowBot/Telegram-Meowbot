import configparser

FILE_NAME = "bot.config"

parser = configparser.ConfigParser()
parser._interpolation = configparser.ExtendedInterpolation()
parser.read(FILE_NAME)


def configwrite():
    with open(FILE_NAME, 'w') as configfile:
        parser.write(configfile)
