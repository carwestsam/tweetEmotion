#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Divide By Emoji
for the sertain type of emotion


input file:
    ../emojiOutput/afterPre.txt -- an no dup, no RT,  json format, from preAll.py

output file:
    ../emojiOutput/labeled_by_emoji_[EMO].txt -- an json format file, label by
    emoji, [EMO] is an sertain type of emo. ( json: {'text':twitter_text,
    'label':labelname} )


"""

import re
import json
import os
import sys
import math
import codecs
import utilities
import os
import dealTweets as dts

ecstaIcons=[ u'\U0001f600', u'\U0001f601', u'\U0001f602',u'\U0001f603', u'\U0001f604', u'\U0001f606', u'\u0001f607', u'\U0001f608', u'\U0001f60A', u'\U0001F60B', u'\U0001f60c', u'\U0001f60E', u'\U0001f60f', u'\U0001f61b', u'\U0001f61c', u'\U0001f61D', u'\U0001f62c', u'\U0001f638', u'\U0001f639', u'\U0001f63A', u'\U0001f63C', u'\U0001f642', u'\U0001f648', u'\U0001f649', u'\U0001f64B']
admirIcons=[u'\U0001f60D', u'\U0001f617', u'\U0001f618', u'\U0001f619', u'\U0001f61a', u'\U0001f63b', u'\U0001f63d', u'\U0001f646', u'\U0001f647', u'\U0001f64f']
terrrIcons=[u'\U0001f613', u'\U0001f61f', u'\U0001f628', u'\U0001f630', u'\U0001f631', u'\U0001f64a']
amazeIcons=[u'\U0001f605', u'\U0001f62e', u'\U0001f62f', u'\U0001f632', u'\U0001f633', u'\U00016f35', u'\U0001f640']
griefIcons=[u'\U0001f614', u'\U0001f616', u'\U0001f61e', u'\U0001f622', u'\U0001f623', u'\U0001f625', u'\U0001f626', u'\U0001f627', u'\U0001f629', u'\U0001f62b', u'\U0001f62d', u'\U0001f63f', u'\U0001f641', u'\U0001f64d', u'\U0001f64e']
loathIcons=[u'\U0001f610', u'\U0001f611', u'\U0001f612', u'\U0001f615', u'\U0001f645']
angerIcons=[u'\U0001f620', u'\U0001f621', u'\U0001f624', u'\U0001f63e']
vigilIcons=[u'\U0001f609']

ecstaEmo = {'name': 'ecsta.txt', 'Icons': ecstaIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'1'}
admirEmo = {'name': 'admir.txt', 'Icons': admirIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'2'}
terrrEmo = {'name': 'terrr.txt', 'Icons': terrrIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'3'}
amazeEmo = {'name': 'amaze.txt', 'Icons': amazeIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'4'}
griefEmo = {'name': 'grief.txt', 'Icons': griefIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'5'}
loathEmo = {'name': 'loath.txt', 'Icons': loathIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'6'}
angerEmo = {'name': 'anger.txt', 'Icons': angerIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'7'}
vigilEmo = {'name': 'vigil.txt', 'Icons': vigilIcons, 'cnt':0, 'ncnt':0, 'fileptr':0, 'label':'8'}

Emotions = [ecstaEmo,admirEmo, terrrEmo, amazeEmo, griefEmo, loathEmo, angerEmo, vigilEmo ];
OutputDir = '../emojiOutput/test_labeled_by_emoji_'
tokenizer = utilities.Tokenizer()

GC = 0
def __divide():
    line = dts.readlineI()
    if not line:
        return


    global GC
    if GC < 1000000:
        GC += 1
        return

    try:
        obj = json.loads( line )
    except:
        return

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
        text = re.sub( '[!?]', '', text )
        text = re.sub( '[^\d\w\ ]', '', text )
        text = re.sub( 'USERNAME', '', text )
        text = re.sub( 'URL', '', text )
        if len( tokenizer.tokenize( text ) ) <= 3:
            return

        tmp = {u'text':text, u'label':ans}
        dts.writeO( json.dumps(tmp) + '\n' )

        for emo in Emotions:
            label = 0
            #print '%d:%d\n' % ( ans, int(emo['label'] ))
            if ans == int(emo['label']):
                label = 1
                Emotions[ ans - 1 ][ 'cnt' ] += 1
                tmp = {u'text':text, u'label':label}
                emo['fileptr'].write( json.dumps(tmp) + '\n' )
            else :
                if Emotions[ans-1]['ncnt'] < Emotions[ans-1]['cnt']:
                    label = -1
                    Emotions[ ans - 1 ][ 'ncnt' ] += 1
                    tmp = {u'text':text, u'label':label}
                    emo['fileptr'].write( json.dumps(tmp) + '\n' )

    pass

if __name__ == "__main__":
    dts.setSize( 2000000 )
    dts.setFile( '../emojiOutput/afterPre.txt','../emojiOutput/test_featre_all', '../log/test_labeled_by_emoji_log' )
    dts.openFiles()
    for emo in Emotions: 
        emo[ 'fileptr' ] = codecs.open( OutputDir + emo['name'], 'w', 'utf-8' )
    dts.loop( __divide, 'divide and label twiiters' )
    for emo in Emotions:
        print '%s\t:\t%d' % ( emo['name'] , emo['cnt'] )
        dts.writeL( '%s\t:\t%d\n' % ( emo['name'] , emo['cnt']  ))
        emo['fileptr'] .close()
    dts.closeFiles()
    pass

