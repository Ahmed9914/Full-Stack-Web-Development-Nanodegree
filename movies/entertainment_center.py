# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:25:04 2017

@author: Ravi Jain
"""

import media
import fresh_tomatoes

idiots = media.Movie("3 Idiots",
                     "In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook.",
                     "https://i.pinimg.com/originals/32/0b/b7/320bb7b2174ef3ae6142788240055b33.jpg",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w")

theri = media.Movie("Theri",
                    "Concealing his identity, DCP Vijaya Kumar goes into self-inflicted exile to bring up his daughter.",
                    "https://upload.wikimedia.org/wikipedia/en/d/db/Theri_poster.jpg",
                    "http://www.youtube.com/watch?v=ZK4uGLpkAKk")


# list of all movies
movies = [idiots, theri]

print(media.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)
