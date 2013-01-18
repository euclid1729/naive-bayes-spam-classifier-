import math,re

class bayesean:
 def __init__(self):
 #dictionary to hold count of a word in a category e.g. {'word1':{'category1':count1,'category2':count2}}}
  fcat_count={}
 #dictionary to hold count of number of documents in each category 
  category={} 
 
 def getwords(doc):
  split_logic=re.compile('\\W*')
  words=[s.lower() for s in split_logic.split(doc)]
  return dict([(word,1) for word in words])
 
 def increase_feature_count(self,feature,cat):
  self.fcat_count.setdefault(feature,{})
  self.fcat_count[feature].setdefault(cat,0)
  self.fcat_count[feature][cat]+=1
 
 #increasing the count of category 
 def increaseCategoryCount(self,cat):
  self.cc.setdefault(cat,0)
  self.category[cat]+=1
 
 #return number of times a feature has occurred in a particular category 
 def getFeatureCount(self,feature,cat):
  if feature in self.fcat_count and cat in self.fcat_count[feature]:
   return self.fcat_count[feature][cat]
 
 #return number of documents in a category
 def getCategoryCount(self,cat):
  if cat in self.category:
   return float(self.category[cat])
 
 def getCountTotalDocument(self):
  return sum(self.category.values())
 
 def getListCategories(self):
  return self.category.keys()
 
 #parse the document and stores the different features and their count in respective categories 
 def parseDoc(self,doc,cat):
  words=self.getwords(doc)
  for feature in words:
   increase_feature_count(feature,cat)
  #increase the category count 
  increaseCategoryCount(cat)
 
 def getFeatureProb(self,f,cat):
  if self.getCategoryCount(cat)==0:
   return 0
  return self.getFeatureCount(f,cat)/self.getCategoryCount(cat)
 
 # "add one smoothing", for handling probabilites for categories or features that are seen first time in test data  
 
 def getWeightedProb(self,f,cat,weight=1.0,ap=0.5):
  org_prob=getFeatureProb(f,cat) 
  totals=sum([self.getFeatureCounts(f,c) for c in self.getListCategories( )])
  bp=((weight*ap)+(totals*org_prob))/(weight+totals)
  return bp
 
 #calculating probability(doc|category)
 def getDocCategoryProbabilty(self,doc,cat):
  #parse the doc 
  words=self.getwords(doc)
  prob=1
  for word in words:
   prob*=self.getWeightedProb(word,cat)
  return prob
 
 #calculating probability(category|doc)
 def getCategoryDocProbability(self,doc,cat):
  probDoc=self.getDoccategoryProbability(doc,cat)
  probCat=self.getCategoryCount(cat)/self.getCountTotalDocument()  
  return probDoc*probCat
 
 #for spam classifcation, we are putting a threshold on the difference between prob of spam and non spams since we dont want to categorize non spam as spam just because the probability(spam|doc) is just a little more than probability(non spam|doc)
 
 def NaiveBayesClassify(self,doc,default='non spam'):
  max_prob==o
  probs={} # this dictionary will keep values of probabilites associated with each spam 
  #we are taking threshold vale as 2
  threshold=2 
  for c in self.getListCategories():
   probs[c]=self.getCategoryDocProbabilty(doc,c)
   if probs[c] > max:
    max=probs[c]
    best=c 
  for c in probs:
   if c == best: continue
   if probs[c] * 2 > probs[best]: return default
  return best
 
 def trainAll(self,path,cat):
  import os
  listing = os.listdir(path)
  for infile in listing:
   parseDoc(infile,cat)  
