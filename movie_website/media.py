# -*- coding: UTF-8 -*-
# Created by xiongwei at 2018/1/6

class Movie:
	"""保存电影相关的属性"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_url = trailer_url


