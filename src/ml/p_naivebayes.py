from statistics import mode
import pickle
from nltk.classify import ClassifierI

classifier_f = open('NuSV_classifier.pickle', 'rb')
NuSV_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('Bernoulli.pickle', 'rb')
Bernoulli = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('LinearSVC_classifier.pickle', 'rb')
LinearSVC_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('Log_classifier.pickle', 'rb')
Log_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('MNB_classifier.pickle', 'rb')
MNB_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('SGD_classifier.pickle', 'rb')
SGD_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open('naivebayes.pickle', 'rb')
naivebayes = pickle.load(classifier_f)
classifier_f.close()


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf


voted_classifier = VoteClassifier(NuSV_classifier, Bernoulli, LinearSVC_classifier, Log_classifier,
                                  MNB_classifier, SGD_classifier, naivebayes)

word_features_f = open('word_feature.pickle', 'rb')
word_features = pickle.load(word_features_f)
word_features_f.close()


def take_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features


def analyze(tweet):
    result = voted_classifier.classify(take_features(tweet.split()))
    return result


def confidence(tweet):
    result = voted_classifier.confidence(take_features(tweet.split()))
    return result

