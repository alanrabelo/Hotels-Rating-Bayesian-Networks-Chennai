import csv

with open('chennai_reviews.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

