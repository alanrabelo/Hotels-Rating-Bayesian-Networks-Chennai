import csv
import re
import nltk
from nltk.corpus import stopwords

dictWords = {}
def main():
    with open('chennai_reviews.csv', 'r') as file:
        reader = csv.reader(file)
        train = []
        for row in reader:
            row[2] = re.sub("[^a-zA-Z]",
                              " ",
                              row[2])
            print(row[3])
            train.append(row)
        titles = train[0]
        train.remove(train[0])
        print(titles)
        print(train[1])
        for evaluation in train:
            countWords(evaluation[2], evaluation[3])

        print(dictWords)
        #print stopwords.words("english")

def countWords(words, sentiment):
    array = words.split()
    array = list(set(array))
    #print(words)
    for word in array:
        word.replace(" ", "")
        if not dictWords.has_key(word):
            dictWords[word] = {"1":0, "2":0, "3":0}
            dictWords[word][sentiment] = 1
        else:
            #print(word)
            #print(sentiment)
            dictWords[word][sentiment] = dictWords[word][sentiment] + 1

if __name__ == '__main__':
    main()