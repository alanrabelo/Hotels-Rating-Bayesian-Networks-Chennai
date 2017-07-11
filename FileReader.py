import csv

class FileReader(object):
    @staticmethod
    def readvalues():
        values = csv.reader('chennai_reviews.csv', delimiter=',,,,',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(values)

