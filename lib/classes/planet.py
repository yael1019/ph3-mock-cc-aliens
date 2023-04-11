from lib import CONN, CURSOR

class Planet:

    def __init__(self, name, population, id = None):
        self.id = id
        self._name = name 
        self.population = population

    # name property goes here
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 3 <= len(name) <= 15:
            self._name = name 
        else:
            print('Name must be a string between 3 and 15 characters')

    name = property(get_name, set_name)

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()



    def create(self):
        sql = """
            INSERT INTO planets (name)
            VALUES (?)
        """
        CURSOR.execute(sql, [self.name])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM planets ORDER BY id DESC LIMIT 1').fetchone()[0]

    def update(self):
        sql = """
            UPDATE planets
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.id])
        CONN.commit()


    @classmethod
    def query_one(cls, id):
        # gets a planet in the database by its id and returns that planet as an instance
        pass
