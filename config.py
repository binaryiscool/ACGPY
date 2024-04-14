import configparser

def load_options(filename, headername):
        options = {}
        config = configparser.ConfigParser()
        config.read('Assets/Data/' + filename)

        if headername in config:
            options = dict(config[headername])
        return options