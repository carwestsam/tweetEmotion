#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
noRT
noDup
noUnknownChars
devide in to emotion files
"""

import codecs
import dealTweets as dts
import os
import re
import sys
import json

tweets = set()

def __cleanRT( text ):
    if 'RT ' in text:
        return None
    return text

def __readin( tweetSet ):
    line = dts.readlineI()
    if not line:
        return
    #print '\n'+ line
    
#    if not re.match( r'\}\s*$', line ):
#        nline = dts.readlineI()
#        
#        if not nline:
#            return
#        line += nline 


    try:
        obj =  json.loads( line )
    except:
        #print line
        #nextline = dts.readlineI()
        #print nextline
        return

    text = __cleanRT ( obj['text'] )
    if not text:
        return
    else:
        tweetSet.add( text )

def __cleanUp( text ):
    pass

def __preProcess():
    dts.loop_with_param(__readin, tweets, 'loading files')
    for tweet in tweets:
        #dts.writeO( tmp + '\n' )
        tmp = { u'text': tweet }
        dts.writeO( json.dumps(tmp) + '\n' )
    setlen = len( tweets )
    print '%d tweets remaining' % setlen
    dts.writeL( '%d tweets remaining' % setlen )

def preAll():
    dts.setSize( 7000000 )
    dts.setFile( '../data/twitter.tweets.json', '../hashOutput/afterPre.txt', '../log/EmojiPre.log' )
    dts.openFiles()
    __preProcess()
    dts.closeFiles()

if __name__ == '__main__':
    preAll()

