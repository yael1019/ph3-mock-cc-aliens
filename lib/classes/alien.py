from lib import CONN, CURSOR

class Alien:

    def __init__(self, first_name, last_name, age, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        # not using the underscore will pass this through the age property, so will not let you initialize with an invalid value
        # if we initialize with an invalid age then it will go through the getter fn and print the else statement bc _age was not set to anything
        # so we do not have the attr _age, it was never initialized
        self.age = age

    def __repr__(self) -> str:
        return f'< Alien id = {self.id} first_name = {self.first_name} last_name = {self.last_name} age = {self.age} >'
    
    # age property goes here
    def get_age(self):
        # checking if we have the attribute _age then return the age 
        if hasattr(self, '_age'):
            return self._age
        else:
            print('Invalid age')
    
    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            print('Age must be a number greater or equal to zero')

    age = property(get_age, set_age)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self):
        if self.id:
            self._update()
        else:
            self._create()
    
    # by putting the underscore we are saying that this is private we should not be calling _create(), instead we should be calling save()
    def _create(self):
        sql = """
            INSERT INTO aliens (first_name, last_name, age)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM aliens ORDER BY id DESC LIMIT 1').fetchone()[0]

    def _update(self):
        sql = """
            UPDATE aliens 
            SET first_name = ?, last_name = ?, age =?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age, self.id])
        CONN.commit()


    @classmethod
    def query_all(cls):
        sql = """
            SELECT * FROM aliens
        """
        all = CURSOR.execute(sql).fetchall()
        result = [Alien(data[1], data[2], data[3], data[0]) for data in all]
        return result

    @classmethod
    def query_one(cls, id):
        sql = """
            SELECT * FROM aliens 
            WHERE id = ?
        """
        one = CURSOR.execute(sql, [id]).fetchone()
        if one:
            alien = Alien(one[1], one[2], one[3])
            alien.id = one[0]
            return alien
        else:
            print('This alien does not exist')
        
        # OR -- we can use the list returned from query_all to grab the alien we want 
        # all = cls.query_all()
        # for alien in all:
        #     if alien.id == id:
        #         return alien

    def destroy(self):
        sql = """
            DELETE FROM aliens
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.id])
        CONN.commit()


    @classmethod
    def average_age(cls):
        sql = """
            SELECT age 
            FROM aliens
        """
        age_list = CURSOR.execute(sql).fetchall()
        ages = [age[0] for age in age_list]
        avg = sum(ages) / len(ages)
        return avg

        # OR we can do this calling the query_all aswell

    @classmethod
    def query_oldest(cls):
        sql = """
            SELECT * FROM aliens 
            WHERE age = (SELECT MAX(age) FROM aliens)
        """
        oldest = CURSOR.execute(sql).fetchone()
        oldest_repr = Alien(oldest[1], oldest[2], oldest[3], oldest[0])
        return oldest_repr

        # OR 
        # sql = """
        #     SELECT * FROM aliens
        #     ORDER by age DESC
        # """


# jane = Alien('Jane', 'Doe', 40)