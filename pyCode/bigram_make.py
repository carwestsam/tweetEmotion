#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Make the dict of bigram
"""

import dealTweets as dts
import re
import codecs
import utilities

tokenizer = utilities.Tokenizer()

def __bigram(dict) :
    text = dts.readlineI()
    if not text:
        return
    text = re.sub('[!?]', '', text)
    text = re.sub('[^\d\w\ ]', '', text)
    
    tokens = tokenizer.tokenize( text )
    
    for wx in tokens:
        for wy in tokens :
            tmpstr = wx + '#' + wy
            dict.update( { tmpstr : dict.get( tmpstr, 0 ) + 1 } )

def __bigram_clean(dict):
    for key, value in [(key, cnt) for key, cnt in dict.iteritems()]:
        if cnt < 10:
            dict.pop( key, 0 )
    

def make_bigram():
    
    dict = {}
    dts.loop_with_param_clean( __bigram,  __bigram_clean , dict,'Make the dict of bigram' )
    
    print 'start to output'

    cntList = {}
    for x in range ( 100000 ):
        cntList.update( { x : 0 } )
    for k,v in dict.iteritems():
        if v > 10:
            dts.writeO( k + ':' + str(v) + '\n' )
        if v >= 100000 :
            cntList.update ( { 100000:  cntList.get( 100000, 0 ) } )
        else :
            cntList.update( { v : cntList.get( v, 0 ) + 1 } )

    for k,v in cntList.iteritems():
        dts.writeL( str(k) + ':' + str ( v ) + '\n')

def bigram():
    dts.setFile( '../output/afterPre.txt', '../output/BiDict.txt', '../log/bigram.txt' )
    dts.setSize( 25000000 )
    dts.openFiles()
    make_bigram()
    dts.closeFiles()

def __filter_bigram( ran ):
    line = dts.readlineI()
    if not line:
        return
    left = ran[0]
    right = ran[1]
    num = int ( line.split(':') [1] )
    if num >= left and num <= right:
        dts.writeO( line  )

def select_bigram():
    dts.setFile( '../output/BiDict.txt', '../output/select_bigram.txt', '../log/select_bigram' )
    dts.setSize( 389920 )
    dts.openFiles()
    dts.loop_with_param( __filter_bigram, [100,100000], 'filter_bigram' )
    dts.closeFiles()

if __name__ == '__main__':
    bigram()
    #select_bigram()

