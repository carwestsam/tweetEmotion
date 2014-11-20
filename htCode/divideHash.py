#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Divide by hashtag
"""

import re
import dealTweets as dts
import os
import sys
import codecs
import json
import math
import preprocess_func
import utilities
import json

haacList = [u'#elated', u'#overjoyed', u'#enjoy', u'#excited', u'#proud', u'#joyful', u'#feelhappy', u'#sohappy', u'#veryhappy', u'#happy', u'#superhappy', u'#happytweet', u'#feelblessed', u'#blessed', u'#amazing', u'#wonderful', u'#excelent', u'#delighted', u'#enthusiastic']
hainList = [u'#calm', u'#calming', u'#peaceful', u'#quiet', u'#silent', u'#serene', u'#convinced', u'#consent', u'#contented', u'#contentment', u'#satisfied', u'#relax', u'#relaxed', u'#relaxing', u'#sleepy', u'#sleepyhead', u'#asleep', u'#resting', u'#restful', u'#placid'] 
unacList = [u'#nervous', u'#anxious', u'#tension', u'#afraid', u'#fearful', u'#angry', u'#annoyed', u'#annoying', u'#stress', u'#distressed', u'#distress', u'#strssful', u'#stressed', u'#worried', u'#tense', u'#bothered', u'#disturbed', u'#irritated', u'#mad', u'#furious']
uninList = [u'#sadifeelsad', u'#feelsad', u'#sosad', u'#verysad', u'#sorrow', u'#disppointed', u'#supersad', u'#miserable', u'#hopeless', u'#depress', u'#depressed', u'#depression', u'#fatigued', u'#gloomy', u'#nothappy', u'#unhappy', u'#suicidal', u'#downhearted', u'#hapless', u'#dispirited']

haacEmo = { 'hashList': haacList, 'cnt':0, 'label': 1 }
hainEmo = { 'hashList': hainList, 'cnt':0, 'label': 2 }
unacEmo = { 'hashList': unacList, 'cnt':0, 'label': 3 }
uninEmo = { 'hashList': uninList, 'cnt':0, 'label': 4 }

EmoList = [ haacEmo, hainEmo, unacEmo, uninEmo ]

def __label( text ):
    label = 0
    for emo in EmoList:
        for hashtag in emo['hashList']:
            if hashtag in text:
                if label == 0 or label == emo['label']:
                    label = emo['label']
                else :
                    return 0
    if label != 0:
        EmoList[ label - 1 ]['cnt'] += 1
    return label

def __divide():
    line = dts.readlineI()
    if not line:
        return
    obj = json.loads( line )
    text = obj['text']
    label = __label( text )
    if label > 0:
        obj['label'] = label
        dts.writeO( json.dumps( obj ) + '\n' )

def divideHashtag():
    dts.setSize( 1000000 )
    dts.setFile( '../hashOutput/afterPre.txt', '../hashOutput/divideHashtag.txt', '../log/divideHashtag.log' )
    dts.openFiles()

    dts.loop ( __divide, 'divide by Hashtag' )
    for emo in EmoList:
        print 'label %d \t: %d' % ( emo['label'], emo['cnt'] )
        dts.writeL('label %d \t: %d\n' % ( emo['label'], emo['cnt'] ))

    dts.closeFiles()

if __name__ == '__main__':
    divideHashtag()

