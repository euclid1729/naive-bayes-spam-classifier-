naive-bayes-spam-classifier-
============================

This program takes input a directory path of spam files and a directory path of non spam files to train the Naive Bayes Classifier. Once the training is done, the classifer is provided with a document that is to be classified as a spam or not.
Steps to follow to run the program

1. python 
2. >> import bayesnet 
3. >> classifier=bayesnet.bayesean()
4. >> classifier.trainAll('path_directory_contianing_spam_files','category_name_e.g._spam')
5. >> classifier.trainAll("path_directory_containing_other_category_e.g._not_spam','category_second_not_spam')
6. >>classifier.NaiveBayesClassify('document_name_to_be_classified')

Note: This Classifier can be used to calssify other categories also, e.g. you cann train it with blog feeds of particular type (news,sports etc as categories) and can then use it to categorize a new blog 
