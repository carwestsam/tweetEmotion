#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
pass and pass the tweets to check if some emoticons left
"""

import re
import codecs
import dealTweets as dts

def __bandWords( tweet ):
    tweet = re.sub('h…', 'URL', tweet)  #deal with truncated url
    tweet = re.sub('ht?….*$', 'URL', tweet) #deal with truncated url
    tweet = re.sub('(^|)?http?s?:?/?/?.*?( |$)', 'URL', tweet) #deal with compelted url
    tweet = re.sub('\.?@.*?( |:|$)', 'USERNAME ', tweet) #deal with username
    noWD = re.sub( r'\w{2,}', ' ', tweet )
    noAt = re.sub( '@', '', noWD )
    noListWhite = re.sub( r'[ \t]+', ' ', noAt )
    return noListWhite

def __cleanTweet():
    dts.writeO( __bandWords(dts.readlineI()) )
    


def filterEmoticons():
    dts.setSize( 310000 )
    dts.setFile( '../data/tweet_noRT_noDup.txt', '../tmp/filter.out', '../log/filterEmoticons.log' )
    dts.openFiles()
    dts.loop( __cleanTweet, 'clean Tweets' )
    dts.closeFiles()

if __name__ == '__main__':
    filterEmoticons()


