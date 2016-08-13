# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals
import math
import jieba
import jieba.posseg as pseg
import os
import sys
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.count(word) / len(blob)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
	if n_containing(word, bloblist)==len(bloblist):
		return 0
	else:
		return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def main():
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
				strRes = strRes + ' ' + str(key).decode('utf8','ignore').split('/')[0]
	bloblist = strRes.strip().split('\n ')
	#bloblist = strRes.decode('utf8','ignore').strip().split('\n ')

	'''bloblist = [u'極速 方案',
	u'極速 優惠 方案',
	u'學生 方案',
	u'學生 優惠 方案',
	u'學生 極速 優惠 方案',
	u'3G 攜碼 升級 方案']'''

	for i, blob in enumerate(bloblist):
		print 'Top words in document {}'.format(i + 1)
		for w in blob.split(' '):
			scores = {w: tfidf(w, blob, bloblist)}
			sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
			for word, score in sorted_words:
				print '\tWord: {}, TF-IDF: {}'.format(word.encode('utf8').decode('utf8','ignore'), round(score, 5))

if __name__ == '__main__':
  	main()