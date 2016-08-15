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
				strRes = str(key).decode('cp950','ignore').split('/')[0]
				first  = False
			else:
				strRes = strRes + ' ' + str(key).decode('cp950','ignore').split('/')[0]
	bloblist = strRes.strip().split('\n ')

	for i, blob in enumerate(bloblist):
		print 'Top words in document {}'.format(i + 1)
		for w in blob.split(' '):
			scores = {w: tfidf(w, blob, bloblist)}
			sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
			for word, score in sorted_words:
				if score != 0.0:
					print '\tWord: {}, TF-IDF: {}'.format(word, round(score, 5))

if __name__ == '__main__':
  	main()