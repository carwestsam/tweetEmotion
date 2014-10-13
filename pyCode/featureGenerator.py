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

import codecs
import dealTweets as dts
import checkemoticon 
import preprocess_func
from collections import deque



index_name_dict={}
index_name_cnt = 0

def __getIndex( index_name ):
    global index_name_dict, index_name_cnt
    if -1 == index_name_dict.get( index_name, -1 ):
        index_name_dict.update( {index_name : index_name_cnt })
        index_name_cnt += 1
    return str( index_name_dict.get( index_name, -1 ) )
    


def __calcDistribution_list( list ):
    sum = 0
    for x in list:
        sum += x
    sum += 0.0
    nlist = []
    for x in list:
        if sum == 0 :
            nlist.append( 0 )
        else :
            nlist.append( x / sum )
    return nlist



def __calcDistribution_dict( dict ):
    sum = 0.0
    for x in dict.itervalues():
        sum += x
    newdict = {}
    for key,value in dict.iteritems() :
        if sum == 0:
            newdict.update ( {key: 0} )
        else :
            newdict.update( { key : value / sum } )
    return newdict 

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
    for ch in formatter:
        dict.update({ 'char_%s' % ch : 0 })
    for ch in text:
        if ch in formatter:
            dict.update( { 'char_%s' % ch : dict.get('char_'+ch, 0) + 1 })

    for key,value in __calcDistribution_dict(dict).iteritems():
        idx = __getIndex( key )
        featureList.update({ idx : str(value)})

def __g_each_feature(text):
    #featureList = {"label":"1"}
    featureList = {}
    __att   (text, featureList)
    __que   (text, featureList)
    __chars (text, featureList)
    return featureList

def __g_each_tweet( param ):
    #line = dts.readlineI()
    line = param[1].readline()
    if not line:
        return
    oline = '%s ' % param[0]

    featureList = __g_each_feature(preprocess_func.preprocess(line))

    for t in range( index_name_cnt-1 ):
        oline += str(t) + ':' + featureList[str(t)] + ' '
    #for key,value in featureList.items():
    #    oline += key + ':' + value + ' '

    #return oline
    dts.writeO( oline + '\n' )

def featureGenerator():
    dts.setSize(2000)
    dts.setFile( '../output/afterPre.txt', '../output/feature.txt', '../log/featureGenerator.log' )
    dts.openFiles()

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

