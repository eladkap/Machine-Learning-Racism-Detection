'''
    Document-Sentence model
    Authors: Elad Kapuza, Shir Shtinits, Hillel Merran
'''




'''
	Convert a sentence (string) to a list of stemmed words, without stopwords
	PARAMETERS:
		row - a sentence (string)
		stopWordsList - a list of stopwords
	RETURN:
		the list of the words of the simplified sentence
'''
def simplify_sentence(row, stopWordsList):


	
'''
	Calculate the score of a tag for a clique
	PARAMETERS:
		s1, s2 - sentences of the clique (string)
		post_tag - tag of the post {0: non-racist, 1: racist}
		tag1, tag2 - tags of s1, s2 {-1: anti-racist, 0:neutral, 1:racist}
		stopWordsList - a list of stopwords
	RETURN:
		the score of the clique
'''
def clique_score(weights, post_tag, tag1, tag2, s1, s2, stopWordsList):



'''
	Calculate the score of a tag for a post (and sentences)
	PARAMETERS:
		weights - vector of weights, one for each feature
		y = (post_tag, [sentence1_tag, ..., sentenceK_tag]) - tag of the post
		s = [sentence1, ..., sentenceK] - list of sentences (string) of the post
	RETURN:
		the score of the clique
'''
def score(weights, y, s):


	
'''
	Determine the tag of the first sentence in a clique which have the highest clique score
	PARAMETERS:
		weights - vector of weights, one for each feature
		clique_no - index of the clique
		current_2nd_sentence_tag - tag of the 2nd sentence of the clique
		sentence1 - first sentence of the clique (string)
		sentence2 - second sentence of the clique (string)
		stopWordsList - list of the stopwords
		viterbi - dictionary for Viterbi algorithm. {key=state: value=score}
	RETURN:
		backpointer - tag of the first sentence which maximize the score of the clique
		score - maximum score of the clique
'''
def max_clique_score(weights, clique_no, post_tag, current_2nd_sentence_tag, sentence1, sentence2, stopWordsList, viterbi):


	
'''
	Determine the tag of the sentences given the tag of the post using Viterbi algorithm
	PARAMETERS:
		weights - vector of weights, one for each feature
		d_tag - tag of the post {0: non racist, 1: racist}
		s - list of the sentences (string) of the post
	RETURN:
		list of tags. each tag is in {-1: anti-racist, 0: neutral, 1:racist} and correspond to a sentence
'''
def argmax(weights, d_tag, s):



'''
	Determine the tag of the post and sentences given the tag of the post using Viterbi algorithm
	PARAMETERS:
		weights - vector of weights, one for each feature
		s - list of the sentences (string) of the post
	RETURN:
		tag of the post and sentences - (post_tag, [s0_tag, ... , sM-1_tag])
'''
def classifier(weights, s):


# main
'''
	create a list of all posts and a list of their tag
	run the MIRA algorithm to learn the vector of weights
	test the model with Cross-Validation (5-folds)
'''
# END_main	
