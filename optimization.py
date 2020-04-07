from cvxpy import *
import numpy as np
import itertools
from MEMM import *
import math
from features_lib import *
from nltk.corpus import stopwords

stopWordsList = stopwords.words('english')


def sum_of_features(y, s, n):
	sum_features = [0]*n
	if len(s) > 1:
		for i in range(0, len(s)-1):
			sum_features = np.add(sum_features, clique_to_features(y[0], y[1][i], y[1][i+1], s[i], s[i+1], stopWordsList))
	elif len(s) == 1:
		sum_features = np.add(sum_features, clique_to_features(y[0], y[1][0], y[1][0], s[0], s[0], stopWordsList))
	return sum_features

def Hamming_loss(w, z):
 	if not w[0].isdigit():
 		return 5
	loss = np.absolute(int(z[0])-int(w[0]))
	for i in range(0, len(w[1])):
		loss += np.absolute(z[1][i]-w[1][i])
	return loss

def argmin(w, y, s):
	m = len(s)
	n = len(w)
	w_star = Variable(n)
	
	iterables = list()
	for i in range(0, m):
		iterables.append([0,1])

	all_possible_tags = list()
	all_possible_scores = list()
	for y_d in range(0,2):
		for t in itertools.product(*iterables):
			tmp_tag = (y_d, list(t))
			all_possible_tags.append(tmp_tag)
			all_possible_scores.append(score(w, tmp_tag, s))
	# take only K=4 tags with the highest scores
	all_possible_scores = np.array(all_possible_scores)
	K_scores_ind = np.argpartition(all_possible_scores, -4)[-4:]
	K_tags = list()
	for k in K_scores_ind:
		K_tags.append(all_possible_tags[k])
	A=[]
	b=[]
	right_features = sum_of_features(y, s, n)
	for tag in K_tags:
		A.append(np.subtract(right_features, sum_of_features(tag, s, n)))
		b.append(Hamming_loss(y, tag))
	A = np.array(A)
	b = np.array(b)
	objective = Minimize(norm(w_star-w))
	constraints = [A*w_star >= b]
	prob = Problem(objective, constraints)
	result = prob.solve()
	vector = list()
	for val in np.array(w_star.value):
		vector.append(val[0])
	return np.array(vector)


