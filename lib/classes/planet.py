from lib import CONN, CURSOR

class Planet:

    def __init__(self, name):
        pass

    # name property goes here

    def save(self):
        # updates the planet in the database
        pass

    @classmethod
    def query_one(cls, id):
        # gets a planet in the database by its id and returns that planet as an instance
        pass
