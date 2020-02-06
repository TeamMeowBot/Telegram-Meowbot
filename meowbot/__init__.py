import configparser

settings = configparser.ConfigParser()
settings._interpolation = configparser.ExtendedInterpolation()
settings.read("bot.config")
print(settings.sections())

