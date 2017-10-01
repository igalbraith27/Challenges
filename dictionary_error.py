def dictionarypy(dictionary, key):
	try:
		return dictionary[key]
	except KeyError:
		print("Nice Exception")
		dictionary[key] = "no value here"
		return "no value found"