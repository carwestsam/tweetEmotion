#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
calc the term frequency fo the words
"""

import util
import dealTweets as dts
import re
import utilities

tokenizer = utilities.Tokenizer()
formatter = 'abcdefghijklmnopqrstuvwxyz'

def __filter_range( border ):
    l = border[0]
    r = border[1]
    line = dts.readlineI()
    if not line:
        return
    cnt = int(  (line.split(':')) [1] )
    if cnt >= l and cnt <= r :
        dts.writeO( line )

def select_dict():
    dts.setFile( '../output/Dict_raw.txt', '../output/Dict_select.txt', '../log/idf_select.log' )
    dts.setSize( 214884  )
    dts.openFiles()

    dts.loop_with_param( __filter_range, [1000, 34400], 'filter Dict_raw' )

    dts.closeFiles()

def __calcIDF(dict):
    line = dts.readlineI()
    if not line:
        return
    line = re.sub('[!?]', '', line)
    line = re.sub(r'[^\d\w\ ]', '', line)
    for term in tokenizer.tokenize( line ):
        dict.update( { term : dict.get( term, 0 ) + 1 } )


def make_dict():
    dts.setFile( '../output/afterPre.txt', '../output/Dict_raw.txt', '../log/idf.log' )
    dts.setSize( 25770000 )
    dts.openFiles()

    dict = {}
    dts.loop_with_param( __calcIDF, dict, 'calc the Idf' )
    
    print 'start sort and print'
    cnt = 0
    pcnt = 0
    CntDistribution = {}
    CNT_MAX = 1000000
    for x in range ( CNT_MAX+1 ):
        CntDistribution[ x ] = 0
    for key, value in [(k,dict[k]) for k in sorted(dict.keys())]:
        if value > 10 and value < 364600:
            dts.writeO( '%s:%d\n' % (key, value))
            pcnt += 1
        cnt += 1
        if ( value > 364600 ):
            print key
        if ( value > CNT_MAX * 10 ):
            CntDistribution[CNT_MAX] += 1
        else :
            CntDistribution[ value / 10 ] += 1
    

    print '%d words output' % pcnt
    dts.writeL( '%d words output\n' % pcnt )

    print 'printing range log'
    ncnt = 0
    for x in range( CNT_MAX ):
        ncnt += CntDistribution [x]
        dts.writeL( '%7d~%7d:\t%d\n' % ( x*10, (x+1)*10, cnt - ncnt ))

    dts.closeFiles()

if __name__ == '__main__':
    #make_dict()
    select_dict()

