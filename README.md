# Object Relations Code Challenge - Aliens at Home

For this challenge, we'll be working with a domain that involves aliens and their home planets.

We have two models: `Alien` and `Planet`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

You will not have to build the tables as they'll be created for you
automatically when you first run `debug.py`.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Alien

- `Alien __init__(self, first_name, last_name, age)`
  - `Alien` is initialized with a first_name, last_name (string) and age (integer)
  - Age **can be** changed after the `Alien` is initialized
- `Alien property age()`
  - Returns the `Alien`'s age
  - Age must be an integer 0 or greater
- `Alien full_name()`
  - Returns the alien's first_name and last_name in a string
  - Format the string like this: `"first_name last_name"`
- `Alien save()`
  - Creates an alien in the database if an alien with the same id doesn't exist
  - Updates an alien in the database if an alien with the same id exists
- `Alien classmethod query_all()`
  - Returns a list of alien instances based on rows in the database
  - The return value ought to be an array of Alien instances
- `Alien classmethod query_one(id)`
  - Returns an alien instance from the database with the matching id
  - The return value ought to be an Alien instance
  - Return None if no Planet exists with that id
- `Alien delete()`
  - Deletes the Alien from the database
  - This method returns `None`

#### Planet

- `Planet __init__(self, name)`
  - `Planet` is initialized with a name (string) and population (integer)
  - Population **can be** changed after the Planet is initialized
- `Planet property name()`
  - Returns the Planet's name
  - Names must be strings between 3 and 15 characters long
- `Planet save()`
  - Creates a planet in the database if a planet with the same id doesn't exist
  - Updates a planet in the database if a planet with the same id exists
- `Planet classmethod query_one(id)`
  - Returns a planet instance from the database with the matching id
  - The return value ought to be a Planet instance
  - Return None if no Planet exists with that id
- `BONUS: Full CRUD with Planet`
  - Build out the methods for `.query_all()` and `.delete()`

### Aggregate and Association Methods

#### Alien

- `Alien classmethod query_average_age()`
  - Returns the average age for all aliens in the database
  - The average is the sum of all ages divided by the number of aliens (think `len()`)

- `Alien classmethod query_oldest()`
  - Returns the oldest alien in the database as an instance
