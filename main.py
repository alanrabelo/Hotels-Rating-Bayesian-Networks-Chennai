import csv
import re
import numpy as np

dictWords = {}
global numberOfReviews
global reviews
global sentiments

def main():


    with open('chennai_reviews.csv', 'r') as file:
        reader = csv.reader(file)
        train = []

        global numberOfReviews
        numberOfReviews = 0

        global reviews
        reviews = []

        global sentiments
        sentiments = []

        for row in reader:
            numberOfReviews += 1
            row[2] = re.sub("[^a-zA-Z]", " ", row[2])
            train.append(row)

        titles = train[0]
        train.remove(train[0])

        for evaluation in train:
            countWords(evaluation[2], evaluation[3])


        corrects = 0.0

        for index,review in enumerate(reviews):
            if classify(review) - int(sentiments[index]) == 0:
                corrects += 1

        print corrects / numberOfReviews

def classify(sentence):
    return np.argsort(probabilityOfSentenceBelongToSentiment(sentence))[2]

def probabilityOfWordBelongToSentiment(word):

    probabilities = [0,0,0]
    global numberOfReviews

    for i in range(0,3):
        probabilities[i] = float(dictWords[word][i]) / numberOfReviews

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
    reviews.append(array)

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