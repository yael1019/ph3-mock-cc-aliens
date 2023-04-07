from . import CONN, CURSOR
from classes.alien import Alien

class Planet:

    def __init__(self, name):
        pass

    # name property goes here

    def save(self):
        # updates the planet in the database
        pass

    def query_aliens(self):
        # gets all aliens in the database associated with the planet and returns them as instances
        pass

    @classmethod
    def query_one(cls, id):
        # gets a planet in the database by its id and returns that planet as an instance
        pass
