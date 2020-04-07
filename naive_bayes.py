from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import stopwords
import csv
from SVM import *

stopWordsList = stopwords.words('english')

def simplify_sentence(row, stopWordsList):
	tmp_row = TextBlob(row.decode('iso-8859-14')).correct()
	tmp_row = tmp_row.words
	filtered_sentence = list()
	for word in tmp_row:
		camelWordList = SplitCamelWordIntoList(word)
                for w in camelWordList:
                    w = RemoveHashTag(w)
                    if len(w) > 1 and not stopWordsList.__contains__(w.lower()) and not w.__contains__('@') and w.isalpha():
                        filtered_sentence.append(stemmer.stem(w).lower())
	return filtered_sentence

if __name__ == "__main__":
	print "creating data"
	Data = list()
	with open("svm_data.csv", "r") as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			row = line['post']
			tag = line['tag']
			Data.append((' '.join(simplify_sentence(row, stopWordsList)), tag))
	Data = np.array(Data)
	print "testing our model with Cross Validation"
	scores = list()
	kf = KFold(len(Data), n_folds=5)
	for train_index, test_index in kf:
		Data_train, Data_test = Data[train_index], Data[test_index]
		cl = NaiveBayesClassifier(Data_train)
		scores.append(cl.accuracy(Data_test))
	print(scores)
	print("Average success rate for 5 fold cross validation is", np.mean(scores))
	print '************Naive-Bayes   FINISH*****************'
