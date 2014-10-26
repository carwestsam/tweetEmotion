#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Divide Emotions
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

def __testEmo():
    line = dts.readlineI()
    if not line:
        return
    obj = json.loads( line )
    if u'\U0001F608' in obj['text']:
        print obj['text']

def __testfind ( ):
    dts.setSize( 3830000 )
    dts.setFile('../emojiOutput/afterPre.txt', '../emojiOutput/EmoAll.txt', '../log/divideEmoticons' )
    dts.openFiles()
    dts.loop( __testEmo, 'test emoji' )
    dts.closeFiles()


ecstaIcons=[ u'\U0001f600', u'\U0001f601', u'\U0001f602',u'\U0001f603', u'\U0001f604', u'\U0001f606', u'\u0001f607', u'\U0001f608', u'\U0001f60A', u'\U0001F60B', u'\U0001f60c', u'\U0001f60E', u'\U0001f60f', u'\U0001f61b', u'\U0001f61c', u'\U0001f61D', u'\U0001f62c', u'\U0001f638', u'\U0001f639', u'\U0001f63A', u'\U0001f63C', u'\U0001f642', u'\U0001f648', u'\U0001f649', u'\U0001f64B']
admirIcons=[u'\U0001f60D', u'\U0001f617', u'\U0001f618', u'\U0001f619', u'\U0001f61a', u'\U0001f63b', u'\U0001f63d', u'\U0001f646', u'\U0001f647', u'\U0001f64f']
terrrIcons=[u'\U0001f613', u'\U0001f61f', u'\U0001f628', u'\U0001f630', u'\U0001f631', u'\U0001f64a']
amazeIcons=[u'\U0001f605', u'\U0001f62e', u'\U0001f62f', u'\U0001f632', u'\U0001f633', u'\U00016f35', u'\U0001f640']
griefIcons=[u'\U0001f614', u'\U0001f616', u'\U0001f61e', u'\U0001f622', u'\U0001f623', u'\U0001f625', u'\U0001f626', u'\U0001f627', u'\U0001f629', u'\U0001f62b', u'\U0001f62d', u'\U0001f63f', u'\U0001f641', u'\U0001f64d', u'\U0001f64e']
loathIcons=[u'\U0001f610', u'\U0001f611', u'\U0001f612', u'\U0001f615', u'\U0001f645']
angerIcons=[u'\U0001f620', u'\U0001f621', u'\U0001f624', u'\U0001f63e']
vigilIcons=[u'\U0001f609']

#ecstaEmo = {'filename': 'ecstaEmo.txt', 'Icons': ecstaIcons, 'cnt':0, 'fileptr':0, 'label':'1'}
#admirEmo = {'filename': 'admirEmo.txt', 'Icons': admirIcons, 'cnt':0, 'fileptr':0, 'label':'2'}
#terrrEmo = {'filename': 'terrrEmo.txt', 'Icons': terrrIcons, 'cnt':0, 'fileptr':0, 'label':'3'}
#amazeEmo = {'filename': 'amazeEmo.txt', 'Icons': amazeIcons, 'cnt':0, 'fileptr':0, 'label':'4'}
#griefEmo = {'filename': 'griefEmo.txt', 'Icons': griefIcons, 'cnt':0, 'fileptr':0, 'label':'5'}
#loathEmo = {'filename': 'loathEmo.txt', 'Icons': loathIcons, 'cnt':0, 'fileptr':0, 'label':'6'}
#angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0, 'fileptr':0, 'label':'7'}
#vigilEmo = {'filename': 'vigilEmo.txt', 'Icons': vigilIcons, 'cnt':0, 'fileptr':0, 'label':'8'}

ecstaEmo = {'filename': 'ecstaEmo.txt', 'Icons': ecstaIcons, 'cnt':0, 'fileptr':0, 'label':'1'}
terrrEmo = {'filename': 'terrrEmo.txt', 'Icons': terrrIcons, 'cnt':0, 'fileptr':0, 'label':'2'}
amazeEmo = {'filename': 'amazeEmo.txt', 'Icons': amazeIcons, 'cnt':0, 'fileptr':0, 'label':'3'}
griefEmo = {'filename': 'griefEmo.txt', 'Icons': griefIcons, 'cnt':0, 'fileptr':0, 'label':'4'}
loathEmo = {'filename': 'loathEmo.txt', 'Icons': loathIcons, 'cnt':0, 'fileptr':0, 'label':'5'}
angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0, 'fileptr':0, 'label':'6'}

#   commit for test Emotion merge
#Emotions = [ecstaEmo, admirEmo, terrrEmo,amazeEmo, griefEmo, loathEmo, angerEmo, vigilEmo ];


Emotions = [ecstaEmo, terrrEmo,amazeEmo, griefEmo, loathEmo, angerEmo ];

outputDir='../emojiOutput/'
tokenizer = utilities.Tokenizer()

def __divide( parList ):
    line = dts.readlineI()
    if not line:
        return
    obj = json.loads( line )
    text = obj['text']

    ans = 0
    for emo in Emotions:
        label = int ( emo['label'] )
        for icon in emo['Icons']:
            if icon in text:
                if 0 == ans or label == ans:
                    ans = label
                else:
                    ans = -1
    
    if ans > 0 :
        ttext = re.sub( '[!?]', '', text )
        ttext = re.sub( '[^\d\w\ ]', '', ttext )
        ttext = re.sub( 'USERNAME', '', ttext )
        ttext = re.sub( 'URL', '', text )
        if len( tokenizer.tokenize( text ) ) <= 3:
            return


    if ans > 0 and  Emotions[ ans - 1 ]['cnt'] < parList[0] :
        Emotions[ ans - 1 ] ['cnt'] += 1
        Emotions[ ans - 1 ] ['fileptr'] . write ( line )


#    totalvote = 0
#    maxvote = 0
#    maxpos = 0
#    for emo in Emotions:
#        label = int( emo['label'] )
#        for icon in emo['Icons']:
#            if icon in text:
#                vote[ label ] += 1
#                totalvote += 1
#                if vote[label] > maxvote:
#                    maxvote = vote [label]
#                    maxpos = label
#
#    if maxvote * 2 > totalvote:
#        tmpemo = Emotions[ maxpos-1 ]
#        if parList[0] >  tmpemo['cnt'] :
#            tmpemo['cnt'] += 1
#            tmpemo['fileptr'] . write( line )


#    for emo in Emotions:
#        if emo['cnt'] >= parList [0]:
#            break
#        for icon in emo['Icons']:
#            if icon in text:
#                emo[ 'cnt' ] += 1
#                if emo['cnt'] < parList[0]:
#                    emo[ 'fileptr' ] . write ( line )

def divideEmoticons():
    dts.setSize( 3830000 )
    dts.setFile('../emojiOutput/EafterPre.txt', '', '../log/divideEmoticons')
    dts.openFiles()

    for emo in Emotions:
        emo [ 'fileptr' ] = codecs.open( outputDir + emo['filename'], 'w', 'utf-8' )

    dts.loop_with_param( __divide, [3000,], 'divide Emotions' )

    for emo in Emotions:
        print '%s\t:\t%d' % ( emo['filename'], emo['cnt'] )
        emo [ 'fileptr' ] . close()
    dts.closeFiles()
    


if __name__ == '__main__':
    divideEmoticons()
    #__testfind()

