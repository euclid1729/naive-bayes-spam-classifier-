import math,re

class bayesean:
 def __init__(self):
 #dictionary to hold count of a word in a category e.g. {'word1':{'category1':count1,'category2':count2}}}
  self.fcat_count={}
 #dictionary to hold count of number of documents in each category 
  self.category={} 
 
 def getwords(self,doc):
  split_logic=re.compile('\\W*')
  content=''
  for line in file(doc):
   content+=line
   content+=' '
  words=[s.lower() for s in split_logic.split(content)]
  return dict([(word,1) for word in words])
 
 def increase_feature_count(self,feature,cat):
  self.fcat_count.setdefault(feature,{})
  self.fcat_count[feature].setdefault(cat,0)
  self.fcat_count[feature][cat]+=1
 
 #increasing the count of category 
 def increaseCategoryCount(self,cat):
  self.category.setdefault(cat,0)
  self.category[cat]+=1
 
 #return number of times a feature has occurred in a particular category 
 def getFeatureCount(self,feature,cat):
  if feature in self.fcat_count and cat in self.fcat_count[feature]:
   return float(self.fcat_count[feature][cat])
 
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
   self.increase_feature_count(feature,cat)
  #increase the category count 
  self.increaseCategoryCount(cat)
 
 def getFeatureProb(self,f,cat):
  if self.getCategoryCount(cat) ==0: return 0
  if self.getFeatureCount(f,cat) == None: return 0
  else : return (self.getFeatureCount(f,cat)/self.getCategoryCount(cat))
 
 # "add one smoothing", for handling probabilites for categories or features that are seen first time in test data  
 
 def getWeightedProb(self,f,cat,weight=1.0,ap=0.5):
  org_prob=self.getFeatureProb(f,cat) 
  totals=sum([self.getFeatureCount(f,c) for c in self.getListCategories( ) if self.getFeatureCount(f,c) is not None])
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
  probDoc=self.getDocCategoryProbabilty(doc,cat)
  probCat=self.getCategoryCount(cat)/self.getCountTotalDocument()  
  return probDoc*probCat
 
 #for spam classifcation, we are putting a threshold on the difference between prob of spam and non spams since we dont want to categorize non spam as spam just because the probability(spam|doc) is just a little more than probability(non spam|doc)
 
 def NaiveBayesClassify(self,doc,default='non spam'):
  max_prob=0
  probs={} # this dictionary will keep values of probabilites associated with each spam 
  #we are taking threshold vale as 2
  threshold=2
  best=self.getListCategories()[0]
  for c in self.getListCategories():
   probs[c]=self.getCategoryDocProbability(doc,c)
   if probs[c] > max_prob:
    max_prob=probs[c]
    best=c
  for c in probs:
   if c == best: continue
   if probs[c] * 2 > max_prob: return default
  return best
  
 def trainAll(self,path,cat):
  import os
  listing = os.listdir(path)
  for infile in listing:
   self.parseDoc(path+'/'+infile,cat)  
