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
	for restaurant, score in sorted(restaurant_rating_dict.items()):
		print ("{} is rated at {}.".format(restaurant, score))

	return restaurant_rating_dict

def add_ratings_scores(rest_dict):
	"""takes user input for a retaurant and it's score and either update or add"""


	new_restaurant = input("What restaurant did you visit? ")
	new_score = input("What score from 1 to 5 would you give it? ")
	new_score = int(new_score)
	if new_restaurant in rest_dict: 
		rest_dict[new_restaurant] += new_score

	else: 
		rest_dict[new_restaurant] = new_score

	print(rest_dict)

r = restaurant_rating_printer("scores.txt")
add_ratings_scores(r)