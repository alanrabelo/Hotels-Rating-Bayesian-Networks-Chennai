import csv
import re
import nltk
from nltk.corpus import stopwords


with open('chennai_reviews.csv', 'r') as file:
    reader = csv.reader(file)
    train = []
    for row in reader:
        row[2] = re.sub("[^a-zA-Z]",
                              " ",
                              row[2])
        train.append(row)
    titles = train[0]
    train.remove(train[0])
    print(titles)
    print(train[5])
    print stopwords.words("english")
