from lib import CONN, CURSOR

class Planet:

    def __init__(self, name, population, id = None):
        self.id = id
        self.name = name 
        self.population = population

    def __repr__(self) -> str:
        return f'<Planet id = {self.id} name = {self.name} population = {self.population}>'

    # name property goes here
    def get_name(self):
        if hasattr(self, '_name'):
            return self._name
        else:
            print('Invalid Name')
    
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
            SET name = ?, population =?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.population, self.id])
        CONN.commit()


    @classmethod
    def query_one(cls, id):
        sql = """
            SELECT * FROM planets
            WHERE id = ?
        """
        one = CURSOR.execute(sql, [id]).fetchone()
        if one:
            return Planet(one[1], None, one[0])
        else:
            print('Planet does not exist')

    @classmethod
    def query_all(cls):
        sql = """
            SELECT * FROM planets
        """
        all = CURSOR.execute(sql).fetchall()
        return [Planet(data[1], None, data[0]) for data in all]

    def destroy(self):
        sql = """
            DELETE FROM planets
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.id])
        CONN.commit()

    def add_column(self):
        sql = """
            ALTER TABLE planets
            ADD COLUMN population INTEGER
        """
        CURSOR.execute(sql)
        CONN.commit()
        self.update()

