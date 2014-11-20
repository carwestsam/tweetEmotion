#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Select topics
"""

import dealTweets as dts
import re
import os
import json
import operator
import pymongo

mongo_client = pymongo.MongoClient("127.0.0.1", 27017 )
twitter_mongo = mongo_client.twitter
tweets_mongo = twitter_mongo.tweets

topicDict = {}

def __dealLine( param ):
    line = dts.readlineI()
    if not line:
        return
    try:
        obj =  json.loads( line )
    except:
        #print line
        nextline = dts.readlineI()
        #print nextline
        return
    text = obj['text']
    regex = r'#\w+'
    matchs = re.findall( regex, text  )
    if not matchs:
        return
    for words in matchs:
        words = words.lower()
        topicDict.update({ words: topicDict.get( words, 0 ) + 1 } )
        #print words

def __clean( param ):
    for key, cnt in [ (k,v) for k,v in topicDict.iteritems() ]:
        if cnt < param[0]:
            topicDict.pop( key )
        

if __name__ == "__main__":
    dts.setSize(13000000)
    
    dts.setFile( '/home/server2103/dump/twitter.tweet.json', '../emojiOutput/topics', '../log/topics.emoji')
    dts.openFiles()
    dts.loop_with_param_clean( __dealLine, __clean, [3,], 'find hashtags' )

    cnt = 0
    sum = 0
    print 'start output'
    for key, value in topicDict.iteritems():
        dts.writeO( '%s\t:%d\n' % ( key , value ) ) 
        cnt += 1
        sum += value
    dts.writeL(  '%d hashtags with %d displays' % ( cnt, sum ) )
    print '%d hashtags with %d displays' % ( cnt, sum )

    dts.closeFiles()
    pass
