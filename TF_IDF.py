# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__=='__main__':
	with open('tf_test.txt') as f:
		cor = f.readlines()
	strRes = ''
	first = True
	for c in cor:
		words = pseg.cut(c)
		for key in words:
			if first:
				strRes = str(key).split('/')[0]
				first  = False
			else:
				strRes = strRes+ ' ' + str(key).split('/')[0]
		break
	'''corpus = strRes.decode("cp950", "ignore").strip().split('\n ')

	vectorizer=CountVectorizer()
	transformer=TfidfTransformer()
	tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
	word=vectorizer.get_feature_names()
	weight=tfidf.toarray()

	#file = open('tfidf.txt', 'w')
	for i in range(len(weight)): 
	    #print 'Line No.', i
	    print corpus[i]
	    for j in range(len(word)):
	    	#if weight[i][j] != 0.0:
	    	print word[j],weight[i][j]
	    		#print type(weight[i][j])
	    		#file.write(word[j]+','+str(weight[i][j]))
	#file.close()
'''