import pytest

from classes.movie import Movie
from classes.viewer import Viewer

class TestViewer:
    '''Viewer in viewer.py'''

    def test_has_username(self):
        '''has the username passed into __init__.'''
        viewer = Viewer(username="gustave_the_cat")
        assert viewer.username == "gustave_the_cat"

    def test_requires_username_between_6_and_16_characters(self):
        '''requires titles to be strings between 6 and 16 characters, inclusive.'''
        with pytest.raises(Exception):
            Viewer(username="abcde")
        with pytest.raises(Exception):
            Viewer(username=123456)

    def test_requires_unique_username(self):
        '''requires username to be unique.'''
        Viewer(username="joey_the_dog")
        with pytest.raises(Exception):
            Viewer(username="joey_the_dog")

    def test_has_reviews(self):
        '''has a list of reviews.'''
        viewer = Viewer(username="fabio_the_hmstr")
        assert hasattr(viewer, "reviews")
        assert isinstance(viewer.reviews, list)

    def test_has_reviewed_movies(self):
        '''has a list of reviewed movies.'''
        viewer = Viewer(username="fanny_the_dog")
        assert hasattr(viewer, "reviewed_movies")
        assert isinstance(viewer.reviewed_movies, list)

    def test_checks_if_reviewed_movie(self):
        '''has a method "reviewed_movie" that checks if a movie has been reviewed or not.'''
        viewer = Viewer(username="lucky_the_cat")
        movie_1 = Movie("No Country for Old Men")
        viewer.reviewed_movies.append(movie_1)
        assert viewer.reviewed_movie(movie_1)
        movie_2 = Movie("The Secret Life of Pets")
        assert not viewer.reviewed_movie(movie_2)

    def test_reviews_movie(self):
        '''adds review to a viewer's reviews if it has not been reviewed, otherwise updates existing review.'''
        viewer = Viewer(username="luckier_the_cat")
        movie = Movie("The Bourne Identity")
        viewer.rate_movie(movie, 3)
        assert movie in viewer.reviewed_movies
        assert viewer.reviews[0].rating == 3
        viewer.rate_movie(movie, 4)
        assert len(viewer.reviewed_movies) == 1
        assert viewer.reviews[0]
