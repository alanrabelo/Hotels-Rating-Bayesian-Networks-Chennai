class Word(object):

   def __init__(self,name):
      self.name = name
      self.qtGoodReviews = 0
      self.qtBadReviews = 0
      self.qtNeutralReviews = 0


   def increaseQtReviews(self, index):
       if index == 0:
           self.qtGoodReviews = self.qtGoodReviews + 1
       elif index == 1:
           self.qtNeutralReviews = self.qtNeutralReviews + 1
       else:
           self.qtBadReviews = self.qtBadReviews + 1

    