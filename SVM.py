from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import re
import csv
import numpy as np
from sklearn import svm
from sklearn.cross_validation import KFold
from textblob import TextBlob

stemmer = SnowballStemmer("english")
stopWordsList = stopwords.words('english')


def RemoveHashTag(word):
	newWord = word.replace("#", "")
	return newWord

def SplitCamelWordIntoList(camelWord):
	newWord = re.sub("([a-z])([A-Z])","\g<1> \g<2>",camelWord)
	return newWord.split(' ')

def CreateCorpusAndPostListsAndTagList(corpus, postsList, tagList, stopWordsList):
	with open("svm_data.csv", "r") as csvfile:
		reader = csv.DictReader(csvfile)

		for line in reader:
			row = TextBlob(line['post'].decode('iso-8859-14')).correct()
			tag = int(line['tag'])
			words = row.words
			postWords = list()   # filtered list of the post's words
			for word in words:
				camelWordList = SplitCamelWordIntoList(word)
				for w in camelWordList:
					w = RemoveHashTag(w)
					if len(w) > 1 and not w.lower() in stopWordsList and not w.__contains__('@') and w.isalpha():
						postWords.append(stemmer.stem(w).lower())
						corpus.add(stemmer.stem(w).lower())

			postsList.append(postWords)
			tagList.append(tag)

def PostToVector(corpus, post):
	vector = [0] * len(corpus)
	for word in post:
		vector[wordToIndex[word]] += 1
	return vector

def StringToVector(corpus, stopWordsList, str):
	wordsList = list()
	str = TextBlob(str.decode('iso-8859-14')).correct()
	postWords = str.words
	for word in postWords:
		camelWordList = SplitCamelWordIntoList(word)
		for w in camelWordList:
			w = RemoveHashTag(w)
			if len(w) > 1 and not stopWordsList.__contains__(w.lower()) and not w.__contains__('@') and w.isalpha():
				wordsList.append(stemmer.stem(w).lower())
	return PostToVector(corpus, wordsList)

def CreateVectors(corpus, postsList, vectorsList):
	for post in postsList:
		vector = PostToVector(corpus, post)
		vectorsList.append(vector)



if __name__ == "__main__":
	# declaration of variables
	postsList = list()    # list of the posts
	tagList = list()      # list of the posts' tags
	vectorsList = list()  # list of vectors. each vector is a post


	# create a stemmed corpus with words from the data
	corpus = set()

	print "\n\n" + '--------------creating corpus and list of posts-----------------'
	CreateCorpusAndPostListsAndTagList(corpus, postsList, tagList, stopWordsList)
	print '------------------success-----------------'

	# two dictionaries for the creation of the vectors
	wordToIndex = dict()
	indexToWord = dict()
	i = 0
	for word in corpus:
		wordToIndex[word] = i
		indexToWord[i] = word
		i += 1

	# convert posts to vectors (Bag Of Words)
	print "\n\n" + '--------------creating vectors from posts-----------------'
	CreateVectors(corpus, postsList, vectorsList)
	print '------------------success-----------------'



	print "\n\n" + '------------------SVM-----------------------'

	X = np.array(vectorsList)
	print 'X', len(X)
	X.reshape(-1, 1)
	Y = np.array(tagList)

	clf = svm.SVC()
	#Testing our model with Cross Validation
	scores = list()
	kf = KFold(len(X), n_folds=5)
	for train_index, test_index in kf:
		#print("TRAIN:", train_index, "TEST:", test_index)
		X_train, X_test = X[train_index], X[test_index]
		Y_train, Y_test = Y[train_index], Y[test_index]
		clf.fit(X_train, Y_train)
		scores.append(clf.score(X_test, Y_test))
	print scores
	print "Average success rate for 5 fold cross validation is ", np.mean(scores)
	print '************SVM  FINISH*****************'

