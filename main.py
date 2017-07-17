import csv
import re
import numpy as np
import random
import math
import nltk
from nltk.corpus import stopwords

dictWords = {}
global numberOfReviews
global reviews
global sentiments, sentimentsTrainning, sentimentsTesting
global trainningSentences, testSentences, trainningIndexes, testIndexes

def main():


    with open('chennai_reviews.csv', 'r') as file:
        reader = csv.reader(file)
        train = []


        global numberOfReviews
        numberOfReviews = -1

        global reviews
        reviews = []

        global sentiments
        sentiments = []

        for index,row in enumerate(reader):

            if index != 0 and row[3] != '':
                numberOfReviews += 1
                row[2] = re.sub("[^a-zA-Z]", " ", row[2])
                sentiments.append(int(row[3])-1)
                train.append(row)
                reviews.append([row[1], row[2], row[3], row[4]])



        dataSequence = range(0, numberOfReviews)
        random.shuffle(dataSequence)

        global testIndexes, trainningSentences, testSentences, trainningIndexes


        testIndexes = dataSequence[:int(math.floor(float(numberOfReviews) / 5))]
        trainningIndexes = list(set(dataSequence).difference(testIndexes))
        testSentences = np.array(reviews)[testIndexes][:,1]
        trainningSentences = np.array(reviews)[trainningIndexes]
        sentimentsTrainning = np.array(sentiments)[trainningIndexes]
        sentimentsTesting = np.array(sentiments)[testIndexes]


        titles = train[0]
        train.remove(train[0])

        for evaluation in trainningSentences:
            countWords(evaluation[1], evaluation[2])

        removeStopWords()


        correctsTrainning = 0.0

        for index, review in enumerate(trainningSentences[:,1]):
            c = classify(review)
            if c - int(sentimentsTrainning[index]) == 0:
                correctsTrainning += 1

        print 'No treino voce atingiu ', (correctsTrainning / len(trainningSentences))

        corrects = 0.0
        for index,review in enumerate(testSentences):
            c = classify(review)
            if c - int(sentimentsTesting[index]) == 0:
                corrects += 1
        print 'No teste voce atingiu ', (corrects / len(testSentences))



def classify(sentence):

    return np.argsort(probabilityOfSentenceBelongToSentiment(sentence))[2]

def probabilityOfWordBelongToSentiment(word):

    probabilities = [0,0,0]
    global numberOfReviews, testSentences

    if dictWords.keys().__contains__(word):
        for i in range(0,3):
            probabilities[i] = float(dictWords[word][i]) / (dictWords[word][0]+ dictWords[word][1] + dictWords[word][2])
    else:
        probabilities = [1, 1, 1]
    return probabilities

def probabilityOfSentenceBelongToSentiment(sentence):
    probabilities = [1, 1, 1]
    global numberOfReviews

    sentence = sentence.lower()
    words = sentence.split()


    for word in words:
        wordprobabilities = probabilityOfWordBelongToSentiment(word)
        for index,probability in enumerate(wordprobabilities):
            probabilities[index] *= probability

    return probabilities


def removeStopWords():
    #print stopwords.words("english")
    #print(dictWords.keys())
    for w in dictWords.keys():
        if w in stopwords.words("english"):
            #print(w)
            dictWords.pop(w, None)

def countWords(words, sentiment):

    if sentiment == "":
        return

    array = list(set(words.lower().split()))
    global reviews
    # reviews.append(array)

    global sentiments
    sentimentindex = int(sentiment) - 1
    sentiments.append(sentimentindex)

    for word in array:
        word.replace(" ", "")
        if not dictWords.has_key(word):
            dictWords[word] = [0, 0, 0]
            dictWords[word][sentimentindex] = 1
        else:
            dictWords[word][sentimentindex] += 1


if __name__ == '__main__':
    main()