def readfile(file):
	"""	Returns a list of words given in a file.
	"""

	f = open(file)

	words = [word.rstrip() for word in f]
	return words

def pickwords(dictionary, *args):
	""" Returns a list of words in a sequence given indexes.
	"""

	if(len(args) < 1):
		return None
	else:
		words = []

		for index in args:
			words.append(dictionary[index])

		return words

def scrabblescore(string):
	"""	Returns the scrabble score from a given string.
	"""

	string = string.lower()
	score = 0
	scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 
		1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

	for char in string:
		index = ord(char) - ord('a')
		score += scores[index]

	return score

def maxscrabblescore(dictionary, string):
	"""	Returns the highest possible score given a word and its unscrambled
	words from a given dictionary.
	"""
	
	words = searchanagrams(dictionary, string)
	max_score = 0

	for word in words:
		max_score += scrabblescore(word)

	return max_score

def checkword(string, word):
	"""	Returns True if the second word can be found using the letter in the
	first word, otherwise False.
	"""

	count = 0

	for char in word:
		if char in string:
			index = string.index(char)
			string = string[:index] + string[index + 1:]
			count += 1

	if count == len(word):
		return True
	else:
		return False

def searchanagrams(dictionary, string, strict = 0):
	"""	Returns a list of all words that can be formed from a word
	from a given dictionary.

	Only returns anagrams of the same word length if strict = 1.
	"""

	words = []

	for word in dictionary:
		if checkword(string, word):
			if strict == 1 and len(word) != len(string):
				continue
			words.append(word)

	return words

def combinewords(iterable):
	"""	Returns the shortest string that can be formed from a given
	list of words.
	"""

	min_word = [0] * 26
	combined_word = ""

	for i in iterable:
		letter_count = [0] * 26

		for letter in i:
			index = ord(letter) - ord('a')
			letter_count[index] += 1

		for j in range(26):
			if(min_word[j] < letter_count[j]):
				min_word[j] = letter_count[j]

	for i in range(26):
		char_key = ord('a') + i
		combined_word += chr(char_key) * min_word[i]

	return combined_word



if __name__ == "__main__":
	dictionary = readfile('dictionary_sample.txt')
	words = pickwords(dictionary, 15, 12, 13, 14)
	print(words)
	words = pickwords(dictionary, 19)
	print(words)
	score = maxscrabblescore(dictionary, 'rnpcemtreaserfsno')
	print(score)
	print(searchanagrams(dictionary, 'colonialists'))
	print(combinewords(['art', 'acts', 'refresh']))

