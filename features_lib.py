from nltk.corpus import stopwords
from nltk import LancasterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import re
import csv
from textblob import TextBlob
from nltk.corpus import stopwords

stopWordsList = stopwords.words('english')


def StemWord(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)

def CreateRacistStemmedCorpus():
    racistSet= set()
    with open("racist_words.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            word = TextBlob(line['racist'].decode('iso-8859-14')).words[0]
            racistSet.add(StemWord(word))
    return racistSet

def CreateAntiRacistStemmedCorpus():
    antiRacistSet= set()
    with open("anti_racist_words.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            word = TextBlob(line['anti_racist'].decode('iso-8859-14')).words[0]
            antiRacistSet.add(StemWord(word))
    return antiRacistSet



racistSet=CreateRacistStemmedCorpus()
antiRacistSet=CreateAntiRacistStemmedCorpus()

def RemoveHashTag(word):
    newWord = word.replace("#", "")
    return newWord

def SplitCamelWordIntoList(camelWord):
    newWord = re.sub("([a-z])([A-Z])","\g<1> \g<2>",camelWord)
    return newWord.split(' ')

def simplify_sentence(row,stopWordsList):
    tmp_row = TextBlob(row).correct()
    tmp_row = tmp_row.words
    filtered_sentence = list()
    for word in tmp_row:
        camelWordList = SplitCamelWordIntoList(word)
        for w in camelWordList:
            w = RemoveHashTag(w)
            if len(w) > 1 and not stopWordsList.__contains__(w.lower()) and not w.__contains__('@') and w.isalpha():
                filtered_sentence.append(StemWord(word).lower())
    return filtered_sentence



def CreateStemmer():
    global stemmer
    stemmer = SnowballStemmer("english")


def Similarity(sentence1, sentence2):
    commonWords = set(sentence1).intersection(set(sentence2))
    return len(commonWords) / float(len(set(sentence1))+len(set(sentence2)))

def IsSimilarityLow(sentence1, sentence2):
    sim=Similarity(sentence1,sentence2)
    return 0.4>sim>0.2


def IsSimilarityHigh(sentence1, sentence2):
    sim=Similarity(sentence1,sentence2)
    return sim>0.4


def ContainsExclamationMark(sentence):
    return sentence.__contains__('!')


def BothContainExclamationMark(sentence1,sentence2):
    return ContainsExclamationMark(sentence1) and ContainsExclamationMark(sentence2)


def ContainsRacistWord(sentence, racistWord):
    return sentence.__contains__(racistWord)


def ContainsAnyRacistWord(sentence):
    for racistWord in racistSet:
        if ContainsRacistWord(sentence,racistWord):
            return True
    return False



def ContainsAntiRacistWord(sentence, antiRacistWord):
    return sentence.__contains__(antiRacistWord)


def ContainsAnyAntiRacistWord(sentence):
    for antiRacistWord in antiRacistSet:
        if ContainsAntiRacistWord(sentence,antiRacistWord):
            return True
    return False


def Polarity(sentence):
    return TextBlob(sentence).polarity


def IsPositiveSentimental(sentence):
    polarity=Polarity(sentence)
    return polarity>=0.3

def IsNegativeSentimental(sentence):
    polarity=Polarity(sentence)
    return polarity<-0.3


def Subjectivity(sentence):
    return TextBlob(sentence).subjectivity

def IsSubjective(sentence):
    subjectivity=Subjectivity(sentence)
    return subjectivity>=0.4

def IsObjective(sentence):
    subjectivity=Subjectivity(sentence)
    return subjectivity<0.4

def HasAdjective(sentence):
    tags_dictionary=dict(TextBlob(sentence).tags)
    return list(tags_dictionary.values()).__contains__('JJ')


def clique_to_features(post_tag,s1_tag,s2_tag,s1,s2,stopWordsList):
    s1_simple=simplify_sentence(s1,stopWordsList)
    s2_simple=simplify_sentence(s2,stopWordsList)



    featuresVector = list()
    featuresVector.append(post_tag==1)
    featuresVector.append(post_tag==1)
    featuresVector.append(post_tag==0)
    featuresVector.append(s1_tag==1)
    featuresVector.append(s1_tag==0)
    featuresVector.append(s1_tag==-1)
    featuresVector.append(s2_tag==1)
    featuresVector.append(s2_tag==0)
    featuresVector.append(s2_tag==-1)

    featuresVector.append(IsSimilarityHigh(s1_simple,s2_simple))
    featuresVector.append(IsSimilarityLow(s1_simple,s2_simple))

    featuresVector.append(ContainsExclamationMark(s1))
    featuresVector.append(ContainsExclamationMark(s2))
    featuresVector.append(ContainsExclamationMark(s1) and ContainsExclamationMark(s2))

    # racist features
    featuresVector.append(ContainsAnyRacistWord(s1_simple))
    featuresVector.append(ContainsAnyRacistWord(s2_simple))
    featuresVector.append(ContainsAnyRacistWord(s1_simple) and ContainsAnyRacistWord(s2_simple))

    for racistWord in racistSet:
        featuresVector.append(ContainsRacistWord(s1_simple,racistWord))
        featuresVector.append(ContainsRacistWord(s2_simple,racistWord))
        featuresVector.append(ContainsRacistWord(s1_simple,racistWord) and ContainsRacistWord(s2_simple,racistWord))

    # anti racist features
    featuresVector.append(ContainsAnyAntiRacistWord(s1_simple))
    featuresVector.append(ContainsAnyAntiRacistWord(s2_simple))
    featuresVector.append(ContainsAnyAntiRacistWord(s1_simple) and ContainsAnyAntiRacistWord(s2_simple))

    for antiRacistWord in antiRacistSet:
        featuresVector.append(ContainsAntiRacistWord(s1_simple,antiRacistWord))
        featuresVector.append(ContainsAntiRacistWord(s2_simple,antiRacistWord))
        featuresVector.append(ContainsAntiRacistWord(s1_simple,antiRacistWord) and ContainsAntiRacistWord(s2_simple,antiRacistWord))

    # positive sentimental
    featuresVector.append(IsPositiveSentimental(s1))
    featuresVector.append(IsPositiveSentimental(s2))
    featuresVector.append(IsPositiveSentimental(s1) and IsPositiveSentimental(s2))

    # negative sentimental
    featuresVector.append(IsNegativeSentimental(s1))
    featuresVector.append(IsNegativeSentimental(s2))
    featuresVector.append(IsNegativeSentimental(s1) and IsNegativeSentimental(s2))

    # objective
    featuresVector.append(IsObjective(s1))
    featuresVector.append(IsObjective(s2))
    featuresVector.append(IsObjective(s1) and IsObjective(s2))

    # subjective
    featuresVector.append(IsSubjective(s1))
    featuresVector.append(IsSubjective(s2))
    featuresVector.append(IsSubjective(s1) and IsSubjective(s2))

    # contains adjective
    featuresVector.append(HasAdjective(s1))
    featuresVector.append(HasAdjective(s2))
    featuresVector.append(HasAdjective(s1) and HasAdjective(s2))

    return featuresVector


'''
if __name__ == '__main__':
    clique_to_features(1,1,1,'hello world','goodbye world',stopWordsList)
'''