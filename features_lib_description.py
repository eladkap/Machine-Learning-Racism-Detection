'''
    Features for Document-Sentence model
    Authors: Elad Kapuza, Shir Shtinits, Hillel Merran
'''


'''
	Convert a word to its stemmed form
	PARAMETERS:
		word - a word (string)
	RETURN:
		The stemmed form of the word
'''
def StemWord(word):


'''
	Create a corpus of racist stemmed word from csv file
	PARAMETERS:
		None
	RETURN:
		Set of racist words
'''
def CreateRacistStemmedCorpus():


'''
	Create a corpus of anti-racist stemmed word from csv file
	PARAMETERS:
		None
	RETURN:
		Set of anti-racist words
'''
def CreateAntiRacistStemmedCorpus():


'''
	Remove '#' from an Hash tag. This function is used to decompose it
	PARAMATERS:
		word - a word (string)
	RETURN:
		the word without '#'
'''
def RemoveHashTag(word):



'''
	Split a camel case word into words list
	e.g HelloWorld into [Hello, World]
	PARAMETERS:
		camelWord - a camel case word (string)
	RETURN:
		List of words from the camel case word
'''
def SplitCamelWordIntoList(camelWord):


'''
	Convert a sentence (string) to a list of stemmed words, without stopwords
	PARAMETERS:
		row - a sentence (string)
		stopWordsList - a list of stopwords
	RETURN:
		the list of the words of the simplified sentence
'''
def simplify_sentence(row,stopWordsList):


'''
	Create stemmer object
	PARAMETERS:
		None
	RETURN:
		Stemmer object
'''
def CreateStemmer():



'''
	Calculate sumilarity value between two sentences by counting common words
	PARAMETERS:
		sentence1 - first sentence (list of words)
		sentence2 - second sentence (list of words)
	RETURN:
		Similarity value
'''
def Similarity(sentence1, sentence2):
    
	
	

'''
	Check if the similarity level between two sentences is low
	PARAMETERS:
		sentence1 - first sentence (list of words)
		sentence2 - second sentence (list of words)
	RETURN:
		True if the similarity level is low and false otherwise
'''	
def IsSimilarityLow(sentence1, sentence2):



'''
	Check if the similarity level between two sentences is high
	PARAMETERS:
		sentence1 - first sentence (list of words)
		sentence2 - second sentence (list of words)
	RETURN:
		True if the similarity level is high and false otherwise
'''	
def IsSimilarityHigh(sentence1, sentence2):



'''
	Check if the sentence contains exclamation mark
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence contains exclamation mark and false othrewise
'''
def ContainsExclamationMark(sentence):



'''
	Check if the both two sentences contain exclamation mark
	PARAMETERS:
		sentence1 - first sentence (string)
		sentence2 - second sentence (string)
	RETURN:
		True if the both two sentences contain exclamation mark and false othrewise
'''
def BothContainExclamationMark(sentence1,sentence2):



'''
	Check if the sentence contains a racist word
	PARAMETERS:
		sentence - sentence (list of words)
		racistWord - racist word (string)
	RETURN:
		True if the sentence contains the racist word
'''
def ContainsRacistWord(sentence, racistWord):




'''
	Check if the sentence contains any racist word from the racist words corpus
	PARAMETERS:
		sentence - sentence (list of words)
	RETURN:
		True if the sentence contains any racist word
'''
def ContainsAnyRacistWord(sentence):


'''
	Check if the sentence contains an anti-racist word
	PARAMETERS:
		sentence - sentence (list of words)
		antiRacistWord - anti-racist word (string)
	RETURN:
		True if the sentence contains the anti-racist word
'''
def ContainsAntiRacistWord(sentence, antiRacistWord):


'''
	Check if the sentence contains any anti-racist word from the anti-racist words corpus
	PARAMETERS:
		sentence - sentence (list of words)
	RETURN:
		True if the sentence contains any anti-racist word
'''
def ContainsAnyAntiRacistWord(sentence):



'''
	Calculates the polarity of the sentence (sentiment level between -1 to 1)
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		Polarity value
'''
def Polarity(sentence):



'''
	Check if the sentence has a positive sentiment
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence has a positive sentiment and false otherwise
'''
def IsPositiveSentimental(sentence):


	
'''
	Check if the sentence has a negative sentiment
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence has a negative sentiment and false otherwise
'''
def IsNegativeSentimental(sentence):



'''
	Calculates the subjectivity level of the sentence (between 0 to 1)
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		Polarity value
'''
def Subjectivity(sentence):

	
	
'''
	Check if the sentence is subjective
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence is subjective and false otherwise
'''
def IsSubjective(sentence):



'''
	Check if the sentence is objective
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence is objective and false otherwise
'''
def IsObjective(sentence):


'''
	Check if the sentence contains adjectives
	PARAMETERS:
		sentence - sentence (string)
	RETURN:
		True if the sentence contains adjectives and false otherwise
'''
def HasAdjective(sentence):


'''
	Creates list of features with values of 0 or 1
	PARAMETERS:
		post_tag - The true tag value of the post (int)
		s1_tag - The true tag value of a sentence in the post (int)
		s2_tag - The true tag value of the following sentence in the post (int)
		s1 - A sentence in the post
		s2 - The following sentence in the post
		stopWordsList - Corpus of stop words
	RETURN:
		List of features with values of 0 or 1
'''
def clique_to_features(post_tag,s1_tag,s2_tag,s1,s2,stopWordsList):
   
   