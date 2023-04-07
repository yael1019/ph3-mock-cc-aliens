import pytest

from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer

class TestReview:
    '''Review in review.py'''

    def test_has_rating_viewer_movie(self):
        '''has the rating, viewer, and movie passed into __init__.'''
        movie = Movie(title="Tootsie")
        viewer = Viewer(username="pongo_the_dog")
        rating = 5
        review = Review(movie=movie, viewer=viewer, rating=rating)
        assert review.movie == movie
        assert review.viewer == viewer
        assert review.rating == rating

    def test_requires_1_to_5_rating(self):
        '''requires ratings to be between 1 and 5, inclusive.'''
        movie = Movie(title="Breathless")
        viewer = Viewer(username="snap_the_turtle")
        with pytest.raises(Exception):
            Review(movie=movie, viewer=viewer, rating="fine")
        with pytest.raises(Exception):
            Review(movie=movie, viewer=viewer, rating=0)

    def test_requires_viewer_of_viewer_class(self):
        '''requires viewer to be instance of Viewer class.'''
        movie = Movie(title="Leap Year")
        rating = 2
        with pytest.raises(Exception):
            viewer = "Penny the Dog"
            Review(movie=movie, viewer=viewer, rating=rating)

    def test_requires_movie_of_movie_class(self):
        '''requires movie to be instance of Movie class.'''
        viewer = Viewer(username="ben_the_human")
        rating = 3
        with pytest.raises(Exception):
            movie = "History of the World, Part 1"
            Review(movie=movie, viewer=viewer, rating=rating)