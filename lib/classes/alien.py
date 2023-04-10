from lib import CONN, CURSOR

class Alien:

    def __init__(self, first_name, last_name, age):
        pass

    # age property goes here

    def full_name(self):
        pass

    def save(self):
        # updates the alien in the database
        pass

    @classmethod
    def query_all(cls):
        # gets all aliens in the database and returns a list of aliens as instances
        pass

    @classmethod
    def query_one(cls, id):
        # gets an alien in the database by its id and returns that alien as an instance
        pass

    @classmethod
    def average_age(cls):
        # creates and returns an average age of all aliens
        pass

    @classmethod
    def query_oldest(cls):
        # returns the oldest alien by age as an instance
        pass
