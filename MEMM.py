'''
    Maximum Entropy Markov Model
    Authors: Herat Gandhi, Prashant Makwana, Mohnish Gorasia, Rushabh Mehta, Prashama Patil, Radhika Kulkarni
'''
import fileinput
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from SVM import *
from features_lib import *
from optimization import *

stopWordsList = stopwords.words('english')


def simplify_sentence(row, stopWordsList):
	tmp_row = TextBlob(row).correct()
	tmp_row = tmp_row.words
	filtered_sentence = list()
	for word in tmp_row:
		camelWordList = SplitCamelWordIntoList(word)
                for w in camelWordList:
                    w = RemoveHashTag(w)
                    if len(w) > 1 and not stopWordsList.__contains__(w.lower()) and not w.__contains__('@') and w.isalpha():
                        filtered_sentence.append(stemmer.stem(w).lower())
	return filtered_sentence

	
def clique_score(weights, post_tag, tag1, tag2, s1, s2, stopWordsList):
	score = 0.0
	index = 0
	weights = np.array(weights)
	for feature in clique_to_features(post_tag, tag1, tag2, s1, s2, stopWordsList):
		if feature == 1:
			score += weights[index]
		index += 1
	return score


def score(weights, y, s):
	if len(s) == 0:
		return 0
	score = 0
	post_tag = y[0]
	tags = y[1]
	if len(s) > 1:
	# if there is at least 2 sentences
		for i in range(0,len(s)-1):
			score += clique_score(weights, post_tag, tags[i], tags[i+1], s[i], s[i+1], stopWordsList)
	else:
		score = clique_score(weights, post_tag, tags[0], tags[0], s[0], s[0], stopWordsList)
	return score

	

def max_clique_score(weights, clique_no, post_tag, current_2nd_sentence_tag, sentence1, sentence2, stopWordsList, viterbi):
	score = viterbi[(clique_no-1,-1)] + clique_score(weights, post_tag, -1, current_2nd_sentence_tag, sentence1, sentence2, stopWordsList)
	backpointer = -1
	for tag in range(0,2):
		tmp_score = viterbi[(clique_no-1, tag)] + clique_score(weights, post_tag, tag, current_2nd_sentence_tag, sentence1, sentence2, stopWordsList)
		if score < tmp_score:
			score = tmp_score
			backpointer = tag
	return backpointer, score


def argmax(weights, d_tag, s):
	M = len(s)
	s_tags = []			# [s0_tag, ... , sM-1_tag]
	viterbi = dict()	# viterbi[(current_clique, current_2nd_sentence_tag)] = score until current 2nd sentence
	backpointer = dict()	# backpointer[(sentence_no, sentence_tag)] = tag of the previous sentence
	if M == 0:
		return None
	elif M == 1:
		score = clique_score(weights, d_tag, -1, -1, s[0], s[0], stopWordsList)
		s_tags = [-1]
		for tag in range(0,2):
			tmp_score = clique_score(weights, d_tag, tag, tag, s[0], s[0], stopWordsList)
			if tmp_score > score:
				score = tmp_score
				s_tags = [tag]
		return s_tags
	else:
		# creating M-1 cliques
		cliques = []		# [... , [s[i],s[i+1]] , ...]
		for i in range(0, M-1):
			cliques.append([s[i], s[i+1]])
	
	# initialization of viterbi algorithm
	viterbi[(-1,-1)] = 0
	viterbi[(-1,0)] = 0
	viterbi[(-1,1)] = 0
	
	# viterbi algorithm
	clique_no = 0
	sentence_no = 1
	for clique in cliques:
		backpointer[(sentence_no, -1)], viterbi[(clique_no, -1)] = max_clique_score(weights, clique_no, d_tag, -1, cliques[clique_no][0], cliques[clique_no][1], stopWordsList, viterbi)
		backpointer[(sentence_no, 0)], viterbi[(clique_no, 0)] =  max_clique_score(weights, clique_no, d_tag, 0, cliques[clique_no][0], cliques[clique_no][1], stopWordsList, viterbi)
		backpointer[(sentence_no, 1)], viterbi[(clique_no, 1)] =  max_clique_score(weights, clique_no, d_tag, 1, cliques[clique_no][0], cliques[clique_no][1], stopWordsList, viterbi)
		clique_no += 1
		sentence_no += 1

	# return value
	max = viterbi[(M-2, -1)]
	tag = -1
	for t in range(0,2):
		temp_max = viterbi[(M-2, t)]
		if  max < temp_max:
			max = temp_max
			tag = t

	s_tags.append(tag)
	for sentence_index in range(M-1, 0, -1):
		previous_tag = backpointer[(sentence_index, tag)]
		s_tags.insert(0, previous_tag)
		tag = previous_tag

	return s_tags


def classifier(weights, s):
	y = []		# [d_tag, [s0_tag, ... sM-1_tag]]
	for d_tag in range(0,2):
		s_tag = argmax(weights, d_tag, s)
		tmp_y = [d_tag, s_tag]
		if len(y) == 0 or score(weights, tmp_y, s) > score(weights, y, s):
			y = tmp_y
	return tuple(y)
	

	
if __name__ == "__main__":
    #Training portion
	post_index = -1
	posts = list()     # list of posts. each post is a list of filtered sentences : [str_sentence1, ..., str_sentenceK]
	tags = list()     # list of tags. each tag is a tuple: (post_tag, [sentence1_tag, ..., sentenceK_tag])
	train_file = "MEMM_test_700.csv"

	with open(train_file, "r") as csvfile:
	        reader = csv.DictReader(csvfile)

	        for line in reader:
		        row = line['post'].decode('iso-8859-14')
			sentiment_val = int(line['tag'])   # tag of the current sentence {-1: anti-racist, 0: neutral, 1: racist}
			if row.find('{') != -1:
			# if it's a new post
				post_index += 1
				row = row.replace('{','')
				row = row.replace('}','')
				post_tag = row[0]     # tag of the whole post {0: non racist, 1: racist}
				row = re.sub(r'-*\d+', '', row)  # remove numbers (the tag)
				posts.append([])
				tags.append((post_tag, []))

			posts[post_index].append(row)
			tags[post_index][1].append(sentiment_val)


	'''
		Classification
	'''
	#Testing our model with Cross Validation
	posts = np.array(posts)

	hits = list()
	kf = KFold(len(posts), n_folds=5)
	features_num = len(clique_to_features(1, 1, 1, "I love ping-pong", "You're so stupid!", stopWordsList))
	CV_index = -1
	for train_index, test_index in kf:
		CV_index += 1
		print "\n","TRAIN:", train_index, "TEST:", test_index, "\n"
		posts_train, posts_test = posts[train_index], posts[test_index]
		tags_train = list()
		tags_test = list()
		for index in range(0, len(tags)):
			if index in test_index:
				tags_test.append(tags[index])
			else:
				tags_train.append(tags[index])
		'''
		MIRA algorithm for learning weights vector
		'''
		w=[0]*features_num
		N=3
		T=len(posts_train)
		for i in range(0,N):
			for t in range(0,T):
				print "CV, N , T = ", CV_index,",", i, ",", t
				w=argmin(w, tags_train[t], posts_train[t])
		hit = 0
		for i in range(0, len(posts_test)):
			hit += tags_test[i] == classifier(w, posts_test[i])
		print "hit for CV =", CV_index, " is ", hit
		hits.append(hit)
	print(hits)
	print("Average success rate for 10 fold cross validation is", np.mean(hits))
	print '************SVM  FINISH*****************'

	
