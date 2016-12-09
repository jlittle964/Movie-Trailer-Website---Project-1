import webbrowser

class Movie():
	"""...Defines the instance..."""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""...[init will look for these 4 values and give them a value to be called later]..."""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer (self):
		webbrowser.open(self.trailer_youtube_url)
