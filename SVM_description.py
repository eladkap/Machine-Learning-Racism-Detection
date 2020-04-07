'''
	Remove '#' from an Hash tag. This function is used to decompose it
	PARAMATERS:
		word - a word (string)
	RETURN:
		the word without '#'
'''
def RemoveHashTag(word):



'''
	Split a camel case word into words list e.g HelloWorld into [Hello, World]
	PARAMETERS:
		camelWord - a camel case word (string)
	RETURN:
		List of words from the camel case word
'''
def SplitCamelWordIntoList(camelWord):



'''
	Create a corpus of termes, a list of posts, of tags, from the data posts
	PARAMETERS:
		corpus (return) - list of all the words in the data
		postsList (return) - list of posts, each post is a list of words
		tagList (return) - list of tags, each tag is in {0: non-racist, 1: racist}
		stopWordsList - a list of stopwords to remove from the posts
'''
def CreateCorpusAndPostListsAndTagList(corpus, postsList, tagList, stopWordsList):



'''
	Convert a post to a vector for the learning algorithm
	PARAMETERS:
		corpus - list of all words in the data
		post - the post to convert. the post is a list of words
	RETURN:
		the vector which represents the post
'''
def PostToVector(corpus, post):


'''
	Convert a post to a vector for the learning algorithm
	PARAMETERS:
		corpus - list of all words in the data
		stopWordsList - list of stopwords to remove from the post
		str - a post, as a string
	RETURN:
		the vector which represents the post
'''
def StringToVector(corpus, stopWordsList, str):



'''
	Convert a list of posts to a list of vectors
	PARAMETERS:
		corpus - list of all words in the data
		postsList - list of the posts to convert. each post is a list of words
		vectorsList (return) - list of vectors. each vector represents a post
'''
def CreateVectors(corpus, postsList, vectorsList):

	
# main
'''
	create a stemmed corpus with words from the data
	create a list of all posts and a list of all tags
	create the vectors from the posts
	run SVM with Cross-Validation (5-folds)
'''
# END_main
