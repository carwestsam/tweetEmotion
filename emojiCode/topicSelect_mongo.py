#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
select topics from mongodb
"""

import pymongo
import re
import codecs
import os
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, AdaptiveETA, AdaptiveTransferSpeed


mongo_client = pymongo.MongoClient("127.0.0.1", 27017)
mongo_twitter = mongo_client.twitter
mongo_tweets = mongo_twitter.tweets

topicDict = {}

output = codecs.open( '../emojiOutput/mongo_topic', 'w', 'utf-8' )
log = codecs.open( '../log/mongo_topic', 'w', 'utf-8' )

def __clean( param ):
    for key, cnt in [ (k,v) for k,v in topicDict.iteritems() ]:
        if cnt < param[0]:
            topicDict.pop( key )

def topicSelect_mongo():
    widgets = [Percentage(), Bar('>') , 'select topics', ReverseBar('<'), Timer()]

    progressSize = mongo_tweets.count()
    #progressSize = 10000000
    progressSlide = progressSize / 100
    with ProgressBar( widgets=widgets, maxval=progressSize ) as progress:
        counter = 0
        #tweets = mongo_tweets.limit(progressSize)
        for tweet in mongo_tweets.find().limit(progressSize):
            text = tweet['text']
            #print text

            regex = r'#\w+'
            matchs = re.findall( regex, text  )
            if not matchs:
                progress.update()
                continue
            #print text
            for words in matchs:
                words = words.lower()
                topicDict.update({ words: topicDict.get( words, 0 ) + 1 } )

            counter += 1
            progress.update( counter )
            if counter % progressSlide == 0:
                __clean([2,])
            if counter == progressSize:
                break
            
    cnt = 0
    sum = 0
    print 'start output'
    for key, value in topicDict.iteritems():
        output.write( '%s\t:%d\n' % ( key , value ) ) 
        cnt += 1
        sum += value
    log.write(  '%d hashtags with %d displays' % ( cnt, sum ) )
    print '%d hashtags with %d displays' % ( cnt, sum )

    pass

if __name__ == '__main__':
    topicSelect_mongo()


