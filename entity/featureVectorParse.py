#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Parse featureVector
"""

import dealTweets as dts
import codecs

name_dict = {}
index_dict = 1


def __getIndex( index_name ):
    global name_dict, index_dict
    return  name_dict.get( index_name, 0 )

def __lineParse():
    line = dts.readlineI()
    if not line:
        return
    obj = eval(line)
    output = str ( obj[1] ) + ' '
    wordlist = {}
    for word,value in obj[0].iteritems():
        if value > 0 :
            index = __getIndex( word )
            if index > 0:
                wordlist.update( { index : value} )
    
    for key, value in [(k,wordlist[k]) for k in sorted(wordlist.keys())]:
        output+= str( key ) + ':' + str( value ) + ' '

    #if obj[1] > 0:
    #    dts.writeO( output + '\n' )
    dts.writeO( output + '\n' )
    

def featureVectorParse():
    topicList = [ur"#emabiggestfans1d", ur"#emabiggestfansjustinbieber", ur"#porn", ur"#ipad", ur"#halloween", ur"#emabiggestfans5sos", ur"#stealmygirl", ur"#thewalkingdead", ur"#ebola", ur"#emabiggestfansarianagrande", ur"#lol"]
    
    dfile = codecs.open( '../log/featureWang', 'r', 'utf-8' )
    line = dfile.readline()
    global name_dict
    name_dict = eval( line )
    dfile.close()

    for topic in topicList:
        ifilename = '../entityOutput/topicTwitter_' + topic[1:]
        ofilename = '../entityOutput/topicFeat_' + topic[1:]
        lfilename = '../log/featureVectorParse_entity'

        dts.setSize( 50000 )
        dts.setFile( ifilename, ofilename, lfilename )
        dts.openFiles()
        dts.loop( __lineParse, 'parse featvect:' + topic )
        dts.closeFiles()

if __name__ == "__main__":
    featureVectorParse()
    pass

