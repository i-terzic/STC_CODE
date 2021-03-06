from app import create_app
from flask_script import Manager, Shell


# change parameter to testing/development for different cofigurations
app = create_app('development')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
