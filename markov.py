import random, string


# EDIT README TO REFLECT CHANGES

def process_file(filename):
	dictionary = {}

	newfile = open(filename)
	line = newfile.read()
	newfile.close()
	
	wordlist = line.split()
	if len(wordlist) > 0:
		n = 0
		#this is our loop to create a markov dictionary.
		for n in range(len(wordlist)-2):
			prefix =  (wordlist[n], wordlist[n+1])
			suffix = wordlist[n+2]
			if dictionary.get(prefix) is not None:
				# if current prefix is a key, add current suffix to list of values.
				dictionary[prefix].append(suffix)
			else:
				# adds a new key (current prefix) and begins a list of values with our current suffix.
				dictionary[prefix] = [suffix]

	else:
		pass
	return dictionary

 
def shift(muple, anything):
	#The function shift take a tuple and a string and return a new reversed tuple. (1,2) + 3 return (2,3)
	new_tuple = (muple[1],anything)
	return new_tuple

def build_sentence(mapping):
	# take random key from dictionary, create a string with key and one value.
	terminators = ['!', '?', '.']
	prefix = random.choice(mapping.keys())
	suffix = random.choice(mapping[prefix])
	sentence = string.capitalize(prefix[0]) + " " + prefix[1] + " " + suffix
	# this loop adds words.
	while suffix[-1] not in terminators:
		prefix = shift(prefix, suffix)
		suffix = random.choice(mapping[prefix])
		sentence += " " + suffix
	return sentence

def build_paragraph(dictionary, number):
	sentences = []
	for n in range(number):
		sentences.append(build_sentence(dictionary))
	paragraph = string.join(sentences)
	return paragraph


def build_tweet(dictionary):
	#use build_sentence() to add sentences as long as whole text is less than 140 characters.
	tweet = ""
	while len(tweet) <= 140:
		new_tweet = build_sentence(dictionary)
		if len(new_tweet) >140:
			continue
		elif len(tweet+new_tweet) > 140:
			return tweet
		else:
			if tweet == "":
				tweet += new_tweet
			else: 
				tweet += " " + new_tweet


def main():
	d = process_file("grimmsfairytales.txt")
	paragraph = build_paragraph(d, 10)
	#tweet = build_tweet(d)
	print paragraph

if __name__ == "__main__":
	main()