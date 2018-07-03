"""Restaurant rating lister."""
def restaurant_rating_printer(file):
	"""takes restaurant and ratings from file and puts in dict."""

	restaurant_rating_dict = {}
	f = open("scores.txt")

	for line in f:
		line = line.rstrip()
		entries = line.split(":")
		restaurant = entries[0]
		score = entries[1]

		restaurant_rating_dict[restaurant] = score

		#sorted_restaurants = sorted(restaurant_rating_dict.items())
	# print (sorted(restaurant_rating_dict.items()))
	for restaurant,score in sorted(restaurant_rating_dict.items()):
		print ("{} is rated at {}.".format(restaurant, score))

restaurant_rating_printer("scores.txt")