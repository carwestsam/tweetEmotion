#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
merge the answer and predict from ../Compare_Output/
"""

import re
import json
import os
import codecs
import divideByEmoji as dbe
import sys

__type = 'uniemo'
inputPrefix = '../Compare_Output/predict_'+__type+'_'
outputPrefix = '../Compare_Output/merge_' + __type + '_'
ansPrefix = '../Compare_Output/test_ans_' + __type + '_'

def calc(ifilename, afilename, emoname):
    #print '----------------'
    #print 'ifilename:%s\nafilename:%s' %( ifilename, afilename )
    
    ptr={'pf': 0, 'af': 0, }
    with open( afilename ) as afile:
        ptr['af'] = afile.readlines()
    with open( ifilename ) as ifile:
        ptr['pf'] = ifile.readlines()

    length1 = len( ptr['pf'] )
    length2 = len( ptr['af'] )

    if length1 != length2:
        print '%s:\terror legnth %d %d' % ( emoname, length1, length2 )
        return

    tp = 0.0
    tn = 0.0
    fp = 0.0
    fn = 0.0

    for x in range( 0, length1 ):
        predict = float( ptr['pf'][x] )
        ans = float( ptr['af'][x] )
        
        if predict > 0:
            if ans > 0:
                tp += 1
            elif ans < 0:
                fp += 1
            else :
                print 't error'
        elif predict < 0:
            if ans > 0:
                tn += 1
            elif ans < 0:
                fn += 1
            else :
                print 'f error'
        else :
            print 'tf error '

    print '----'
    print 'tp:%d tn:%d fp:%d fn:%d' % ( tp, tn, fp, fn )

    print '%s:precition:%f,recall:%f,f1:%f' % ( emoname, tp/(tp+fp+0.0001), tp/(tp+fn+0.00001), (2*tp)/(2*tp+fp+fn+0.00001) )
    

def merge( var1=0, var2=0 ):

    var1 = int( var1 )
    var2 = int( var2 )

    print 'test for s:%d t:%d' % ( var1, var2 )

    all_afilename = '%s%s' % ( ansPrefix, 'all' )
    all_ifilename = '%s%s_%d_%d' % ( inputPrefix, 'all', var1, var2 )
    #calc( all_ifilename, all_afilename, 'all' )

    for emo in dbe.Emotions:
        afilename = '%s%s' % ( ansPrefix , emo['name'] )
        ifilename = '%s%s_%d_%d' % ( inputPrefix, emo['name'], var1, var2 )
        #print afilename
        #print ifilename
        calc ( ifilename, afilename, emo['name'] )


#        ptr={'pf': 0, 'af': 0, }
#        with open( afilename ) as afile:
#            ptr['af'] = afile.readlines()
#        with open( ifilename ) as ifile:
#            ptr['pf'] = ifile.readlines()
#
#        length1 = len( ptr['pf'] )
#        length2 = len( ptr['af'] )
#
#        if length1 != length2:
#            print '%s:\terror legnth %d %d' % ( emo['name'], length1, length2 )
#            continue
#
#        tp = 0.0
#        tn = 0.0
#        fp = 0.0
#        fn = 0.0
#
#        for x in range( 0, length1 ):
#            predict = float( ptr['pf'][x] )
#            ans = float( ptr['af'][x] )
#            
#            if predict > 0:
#                if ans > 0:
#                    tp += 1
#                elif ans < 0:
#                    fp += 1
#                else :
#                    print 't error'
#            elif predict < 0:
#                if ans > 0:
#                    tn += 1
#                elif ans < 0:
#                    fn += 1
#                else :
#                    print 'f error'
#            else :
#                print 'tf error '
#
#        print '-------------'
#        print 'tp:%d tn:%d fp:%d fn:%d' % ( tp, tn, fp, fn )
#
#        print '%s:precition:%f,recall:%f,f1:%f' % ( emo['name'], tp/(tp+fp+0.0001), tp/(tp+fn+0.00001), (2*tp)/(2*tp+fp+fn+0.00001) )



    pass

if __name__ == "__main__":
    merge( sys.argv[1], sys.argv[2] )
    pass


