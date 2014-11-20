#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Unigram feature from Wang's featureList
"""

import re
import json
import os
import codecs
import dealTweets as dts
from collections import deque
import utilities
import HTMLParser
import getUnigramWords

tokenizer = utilities.Tokenizer()

def preprocess(text):
        text = re.sub(u'\\\'', '\'', text)
        text = re.sub(u'\\\w', '', text)
	text = re.sub(u'\u2026', ' ', text)                             #deal with horizontal ellipsis
	text = re.sub(u'[\u201c\u201d]', '"', text)                     #deal with double quotation lmark
	text = re.sub(u'[\u2018\u2019]', '\'', text)                    #deal with single quotation mark
	text = re.sub('h…', 'URL', text)                                #deal with truncated url
	text = re.sub('ht?….*$', 'URL', text)                           #deal with truncated url 
	text = re.sub('(^|)?http?s?:?/?/?.*?( |$)', 'URL', text)        #deal with compelted url
	text = re.sub(u'(RT |\\\\|\u201c)"?@.*?[: ]', ' ', text)        #deal with retweet
        text = re.sub(u'#[\w\d]+', ' ', text)
	text = re.sub('\.?@.*?( |:|$)', 'USERNAME ', text)              #deal with username
	text = HTMLParser.HTMLParser().unescape(text)                   #deal with character entity
#	text = re.sub('[][!"#$*,/;<=>?@\\\\^_`{|}~]', ' ', text)        #deal with punctuation
        text = re.sub('[][:\(\)"#$*,/;<=>@\\\\^_`{|}~]', ' ', text)          #deal with punctuation, without '!?', for features
	text = re.sub('( - )', ' ', text)
	text = re.sub('---', ' ', text)
	text = re.sub('\.\.\.', ' ', text)
	text = re.sub('(, |\.( |$))', ' ', text)

	return text

def getUnigramVector(text):
    pass

def __dealLine(param):
    line = dts.readlineI()
    if not line:
        return
    obj = json.loads( line )
    text = obj['text']
    hashtag = obj['hashtag']
    if hashtag != param[0]:
        return
    
    wordList = tokenizer.tokenize(preprocess(text))
    dict = {}
    for uni in getUnigramWords.getUnigramWords():
        dict.update( { uni: 0 } )
        for word in wordList:
            if word == uni:
                dict.update( { word: 1 } )
    
    nobj = ( dict, 0 )
    #print nobj
    dts.writeO( str(nobj)+'\n' )


def featureUnigram():
    topicList = [ur"#emabiggestfans1d", ur"#emabiggestfansjustinbieber", ur"#porn", ur"#ipad", ur"#halloween", ur"#emabiggestfans5sos", ur"#stealmygirl", ur"#thewalkingdead", ur"#ebola", ur"#emabiggestfansarianagrande", ur"#lol"]
    
    for hashtag in topicList:
        topic = hashtag[1:]
        dts.setSize( 50000 )
        dts.setFile( '../entityOutput/topictwitter', '../entityOutput/topicTwitter_'+topic, '../log/topicTwitterFeatvect')
        dts.openFiles()
        dts.loop_with_param( __dealLine, [ hashtag, ],'Generating Unigram With Tag:'+topic )
        dts.closeFiles()

if __name__ == "__main__":
    featureUnigram()
    pass

