import csv
import re
import numpy as np
import random
import math

dictWords = {}
global numberOfReviews
global reviews
global sentiments
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



        for row in reader:
            numberOfReviews += 1
            row[2] = re.sub("[^a-zA-Z]", " ", row[2])
            train.append(row)
            reviews.append([row[1], row[2], row[3], row[4]])

        reviews.pop(0)

        dataSequence = range(0, numberOfReviews)
        random.shuffle(dataSequence)

        global testIndexes, trainningSentences, testSentences, trainningIndexes

        testIndexes = dataSequence[:int(math.floor(float(numberOfReviews) / 5))]
        trainningIndexes = list(set(dataSequence).difference(testIndexes))
        testSentences = np.array(reviews)[testIndexes][:,1]
        trainningSentences = np.array(reviews)[trainningIndexes]

        titles = train[0]
        train.remove(train[0])

        for evaluation in trainningSentences:
            countWords(evaluation[1], evaluation[2])

        corrects = 0.0
        for index,review in enumerate(testSentences):
            if classify(review) - int(sentiments[index]) == 0:
                corrects += 1

        print 'Vc atingiu ', (corrects / len(testSentences))

def classify(sentence):

    return np.argsort(probabilityOfSentenceBelongToSentiment(sentence))[2]

def probabilityOfWordBelongToSentiment(word):

    probabilities = [0,0,0]
    global numberOfReviews, testSentences

    if dictWords.keys().__contains__(word):
        for i in range(0,3):
            probabilities[i] = float(dictWords[word][i]) / len(testSentences)
    else:
        probabilities = [1, 1, 1]

    return probabilities


def probabilityOfSentenceBelongToSentiment(sentence):
    probabilities = [1, 1, 1]
    global numberOfReviews

    for word in sentence:
        wordprobabilities = probabilityOfWordBelongToSentiment(word)
        for index,probability in enumerate(wordprobabilities):
            probabilities[index] *= probability

    return probabilities



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