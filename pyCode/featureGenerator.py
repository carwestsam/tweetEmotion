#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
feature Generator 
"""

import util
import codecs
import dealTweets as dts
import checkemoticon 
import preprocess_func
from collections import deque
import utilities
import re


tokenizer = utilities.Tokenizer()

index_name_dict={}
index_name_cnt = 0

def __getIndex( index_name ):
    global index_name_dict, index_name_cnt
    if -1 == index_name_dict.get( index_name, -1 ):
        index_name_dict.update( {index_name : index_name_cnt })
        index_name_cnt += 1
    return index_name_dict.get( index_name, -1 ) 
    

def __att(text, featureList):
    cnt = 0
    for x in text:
        if x == '!':
            cnt += 1
    index = __getIndex ( 'att' ) 
    featureList.update({ index : str( cnt )})

def __que(text, featureList):
    cnt = 0
    for x in text:
        if x == '?':
            cnt += 1
    idx = __getIndex( 'que' )
    featureList.update({ idx : str( cnt )})

def __chars( text, featureList ):
    formatter = 'abcdefghijklmnopqrstuvwxyz1234567890'
    #formatter = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    #for ch in formatter:
    #    dict.update({ 'char_%s' % ch : 0 })
    for ch in text:
        if ch in formatter:
            dict.update( { 'char_%s' % ch : dict.get('char_'+ch, 0) + 1 })

    for key,value in util.__calcDistribution_dict(dict).iteritems():
        idx = __getIndex( key )
        featureList.update({ idx : str(value)})


def __words( text, featureList ):
    text = re.sub('[!?]', '', text)
    text = re.sub('[^\d\w\ ]', '', text)
    dict = {}
    for term in tokenizer.tokenize( text ):
        dict.update( { 'words_%s' % term : dict.get( 'words_%s' % term, 0 ) + 1 } )
    for key,value in dict.iteritems():
        idx = __getIndex( key )
        featureList.update({ idx : str(value) })

__att_SELECT = False
__que_SELECT = False
__chars_SELECT = False
__words_SELECT = False

def __g_each_feature(text):
    #featureList = {"label":"1"}
    featureList = {}
    if __att_SELECT :
        __att   (text, featureList)
    if __que_SELECT :
        __que   (text, featureList)
    if __chars_SELECT :
        __chars (text, featureList)
    if __words_SELECT :
        __words (text, featureList)
    return featureList

def __g_each_tweet( param ):
    #line = dts.readlineI()
    line = param[1].readline()
    if not line:
        return
    oline = '%s ' % param[0]

    featureList = __g_each_feature(preprocess_func.preprocess(line))

    
    for key, value in [(k,featureList[k]) for k in sorted(featureList.keys())]:
        oline += str(key) + ':' + value + ' '
    
    #for t in range( index_name_cnt-1 ):
    #    oline += str(t) + ':' + featureList[str(t)] + ' '
    #for key,value in featureList.items():
    #    oline += key + ':' + value + ' '

    #return oline
    dts.writeO( oline + '\n' )

def __featureGenerator_init(): 
    global __att_SELECT, __que_SELECT, __chars_SELECT, __words_SELECT
    
    __getIndex ( 'att' ) 
    __att_SELECT = True

    __getIndex ( 'que' )
    __que_SELECT = True
    
    formatter = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for ch in formatter:
        __getIndex( 'char_%s' % ch )
    __chars_SELECT = True
    
    ifile = codecs.open( '../output/Dict_select.txt', 'r', 'utf-8' )
    for x in range ( 20000 ):
        line = ifile.readline()
        if not line:
            break
        word = line.split( ':' )[0]
        __getIndex( 'words_%s' % word )
    ifile.close()
    __words_SELECT = True



def featureGenerator():
    dts.setSize(3000)
    dts.setFile( '../output/afterPre.txt', '../output/feature.txt', '../log/featureGenerator.log' )
    dts.openFiles()

    __featureGenerator_init()

    for emo in checkemoticon.Emotions:
        filename = checkemoticon.outputDir + emo['filename']
        ifile = codecs.open( filename, 'r', 'utf-8' )
        #print 'Processing %s:' % emo['filename']
        dts.loop_with_param( __g_each_tweet, [emo['label'], ifile] , emo['filename']  )
        ifile.close()

    #dts.loop( __g_each_tweet, 'feature Generator' )

    dts.closeFiles()

if __name__ == '__main__':
    featureGenerator()

