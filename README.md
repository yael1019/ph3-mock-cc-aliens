# Object Relations Code Challenge - Aliens at Home

For this challenge, we'll be working with a domain that involves aliens and their home planets.

We have two models: `Alien` and `Planet`.

A `Planet` has many `Alien`s. An `Alien` belongs to a `Planet`.

`Planet` - `Alien` is a one to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods
- SQL queries
- ORM methods
- Foreign keys

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

<!-- TODO: THIS MIGHT NOT BE TRUE SO DELETE IF NOT -->
**Remember!** This code challenge is test-driven. You can run `pytest` at any
time to check your work.
You'll need to create your own sample instances so that you can try out your
code on your own. Make sure your relationships and methods work in the console
before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

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

### Object Relationship Methods

#### Alien

- `query_planet()`
  - Returns the planet the alien lives on via the planet_id
  - Returned Planets must be `Planet` instances

#### Planet

- `query_aliens()`
  - Returns all aliens living on a planet via their planet_id
  - Returned Aliens must be in a list of `Alien` instances

### Aggregate and Association Methods

#### Alien

- `Alien classmethod query_average_age()`
  - Returns the average age for all aliens in the database
  - The average is the sum of all ages divided by the number of aliens (think `len()`)

- `Alien classmethod query_oldest()`
  - Returns the oldest alien in the database as an instance
