import os
from horus.apps import create_app


config_file = os.path.join(os.path.dirname(os.path.realpath(__file__))
                           , 'config.py')
print config_file
app = create_app(config_file)


if __name__ == '__main__':
    app.run()
