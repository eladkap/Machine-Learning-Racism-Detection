
'''
	Calculate the sum of the different clique features vectors of a sentence
	PARAMETERS:
		y - tag of a post. y = (post_tag, [s1_tag, ..., sK_tag])
		s - a post (list of sentences). s = [s1_string, ..., sK_string]
		n - length of the features vectors
	RETURN:
		the sum of the vectors
'''
def sum_of_features(y, s, n):



'''
	Calculate the Hamming loss of a tag. Namely how many coordinates of 2 binary vectors are different
	PARAMETERS:
		w - a first tag. w = (post_tag, [sentence1_tag, ... , sentenceK_tag])
		z - a second tag. z = (post_tag, [sentence1_tag, ... , sentenceK_tag])
	RETURN:
		the Hamming loss
'''
def Hamming_loss(w, z):



'''
	Resolve the 4th step in MIRA algorithm. That is calculate the weight vector for iteration i+1
	PARAMETERS:
		w - original weights vector
		y - real tag of a post. y = (post_tag, [sentence1_tag, ..., sentenceK_tag])
		s - a post (list of sentences). s = [s1_string, ..., sK_string]
	RETURN:
		weight vector for next iteration
'''
def argmin(w, y, s):
