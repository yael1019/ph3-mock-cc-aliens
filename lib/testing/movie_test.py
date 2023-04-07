import pytest

from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer

class TestMovie:
    '''Movie in movie.py'''

    def test_has_title(self):
        '''has the title passed into __init__.'''
        movie = Movie(title="Avatar: The Way of Water")
        assert movie.title == "Avatar: The Way of Water"

    def test_requires_nonzero_string_title(self):
        '''requires titles to be strings of >0 characters.'''
        with pytest.raises(Exception):
            Movie(title=1)
        with pytest.raises(Exception):
            Movie(title="")
    
    def test_has_reviews(self):
        '''contains an instance attribute, reviews, a list of its reviews.'''
        movie = Movie(title="Scarface")
        assert hasattr(movie, "reviews")
        assert isinstance(movie.reviews, list)

    def test_has_reviewers(self):
        '''contains an instance attribute, reviewers, a list of its viewers who left reviews.'''
        movie = Movie(title="Rashomon")
        assert hasattr(movie, "reviewers")
        assert isinstance(movie.reviewers, list)

    def test_calculates_average_rating(self):
        '''has a method "average_rating" that returns the average of self.reviews.'''
        movie = Movie(title="My Neighbor Totoro")

        Review(viewer=Viewer("Jeffrey"), movie=movie, rating=1)
        Review(viewer=Viewer("William"), movie=movie, rating=3)
        Review(viewer=Viewer("Benjamin"), movie=movie, rating=2)
        Review(viewer=Viewer("Katherine"), movie=movie, rating=4)
        Review(viewer=Viewer("Catherine"), movie=movie, rating=5)
        Review(viewer=Viewer("Kathryn"), movie=movie, rating=4)
        Review(viewer=Viewer("Katrina"), movie=movie, rating=2)
        Review(viewer=Viewer("Samwise"), movie=movie, rating=3)

        assert movie.average_rating() == 3

    def test_shows_highest_rated(self):
        '''has a method "highest_rated" that returns the highest rated movie.'''
        Movie.all = []
        Viewer.all = []
        movie_1 = Movie(title="Avatar: The Way of Water")
        Review(viewer=Viewer("Jeffrey"), movie=movie_1, rating=1)
        Review(viewer=Viewer("William"), movie=movie_1, rating=3)
        Review(viewer=Viewer("Benjamin"), movie=movie_1, rating=2)
        movie_2 = Movie(title="Scarface")
        Review(viewer=Viewer("Katherine"), movie=movie_2, rating=4)
        Review(viewer=Viewer("Catherine"), movie=movie_2, rating=5)
        movie_3 = Movie(title="Rashomon")
        Review(viewer=Viewer("Kathryn"), movie=movie_3, rating=5)
        Review(viewer=Viewer("Katrina"), movie=movie_3, rating=5)
        movie_4 = Movie(title="My Neighbor Totoro")
        Review(viewer=Viewer("Samwise"), movie=movie_4, rating=3)
        assert Movie.highest_rated().title == "Rashomon"
